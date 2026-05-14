"""
ICTL Modern GUI Interpreter
A sleek, modern GUI-based interpreter for ICTL language using PySide6 (Qt6)
"""

import sys
import os
from pathlib import Path
import subprocess
import tempfile

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QSplitter, QLabel, QStatusBar, QMenuBar,
    QMenu, QFileDialog, QMessageBox, QTabWidget, QScrollArea, QFrame
)
from PySide6.QtCore import Qt, QSize, QTimer, QThread, Signal, QProcess
from PySide6.QtGui import QIcon, QFont, QColor, QKeySequence, QAction, QTextCursor

from ui.code_editor import CodeEditor
from ui.output_console import OutputConsole
from ui.sidebar import SideBar
from interpreter.executor import ICTLExecutor


class ICTLGuiInterpreter(QMainWindow):
    """Main window for the ICTL GUI Interpreter"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ICTL Modern Interpreter - Untitled")
        self.setGeometry(100, 100, 1400, 900)
        
        # Initialize components
        self.executor = ICTLExecutor()
        self.current_file = None
        self.modified = False
        
        # Setup UI
        self.setup_ui()
        self.setup_menu()
        self.apply_modern_style()
        
        self.show()
    
    def setup_ui(self):
        """Setup the main user interface"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setStyleSheet("QWidget { margin: 0px; padding: 0px; }")
        
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = SideBar(self)
        main_layout.addWidget(self.sidebar)
        
        # Main content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Splitter for code editor and console
        splitter = QSplitter(Qt.Vertical)
        splitter.setStyleSheet("QSplitter::handle { background-color: #2b2b2b; height: 4px; }")
        
        # Code Editor
        self.code_editor = CodeEditor()
        splitter.addWidget(self.code_editor)
        
        # Output Console
        self.output_console = OutputConsole()
        splitter.addWidget(self.output_console)
        
        # Set initial sizes (70% editor, 30% console)
        splitter.setSizes([630, 270])
        
        content_layout.addWidget(splitter)
        
        # Bottom control panel
        bottom_panel = QWidget()
        bottom_panel.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                border-top: 1px solid #3d3d3d;
            }
        """)
        bottom_panel.setFixedHeight(50)
        
        button_layout = QHBoxLayout(bottom_panel)
        button_layout.setContentsMargins(10, 8, 10, 8)
        button_layout.setSpacing(8)
        
        self.run_button = self._create_button("▶ Run Code", "#4CAF50", "#45a049", "#3d8b40")
        self.run_button.clicked.connect(self.run_code)
        
        self.clear_button = self._create_button("🗑 Clear Output", "#f44336", "#da190b", "#ba0000")
        self.clear_button.clicked.connect(self.output_console.clear)
        
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        
        content_layout.addWidget(bottom_panel)
        
        main_layout.addWidget(content_widget, 1)
        
        # Status bar
        self.statusBar().showMessage("Ready")
    
    def _create_button(self, text, bg_color, hover_color, pressed_color):
        """Create a styled button"""
        btn = QPushButton(text)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: white;
                border: none;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
                padding: 6px 12px;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
        """)
        return btn
    
    def setup_menu(self):
        """Setup menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        new_action = file_menu.addAction("New")
        new_action.triggered.connect(self.new_file)
        
        open_action = file_menu.addAction("Open")
        open_action.triggered.connect(self.open_file)
        
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_file)
        
        save_as_action = file_menu.addAction("Save As...")
        save_as_action.triggered.connect(self.save_file_as)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        undo_action = edit_menu.addAction("Undo")
        undo_action.triggered.connect(self.code_editor.undo)
        
        redo_action = edit_menu.addAction("Redo")
        redo_action.triggered.connect(self.code_editor.redo)
        
        # Run menu
        run_menu = menubar.addMenu("Run")
        
        run_action = run_menu.addAction("Run Code")
        run_action.triggered.connect(self.run_code)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = help_menu.addAction("About ICTL")
        about_action.triggered.connect(self.show_about)
    
    def apply_modern_style(self):
        """Apply modern dark theme stylesheet"""
        style = """
        QMainWindow, QWidget {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        
        QMenuBar {
            background-color: #2b2b2b;
            color: #ffffff;
            border-bottom: 1px solid #3d3d3d;
        }
        
        QMenuBar::item:selected {
            background-color: #404040;
        }
        
        QMenu {
            background-color: #2b2b2b;
            color: #ffffff;
            border: 1px solid #3d3d3d;
        }
        
        QMenu::item:selected {
            background-color: #404040;
        }
        
        QStatusBar {
            background-color: #2b2b2b;
            color: #ffffff;
            border-top: 1px solid #3d3d3d;
        }
        
        QTextEdit {
            background-color: #252526;
            color: #d4d4d4;
            border: none;
            border-radius: 0px;
        }
        
        QScrollBar:vertical {
            background-color: #1e1e1e;
            width: 12px;
            border: none;
        }
        
        QScrollBar::handle:vertical {
            background-color: #4a4a4a;
            border-radius: 6px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background-color: #5a5a5a;
        }
        """
        self.setStyleSheet(style)
    
    def run_code(self):
        """Execute the ICTL code in the editor"""
        code = self.code_editor.toPlainText()
        
        if not code.strip():
            self.output_console.append_output("❌ No code to execute!", "error")
            return
        
        self.output_console.clear()
        self.output_console.append_output("▶ Executing ICTL code...\n", "info")
        self.run_button.setEnabled(False)
        
        try:
            # Execute ICTL code
            output = self.executor.execute(code)
            
            if output.strip():
                self.output_console.append_output(output, "success")
            else:
                self.output_console.append_output("✓ Code executed successfully (no output)", "success")
            
            self.statusBar().showMessage("✓ Execution completed successfully")
        except Exception as e:
            error_msg = f"❌ {str(e)}"
            self.output_console.append_output(error_msg, "error")
            self.statusBar().showMessage("✗ Execution failed")
        finally:
            self.run_button.setEnabled(True)
    
    def new_file(self):
        """Create a new file"""
        if self.modified:
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "Do you want to save changes before creating a new file?"
            )
            if reply == QMessageBox.Yes:
                self.save_file()
        
        self.code_editor.clear()
        self.current_file = None
        self.modified = False
        self.setWindowTitle("ICTL Modern Interpreter - Untitled")
        self.statusBar().showMessage("New file created")
    
    def open_file(self):
        """Open a file dialog"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open ICTL File", "", "ICTL Files (*.ictl);;All Files (*)"
        )
        
        if file_path:
            self.open_file_direct(file_path)
            self.sidebar.add_file(file_path)
    
    def open_file_direct(self, file_path):
        """Open a file directly without dialog"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            self.code_editor.setPlainText(content)
            self.current_file = file_path
            self.modified = False
            self.setWindowTitle(f"ICTL Modern Interpreter - {Path(file_path).name}")
            self.statusBar().showMessage(f"Opened: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")
    
    def save_file(self):
        """Save the current file"""
        if not self.current_file:
            self.save_file_as()
        else:
            try:
                with open(self.current_file, 'w') as f:
                    f.write(self.code_editor.toPlainText())
                self.modified = False
                self.statusBar().showMessage(f"Saved: {self.current_file}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")
    
    def save_file_as(self):
        """Save file with a new name"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save ICTL File", "", "ICTL Files (*.ictl);;All Files (*)"
        )
        
        if file_path:
            self.current_file = file_path
            self.save_file()
    
    def show_about(self):
        """Show about dialog"""
        QMessageBox.information(
            self, "About ICTL Modern Interpreter",
            "ICTL v26.05.01\n\n"
            "A beginner-friendly programming language designed to make "
            "the learning journey easy and enjoyable.\n\n"
            "Built with PySide6 (Qt6)\n"
            "© 2026 IndianCoder3"
        )


def main():
    app = QApplication(sys.argv)
    interpreter = ICTLGuiInterpreter()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
