# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/GUIHandler.py
from ictl_builtins.gui import (
    gui_message_box, gui_dialog_box, gui_input_box, gui_choice_box,
    gui_new_window, gui_button, gui_label, gui_image, gui_show_window,
    gui_spacing, gui_separator, gui_set_theme, gui_text_field, gui_get_text_field,
    gui_color_picker, gui_color_palette, gui_date_picker, gui_color_map,
    gui_info_dialog, gui_warning_dialog, gui_error_dialog, gui_confirm_dialog,
    gui_file_open_dialog, gui_file_save_dialog, gui_folder_dialog, 
    gui_input_dialog, gui_multi_choice_dialog, gui_number_dialog, gui_ok_cancel_dialog
)
from error_handler import RuntimeErrorICTL

def handle_gui(command, args, eval_expr):
    """
    Route GUI commands to appropriate functions.
    
    Example:
        GUI.MessageBox("Title", "Message")
        GUI.InfoDialog("Title", "Info message")
        GUI.WarningDialog("Warning!", "Something might be wrong")
        GUI.ErrorDialog("Error", "Something went wrong")
        GUI.ConfirmDialog("Are you sure?", "Continue?")
        GUI.FileOpenDialog("Open")
        GUI.FileSaveDialog("Save")
        GUI.FolderDialog("Select folder")
        GUI.InputDialog("Name", "Enter your name")
    """
    command_lower = command.lower()
    
    commands = {
        "messagebox": gui_message_box,
        "newdialogbox": gui_dialog_box,
        "inputbox": gui_input_box,
        "choicebox": gui_choice_box,
        "window": gui_new_window,
        "button": gui_button,
        "label": gui_label,
        "image": gui_image,
        "showwindow": gui_show_window,
        "spacing": gui_spacing,
        "separator": gui_separator,
        "settheme": gui_set_theme,
        "textfield": gui_text_field,
        "gettextfield": gui_get_text_field,
        "colorpicker": gui_color_picker,
        "colorpalette": gui_color_palette,
        "datepicker": gui_date_picker,
        "colormap": gui_color_map,
        "infodialog": gui_info_dialog,
        "warningdialog": gui_warning_dialog,
        "errordialog": gui_error_dialog,
        "confirmdialog": gui_confirm_dialog,
        "fileopendialog": gui_file_open_dialog,
        "filesavedialog": gui_file_save_dialog,
        "folderdialog": gui_folder_dialog,
        "inputdialog": gui_input_dialog,
        "multichoicedialog": gui_multi_choice_dialog,
        "numberdialog": gui_number_dialog,
        "okcanceldialog": gui_ok_cancel_dialog,
    }
    
    if command_lower not in commands:
        available = ", ".join(sorted(commands.keys()))
        raise RuntimeErrorICTL(f"Unknown GUI command: {command}\nAvailable: {available}")
    
    # Evaluate arguments
    evaluated_args = [eval_expr(arg) for arg in args]
    
    # Call the appropriate function
    return commands[command_lower](*evaluated_args)
