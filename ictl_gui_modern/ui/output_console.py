"""
Output Console for ICTL GUI Interpreter
"""

from PySide6.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QTextCursor


class OutputConsole(QWidget):
    """Modern output console"""
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Console header
        header = QHBoxLayout()
        title = QLabel("Output Console")
        title.setStyleSheet("""
            QLabel {
                color: #d4d4d4;
                font-weight: bold;
                padding: 8px;
                background-color: #2b2b2b;
                border-bottom: 1px solid #3d3d3d;
            }
        """)
        header.addWidget(title)
        header.addStretch()
        
        layout.addLayout(header)
        
        # Text display
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        
        font = QFont("Courier New", 10)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.text_edit.setFont(font)
        
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: none;
                padding: 10px;
            }
        """)
        
        layout.addWidget(self.text_edit)
    
    def append_output(self, text, output_type="normal"):
        """Append text to console with formatting"""
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.text_edit.setTextCursor(cursor)
        
        # Set color based on output type
        if output_type == "error":
            color = QColor("#f48771")  # Red
        elif output_type == "success":
            color = QColor("#4ec9b0")  # Green
        elif output_type == "warning":
            color = QColor("#dcdcaa")  # Yellow
        elif output_type == "info":
            color = QColor("#9cdcfe")  # Light Blue
        else:
            color = QColor("#d4d4d4")  # Default
        
        # Insert text with color
        fmt = self.text_edit.currentCharFormat()
        fmt.setForeground(color)
        self.text_edit.setCurrentCharFormat(fmt)
        self.text_edit.insertPlainText(text)
        
        # Reset format
        fmt.setForeground(QColor("#d4d4d4"))
        self.text_edit.setCurrentCharFormat(fmt)
    
    def clear(self):
        """Clear the console"""
        self.text_edit.clear()
    
    def set_text(self, text):
        """Set console text"""
        self.text_edit.setPlainText(text)
