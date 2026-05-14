# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# ictl_builtins/gui.py
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QLabel, QMessageBox, QInputDialog, 
                             QFileDialog, QComboBox)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from urllib.request import urlopen
from io import BytesIO
from error_handler import RuntimeErrorICTL
import os

# Global application and window
_app = None
_current_window = None
_window_callbacks = {}

def _get_app():
    """Get or create QApplication instance."""
    global _app
    if _app is None:
        if QApplication.instance() is None:
            _app = QApplication(sys.argv)
        else:
            _app = QApplication.instance()
    return _app

def gui_message_box(title, message):
    """Display a simple message box."""
    try:
        app = _get_app()
        QMessageBox.information(None, str(title), str(message))
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.MessageBox error: {e}")

def gui_dialog_box(title, message):
    """Display a dialog box (Windows-style)."""
    try:
        app = _get_app()
        QMessageBox.question(None, str(title), str(message), QMessageBox.Ok)
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.NewDialogBox error: {e}")

def gui_input_box(prompt, title="Input"):
    """Show input dialog and get user text."""
    try:
        app = _get_app()
        text, ok = QInputDialog.getText(None, str(title), str(prompt))
        if ok:
            return text
        return ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.InputBox error: {e}")

def gui_choice_box(title, message, *options):
    """Show dialog with multiple choice options."""
    try:
        app = _get_app()
        if not options:
            raise RuntimeErrorICTL("GUI.ChoiceBox requires at least one option")
        
        choice, ok = QInputDialog.getItem(None, str(title), str(message), 
                                         [str(opt) for opt in options], 0, False)
        if ok:
            return choice
        return ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ChoiceBox error: {e}")

def gui_new_window(title="Window", width=600, height=400):
    """Create a new GUI window."""
    try:
        global _current_window, _window_callbacks
        app = _get_app()
        
        _current_window = QMainWindow()
        _current_window.setWindowTitle(str(title))
        _current_window.setGeometry(100, 100, int(width), int(height))
        
        # Central widget with layout
        central = QWidget()
        _current_window.setCentralWidget(central)
        
        layout = QVBoxLayout()
        central.setLayout(layout)
        
        # Store layout reference for adding widgets
        _current_window.layout_ref = layout
        
        _window_callbacks = {}
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Window error: {e}")

def gui_button(label, kheer_name):
    """Add a button to the window."""
    try:
        global _current_window, _window_callbacks
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        button = QPushButton(str(label))
        
        # Store callback reference
        callback_id = f"btn_{len(_window_callbacks)}"
        _window_callbacks[callback_id] = str(kheer_name)
        
        # Create closure to capture kheer_name
        def make_callback(kheer):
            def on_click():
                from runtime import _kheers, run_item
                if kheer not in _kheers:
                    QMessageBox.warning(None, "Error", f"Kheer '{kheer}' not defined")
                else:
                    try:
                        for item in _kheers[kheer]:
                            run_item(item)
                    except Exception as e:
                        QMessageBox.critical(None, "Error", f"Kheer error: {str(e)}")
            return on_click
        
        button.clicked.connect(make_callback(str(kheer_name)))
        _current_window.layout_ref.addWidget(button)
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Button error: {e}")

def gui_label(text):
    """Add a text label to the window."""
    try:
        global _current_window
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        label = QLabel(str(text))
        label.setFont(QFont("Arial", 11))
        _current_window.layout_ref.addWidget(label)
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Label error: {e}")

def gui_image(url_or_path):
    """Display an image in the window."""
    try:
        global _current_window
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        pixmap = None
        url_or_path = str(url_or_path)
        
        # Check if it's a URL
        if url_or_path.startswith(("http://", "https://")):
            try:
                response = urlopen(url_or_path)
                image_data = BytesIO(response.read())
                pixmap = QPixmap()
                pixmap.loadFromData(image_data.getvalue())
            except Exception as e:
                raise RuntimeErrorICTL(f"Failed to load image from URL: {e}")
        else:
            # Local file path
            if not os.path.exists(url_or_path):
                raise RuntimeErrorICTL(f"Image file not found: {url_or_path}")
            pixmap = QPixmap(url_or_path)
        
        if pixmap.isNull():
            raise RuntimeErrorICTL(f"Failed to load image: {url_or_path}")
        
        # Scale to reasonable size
        scaled = pixmap.scaledToWidth(300, Qt.SmoothTransformation)
        
        image_label = QLabel()
        image_label.setPixmap(scaled)
        _current_window.layout_ref.addWidget(image_label)
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Image error: {e}")

def gui_show_window():
    """Display the GUI window and run event loop."""
    try:
        global _current_window, _app
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created")
        
        _current_window.show()
        app = _get_app()
        app.exec_()
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ShowWindow error: {e}")

def gui_spacing(height=10):
    """Add vertical spacing to window."""
    try:
        global _current_window
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        label = QLabel()
        label.setFixedHeight(int(height))
        _current_window.layout_ref.addWidget(label)
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Spacing error: {e}")

def gui_separator():
    """Add a visual separator line to window."""
    try:
        global _current_window
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        line = QLabel()
        line.setText("―" * 50)
        line.setStyleSheet("color: gray;")
        _current_window.layout_ref.addWidget(line)
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.Separator error: {e}")

def gui_set_theme(theme):
    """Set application theme (Dark or Light)."""
    try:
        global _current_window, _app
        app = _get_app()
        theme = str(theme).lower()
        
        if theme == "dark":
            # Dark theme stylesheet
            dark_style = """
                QMainWindow { background-color: #2b2b2b; color: #ffffff; }
                QPushButton { background-color: #0d47a1; color: white; border: none; padding: 5px; border-radius: 3px; font-weight: bold; }
                QPushButton:hover { background-color: #1565c0; }
                QLabel { color: #ffffff; }
                QLineEdit { background-color: #404040; color: #ffffff; border: 1px solid #555555; padding: 5px; border-radius: 3px; }
                QComboBox { background-color: #404040; color: #ffffff; border: 1px solid #555555; padding: 5px; }
                QCalendarWidget { background-color: #2b2b2b; color: #ffffff; }
                QCalendarWidget QToolButton { color: #ffffff; }
                QCalendarWidget QSpinBox { background-color: #404040; color: #ffffff; }
            """
            app.setStyle('Fusion')
            app.setStyleSheet(dark_style)
        elif theme == "light":
            # Light theme (default)
            light_style = """
                QMainWindow { background-color: #ffffff; color: #000000; }
                QPushButton { background-color: #2196F3; color: white; border: none; padding: 5px; border-radius: 3px; font-weight: bold; }
                QPushButton:hover { background-color: #1976D2; }
                QLabel { color: #000000; }
                QLineEdit { background-color: #f5f5f5; color: #000000; border: 1px solid #cccccc; padding: 5px; border-radius: 3px; }
                QComboBox { background-color: #f5f5f5; color: #000000; border: 1px solid #cccccc; padding: 5px; }
            """
            app.setStyle('Fusion')
            app.setStyleSheet(light_style)
        else:
            raise RuntimeErrorICTL(f"Unknown theme: {theme}. Use 'Dark' or 'Light'")
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.SetTheme error: {e}")

def gui_text_field(placeholder="", label=""):
    """Add a text input field to the window."""
    try:
        from PyQt5.QtWidgets import QLineEdit
        global _current_window
        
        if _current_window is None:
            raise RuntimeErrorICTL("No window created. Call GUI.Window() first")
        
        # Add label if provided
        if label:
            label_widget = QLabel(str(label))
            _current_window.layout_ref.addWidget(label_widget)
        
        # Create text field
        text_field = QLineEdit()
        text_field.setPlaceholderText(str(placeholder))
        _current_window.layout_ref.addWidget(text_field)
        
        # Store reference for retrieval
        if not hasattr(_current_window, 'text_fields'):
            _current_window.text_fields = {}
        field_id = f"field_{len(_current_window.text_fields)}"
        _current_window.text_fields[field_id] = text_field
        
        return field_id
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.TextField error: {e}")

def gui_get_text_field(field_id):
    """Get the text from a text field."""
    try:
        global _current_window
        
        if _current_window is None or not hasattr(_current_window, 'text_fields'):
            raise RuntimeErrorICTL("No text fields in current window")
        
        if field_id not in _current_window.text_fields:
            raise RuntimeErrorICTL(f"Text field not found: {field_id}")
        
        return _current_window.text_fields[field_id].text()
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.GetTextField error: {e}")

def gui_color_picker(label="Select a color"):
    """Show color picker dialog and return selected color."""
    try:
        from PyQt5.QtWidgets import QColorDialog
        app = _get_app()
        
        color = QColorDialog.getColor()
        if color.isValid():
            return color.name()  # Returns hex color like "#FF5733"
        return "#000000"
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ColorPicker error: {e}")

def gui_color_palette(*colors):
    """Show a custom color palette and return selected color."""
    try:
        if not colors:
            colors = ("Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Cyan")
        
        app = _get_app()
        choice, ok = QInputDialog.getItem(None, "Color Palette", "Select a color:", 
                                          [str(c) for c in colors], 0, False)
        if ok:
            return choice
        return colors[0] if colors else "Red"
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ColorPalette error: {e}")

def gui_date_picker(label="Select a date"):
    """Show calendar date picker and return selected date."""
    try:
        from PyQt5.QtWidgets import QCalendarWidget, QDialog, QVBoxLayout, QPushButton, QHBoxLayout
        from PyQt5.QtCore import QDate

        app = _get_app()

        # Create dialog
        dialog = QDialog()
        dialog.setWindowTitle(str(label))
        layout = QVBoxLayout()

        # Create calendar
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        layout.addWidget(calendar)

        # OK/Cancel buttons (horizontal layout)
        button_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)

        # Finalize dialog
        dialog.setLayout(layout)

        # Connect buttons to accept/reject so exec_() returns properly
        ok_btn.clicked.connect(dialog.accept)
        cancel_btn.clicked.connect(dialog.reject)

        # Run dialog and return selected date if accepted
        if dialog.exec_() == QDialog.Accepted:
            selected_date = calendar.selectedDate()
            date_str = selected_date.toString("yyyy-MM-dd")
            return date_str
        return ""

    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.DatePicker error: {e}")

def gui_color_map():
    """Display a map/palette of available colors and return selection."""
    try:
        # Extended color palette
        colors = {
            "Red": "#FF0000",
            "Green": "#00FF00",
            "Blue": "#0000FF",
            "Yellow": "#FFFF00",
            "Purple": "#800080",
            "Cyan": "#00FFFF",
            "Magenta": "#FF00FF",
            "Orange": "#FFA500",
            "Pink": "#FFC0CB",
            "Brown": "#A52A2A",
            "Gray": "#808080",
            "Black": "#000000",
            "White": "#FFFFFF",
            "Lime": "#00FF00",
            "Navy": "#000080",
            "Teal": "#008080",
        }
        
        app = _get_app()
        color_names = list(colors.keys())
        choice, ok = QInputDialog.getItem(None, "Color Map", "Select a color:", 
                                          color_names, 0, False)
        if ok:
            return colors[choice]
        return colors["Black"]
        
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ColorMap error: {e}")

# --- NEW DIALOG FUNCTIONS ---

def gui_info_dialog(title, message):
    """Display an information dialog."""
    try:
        app = _get_app()
        QMessageBox.information(None, str(title), str(message))
        return "OK"
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.InfoDialog error: {e}")

def gui_warning_dialog(title, message):
    """Display a warning dialog."""
    try:
        app = _get_app()
        QMessageBox.warning(None, str(title), str(message))
        return "OK"
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.WarningDialog error: {e}")

def gui_error_dialog(title, message):
    """Display an error dialog."""
    try:
        app = _get_app()
        QMessageBox.critical(None, str(title), str(message))
        return "OK"
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ErrorDialog error: {e}")

def gui_confirm_dialog(title, message):
    """Display confirmation dialog (Yes/No)."""
    try:
        app = _get_app()
        reply = QMessageBox.question(None, str(title), str(message),
                                     QMessageBox.Yes | QMessageBox.No)
        return "Yes" if reply == QMessageBox.Yes else "No"
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.ConfirmDialog error: {e}")

def gui_file_open_dialog(title="Open File", file_filter="All Files (*)"):
    """Display file open dialog."""
    try:
        app = _get_app()
        file_path, _ = QFileDialog.getOpenFileName(None, str(title), "", str(file_filter))
        return file_path if file_path else ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.FileOpenDialog error: {e}")

def gui_file_save_dialog(title="Save File", file_filter="All Files (*)"):
    """Display file save dialog."""
    try:
        app = _get_app()
        file_path, _ = QFileDialog.getSaveFileName(None, str(title), "", str(file_filter))
        return file_path if file_path else ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.FileSaveDialog error: {e}")

def gui_folder_dialog(title="Select Folder"):
    """Display folder/directory selection dialog."""
    try:
        app = _get_app()
        folder_path = QFileDialog.getExistingDirectory(None, str(title), "")
        return folder_path if folder_path else ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.FolderDialog error: {e}")

def gui_input_dialog(title, message, default=""):
    """Display simple text input dialog."""
    try:
        app = _get_app()
        text, ok = QInputDialog.getText(None, str(title), str(message), 
                                        text=str(default))
        return text if ok else ""
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.InputDialog error: {e}")

def gui_multi_choice_dialog(title, message, *choices):
    """Display dialog with multiple choice selection."""
    try:
        app = _get_app()
        if not choices:
            raise RuntimeErrorICTL("MultiChoiceDialog requires at least one choice")
        
        from PyQt5.QtWidgets import QCheckBox, QDialog, QVBoxLayout, QPushButton, QHBoxLayout
        
        dialog = QDialog()
        dialog.setWindowTitle(str(title))
        layout = QVBoxLayout()
        
        label = QLabel(str(message))
        layout.addWidget(label)
        
        checkboxes = []
        for choice in choices:
            checkbox = QCheckBox(str(choice))
            checkboxes.append(checkbox)
            layout.addWidget(checkbox)
        
        button_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
        
        selected = []
        def on_ok():
            for i, cb in enumerate(checkboxes):
                if cb.isChecked():
                    selected.append(str(choices[i]))
            dialog.accept()
        
        ok_btn.clicked.connect(on_ok)
        cancel_btn.clicked.connect(dialog.reject)
        
        dialog.setLayout(layout)
        dialog.exec_()
        
        return selected if selected else []
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.MultiChoiceDialog error: {e}")

def gui_number_dialog(title, message, default_value=0, min_val=0, max_val=100):
    """Display number input dialog."""
    try:
        app = _get_app()
        from PyQt5.QtWidgets import QSpinBox, QDialog, QVBoxLayout, QPushButton, QHBoxLayout
        
        dialog = QDialog()
        dialog.setWindowTitle(str(title))
        layout = QVBoxLayout()
        
        label = QLabel(str(message))
        layout.addWidget(label)
        
        spin_box = QSpinBox()
        spin_box.setMinimum(int(min_val))
        spin_box.setMaximum(int(max_val))
        spin_box.setValue(int(default_value))
        layout.addWidget(spin_box)
        
        button_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
        
        result = [None]
        def on_ok():
            result[0] = spin_box.value()
            dialog.accept()
        
        ok_btn.clicked.connect(on_ok)
        cancel_btn.clicked.connect(dialog.reject)
        
        dialog.setLayout(layout)
        dialog.exec_()
        
        return result[0] if result[0] is not None else int(default_value)
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.NumberDialog error: {e}")

def gui_ok_cancel_dialog(title, message):
    """Display OK/Cancel dialog."""
    try:
        app = _get_app()
        reply = QMessageBox.question(None, str(title), str(message),
                                     QMessageBox.Ok | QMessageBox.Cancel)
        return "OK" if reply == QMessageBox.Ok else "Cancel"
    except Exception as e:
        raise RuntimeErrorICTL(f"GUI.OkCancelDialog error: {e}")
