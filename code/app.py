# == Basic ICTL Studio Online ==
# app.py
# Licensed under GNU GPL v3 License (https://www.gnu.org/licenses/)
# Source: https://github.com/indiancoder3/abhinu-dev_basic-ictl

# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, render_template, request
from flask_sock import Sock
import subprocess
import sys
import threading
import time
import os
import json

app = Flask(__name__, static_folder='static', template_folder='templates')
sock = Sock(app)

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
        with open("temp.ictl", "w", encoding="utf-8") as f:
            f.write(code)

        # start interpreter unbuffered
        process = subprocess.Popen(
            [sys.executable, '-u', 'main.py', 'temp.ictl'],
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
                # unknown command
                ws.send("JSON:" + json.dumps({"event":"error", "message":"unknown command"}))
    finally:
        # cleanup on disconnect
        watcher_stop.set()
        # do not automatically kill process on client disconnect; keep it simple
        return

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists("temp.ictl"):
        open("temp.ictl", "w").close()
    app.run(debug=True, port=5000, threaded=True)
