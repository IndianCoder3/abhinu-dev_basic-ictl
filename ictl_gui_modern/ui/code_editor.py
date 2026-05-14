"""
Modern Code Editor with Syntax Highlighting for ICTL
"""

from PySide6.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor, QTextCharFormat, QSyntaxHighlighter, QTextDocument
import re


class ICTLSyntaxHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for ICTL code"""
    
    def __init__(self, document):
        super().__init__(document)
        
        # Define color scheme
        self.colors = {
            'keyword': QColor("#569cd6"),      # Blue
            'string': QColor("#ce9178"),       # Orange
            'number': QColor("#b5cea8"),       # Green
            'comment': QColor("#6a9955"),      # Dim Green
            'function': QColor("#dcdcaa"),     # Yellow
            'variable': QColor("#9cdcfe"),     # Light Blue
            'operator': QColor("#d4d4d4"),     # Gray
            'builtin': QColor("#c586c0"),      # Purple
        }
        
        # ICTL Keywords
        self.keywords = [
            'if', 'else', 'elif', 'for', 'while', 'def', 'return',
            'class', 'import', 'from', 'as', 'try', 'except', 'finally',
            'with', 'lambda', 'True', 'False', 'None', 'and', 'or', 'not',
            'in', 'is', 'break', 'continue', 'pass', 'yield', 'async', 'await'
        ]
        
        # ICTL Built-in functions
        self.builtins = [
            'print', 'input', 'len', 'range', 'str', 'int', 'float',
            'list', 'dict', 'set', 'tuple', 'type', 'isinstance', 'callable'
        ]
        
        # Compile patterns
        self.keyword_pattern = QTextCharFormat()
        self.keyword_pattern.setForeground(self.colors['keyword'])
        keyword_font = QFont()
        keyword_font.setBold(True)
        self.keyword_pattern.setFont(keyword_font)
        
        self.string_pattern = QTextCharFormat()
        self.string_pattern.setForeground(self.colors['string'])
        
        self.comment_pattern = QTextCharFormat()
        self.comment_pattern.setForeground(self.colors['comment'])
        self.comment_pattern.setFontItalic(True)
        
        self.number_pattern = QTextCharFormat()
        self.number_pattern.setForeground(self.colors['number'])
        
        self.builtin_pattern = QTextCharFormat()
        self.builtin_pattern.setForeground(self.colors['builtin'])
        
    def highlightBlock(self, text):
        """Highlight a block of code"""
        
        # Highlight comments
        comment_index = text.find('#')
        if comment_index >= 0:
            self.setFormat(comment_index, len(text) - comment_index, self.comment_pattern)
            text = text[:comment_index]
        
        # Highlight strings
        for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', text):
            self.setFormat(match.start(), match.end() - match.start(), self.string_pattern)
        
        # Highlight numbers
        for match in re.finditer(r'\b\d+\.?\d*\b', text):
            self.setFormat(match.start(), match.end() - match.start(), self.number_pattern)
        
        # Highlight keywords
        for keyword in self.keywords:
            pattern = r'\b' + keyword + r'\b'
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), self.keyword_pattern)
        
        # Highlight built-in functions
        for builtin in self.builtins:
            pattern = r'\b' + builtin + r'\b'
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), self.builtin_pattern)

class CodeEditor(QTextEdit):
    """Modern code editor with syntax highlighting"""
    
    def __init__(self):
        super().__init__()
        
        # Setup font
        font = QFont("Courier New", 11)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.setFont(font)
        
        # Setup syntax highlighter
        self.highlighter = ICTLSyntaxHighlighter(self.document())
        
        # Setup colors
        self.setStyleSheet("""
            QTextEdit {
                background-color: #252526;
                color: #d4d4d4;
                border: none;
                margin: 0px;
                padding: 10px;
            }
        """)
        
        # Tab size
        self.setTabStopDistance(40)
