# == Basic ICTL Studio Online ==
# app.py
# Licensed under GNU GPL v3 License (https://www.gnu.org/licenses/)
# Source: https://github.com/indiancoder3/abhinu-dev_basic-ictl

# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# This is a simple Flask app that serves the ICTL Studio Online interface and manages 
# a single global interpreter process.
# Hosted online at indiancoder3.github.io/abhinu-dev_basic-ictl/editor.html 
# (it may take a few seconds to "wake up" due to free hosting limitations).

from flask import Flask, render_template, request
from flask_sock import Sock
import subprocess
import sys
import threading
import time
import os
import json
import logging
from pathlib import Path
import uuid

app = Flask(__name__, static_folder='static', template_folder='templates')
sock = Sock(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration constants
TEMP_FILE = 'temp.ictl'

# Single global process (simple). Protect with lock.
process = None
process_lock = threading.Lock()

def start_process(code):
    global process
    with process_lock:
        # stop existing
        if process and process.poll() is None:
            try:
                process.terminate()
                process.wait(timeout=1)
            except Exception:
                try:
                    process.kill()
                except Exception:
                    pass
            process = None

        # write temp file
        with open(TEMP_FILE, "w", encoding="utf-8") as f:
            f.write(code)

        # start interpreter unbuffered
        process = subprocess.Popen(
            [sys.executable, '-u', 'main.py', TEMP_FILE],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=0,
            text=True
        )
        return process

def stop_process():
    global process
    with process_lock:
        if process and process.poll() is None:
            try:
                process.terminate()
                process.wait(timeout=1)
            except Exception:
                try:
                    process.kill()
                except Exception:
                    pass
            process = None
            return True
    return False

@sock.route('/ws')
def websocket(ws):
    """
    Protocol: client sends JSON messages:
      {"cmd":"run", "code":"..."}      -> start interpreter
      {"cmd":"stop"}                   -> stop interpreter
      {"cmd":"input", "text":"..."}    -> send a line to stdin (no newline appended)
    Server sends raw text frames containing interpreter output (exact characters).
    Server may also send JSON control messages prefixed with "JSON:" for events:
      "JSON:{"event":"finished"}"
      "JSON:{"event":"stopped"}"
    """
    global process
    client_id = str(uuid.uuid4())[:8]
    logger.info(f"Client {client_id} connected")
    watcher = None
    watcher_stop = threading.Event()

    def watcher_thread(proc, stop_evt):
        try:
            # Read character-by-character and send as text frames
            while True:
                if stop_evt.is_set():
                    break
                ch = proc.stdout.read(1)
                if ch == '':
                    break
                try:
                    ws.send(ch)
                except Exception:
                    # client disconnected
                    break
            # drain remaining
            remaining = proc.stdout.read()
            if remaining:
                try:
                    ws.send(remaining)
                except Exception:
                    pass
        except Exception as e:
            try:
                ws.send(f"[Watcher error] {e}")
            except Exception:
                pass
        finally:
            # notify client that process finished
            try:
                ws.send("JSON:" + json.dumps({"event":"finished"}))
            except Exception:
                pass

    try:
        while True:
            msg = ws.receive()
            if msg is None:
                # client disconnected
                break

            # Expect JSON commands from client
            try:
                data = json.loads(msg)
            except Exception:
                # ignore non-json messages
                continue

            cmd = data.get('cmd')
            if cmd == 'run':
                code = data.get('code', '')
                proc = start_process(code)
                # start watcher thread for this connection
                watcher_stop.clear()
                watcher = threading.Thread(target=watcher_thread, args=(proc, watcher_stop), daemon=True)
                watcher.start()
                # ack
                ws.send("JSON:" + json.dumps({"event":"started"}))
            elif cmd == 'stop':
                stopped = stop_process()
                # signal watcher to stop if running
                watcher_stop.set()
                ws.send("JSON:" + json.dumps({"event":"stopped", "stopped": stopped}))
            elif cmd == 'input':
                text = data.get('text', '')
                # write to stdin with newline
                with process_lock:
                    if process and process.poll() is None and process.stdin:
                        try:
                            process.stdin.write(text + '\n')
                            process.stdin.flush()
                        except Exception as e:
                            ws.send(f"[Input error] {e}")
                    else:
                        ws.send("[Input error] No running process")
            else:
                logger.warning(f"Unknown command from client {client_id}: {cmd}")
                try:
                    ws.send(f"JSON:" + json.dumps({"event": "error", "message": "Unknown command"}))
                except Exception:
                    pass
    finally:
        watcher_stop.set()
        logger.info(f"Client {client_id} handler cleanup")

@app.route('/')
def index():
    """Serve the main editor page."""
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Failed to render template: {e}")
        return "Error loading editor", 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'ok'}, 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return {'error': 'Not found'}, 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {error}")
    return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    # Ensure temp file exists
    try:
        temp_path = Path(TEMP_FILE)
        temp_path.touch(exist_ok=True)
        logger.info(f"Initialized temp file: {TEMP_FILE}")
    except Exception as e:
        logger.warning(f"Failed to create temp file: {e}")
    
    logger.info("Starting ICTL Studio Server on port 5000")
    try:
        app.run(debug=True, port=5000, threaded=True, use_reloader=False)
    except KeyboardInterrupt:
        logger.info("Shutting down...")
        stop_process()
    except Exception as e:
        logger.error(f"Server error: {e}")
    finally:
        # Cleanup
        try:
            stop_process()
            logger.info("Cleanup complete")
        except Exception as e:
            logger.warning(f"Cleanup error: {e}")
