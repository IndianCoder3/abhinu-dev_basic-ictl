"""
Sidebar for ICTL GUI Interpreter - VS Code style
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QListWidget, QListWidgetItem, QScrollArea, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont, QColor


class SideBar(QWidget):
    """Modern VS Code-style sidebar"""
    
    new_file_clicked = Signal()
    open_file_clicked = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.parent_window = parent
        self.setFixedWidth(280)
        self.setStyleSheet("""
            QWidget {
                background-color: #252526;
                border-right: 1px solid #3d3d3d;
            }
            QLabel {
                color: #d4d4d4;
            }
            QPushButton {
                background-color: transparent;
                color: #d4d4d4;
                border: none;
                text-align: left;
                padding: 8px 10px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #2b2b2b;
            }
            QPushButton:pressed {
                background-color: #3d3d3d;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QLabel("📁 ICTL EXPLORER")
        header.setStyleSheet("""
            QLabel {
                color: #d4d4d4;
                font-weight: bold;
                font-size: 12px;
                padding: 12px;
                background-color: #2b2b2b;
                border-bottom: 1px solid #3d3d3d;
                text-transform: uppercase;
            }
        """)
        layout.addWidget(header)
        
        # Tab buttons
        tab_widget = QWidget()
        tab_layout = QHBoxLayout(tab_widget)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.setSpacing(0)
        
        self.explorer_btn = QPushButton("🔍 EXPLORER")
        self.explorer_btn.setMinimumHeight(36)
        self.explorer_btn.setStyleSheet("""
            QPushButton {
                background-color: #2b2b2b;
                color: #d4d4d4;
                border: none;
                border-bottom: 2px solid #007acc;
                padding: 8px;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #3d3d3d;
            }
        """)
        tab_layout.addWidget(self.explorer_btn, 1)
        
        layout.addWidget(tab_widget)
        
        # File explorer content
        self.file_list = QListWidget()
        self.file_list.setStyleSheet("""
            QListWidget {
                background-color: #252526;
                border: none;
                outline: none;
            }
            QListWidget::item {
                padding: 6px 8px;
                border-bottom: none;
            }
            QListWidget::item:hover {
                background-color: #2d2d30;
            }
            QListWidget::item:selected {
                background-color: #094771;
                color: white;
            }
        """)
        self.file_list.itemDoubleClicked.connect(self._on_file_double_clicked)
        
        layout.addWidget(QLabel("OPEN EDITORS"), alignment=Qt.AlignTop)
        layout.addWidget(self.file_list)
        
        # Spacing
        layout.addStretch()
        
        # Quick actions section
        actions_label = QLabel("QUICK ACTIONS")
        actions_label.setStyleSheet("""
            QLabel {
                color: #858585;
                font-size: 11px;
                font-weight: bold;
                padding: 12px 10px 8px 10px;
                background-color: #2b2b2b;
                border-top: 1px solid #3d3d3d;
                margin-top: 10px;
            }
        """)
        layout.addWidget(actions_label)
        
        # Action buttons
        self.new_file_btn = QPushButton("+ New File")
        self.new_file_btn.clicked.connect(self._on_new_file)
        layout.addWidget(self.new_file_btn)
        
        self.open_file_btn = QPushButton("📂 Open File")
        self.open_file_btn.clicked.connect(self._on_open_file)
        layout.addWidget(self.open_file_btn)
        
        self.open_folder_btn = QPushButton("📁 Open Folder")
        self.open_folder_btn.clicked.connect(self._on_open_folder)
        layout.addWidget(self.open_folder_btn)
    
    def _on_new_file(self):
        """Handle new file button"""
        if self.parent_window:
            self.parent_window.new_file()
    
    def _on_open_file(self):
        """Handle open file button"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open ICTL File", "", "ICTL Files (*.ictl);;All Files (*)"
        )
        if file_path:
            self.open_file_clicked.emit(file_path)
            if self.parent_window:
                self.parent_window.open_file_direct(file_path)
                self._add_to_list(file_path)
    
    def _on_open_folder(self):
        """Handle open folder button"""
        folder = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder:
            # Could implement folder browsing here
            pass
    
    def _on_file_double_clicked(self, item):
        """Handle file double-click"""
        file_path = item.data(Qt.UserRole)
        if file_path and self.parent_window:
            self.parent_window.open_file_direct(file_path)
    
    def _add_to_list(self, file_path):
        """Add file to open editors list"""
        item = QListWidgetItem(f"📄 {Path(file_path).name}")
        item.setData(Qt.UserRole, file_path)
        item.setFont(QFont("Segoe UI", 10))
        self.file_list.addItem(item)
    
    def add_file(self, file_path):
        """Add a file to the explorer"""
        self._add_to_list(file_path)


# Import Path at module level
from pathlib import Path
