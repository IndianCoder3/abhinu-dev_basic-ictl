# ICTL Modern GUI Interpreter

A sleek, modern GUI-based interpreter for ICTL language built with **PySide6** (Qt6).

## Features

✨ **Modern Dark Theme** - Professional dark UI inspired by VS Code  
📝 **Advanced Code Editor** - Syntax highlighting for ICTL, line numbers  
🖥️ **Live Output Console** - Color-coded output (info, success, error, warning)  
🎯 **File Management** - Open, save, and manage ICTL files  
⚡ **Fast Execution** - Run code with a single click  
🎨 **Modern Aesthetics** - Uses Fira Code font and smooth animations  

## Requirements

- Python 3.8+
- PySide6 6.7.0+
- Pygments 2.17.2+

## Installation

1. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

Run the interpreter:
```bash
python main.py
```

## Project Structure

```
ictl_gui_modern/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── ui/                     # UI components
│   ├── __init__.py
│   ├── code_editor.py      # Code editor with syntax highlighting
│   ├── output_console.py   # Output display console
│   └── sidebar.py          # Sidebar file explorer
├── interpreter/            # Code execution engine
│   ├── __init__.py
│   └── executor.py         # ICTL code executor
└── README.md              # This file
```

## Components

### Code Editor
- Syntax highlighting for ICTL keywords
- Line numbers
- Fira Code font for better readability
- Tab support (4 spaces)

### Output Console
- Color-coded output types:
  - **Success**: Green
  - **Error**: Red
  - **Warning**: Yellow
  - **Info**: Light Blue

### Sidebar
- File explorer
- Quick file operations
- Settings and search

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+N` | New file |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+R` | Run code |
| `Ctrl+K` | Clear output |

## Theme

The interpreter uses a modern dark theme with:
- Background: `#1e1e1e`
- Foreground: `#d4d4d4`
- Accent: `#007acc`
- Syntax colors inspired by VS Code Dark+ theme

## Future Enhancements

- [ ] Debugger with breakpoints
- [ ] Real-time error checking
- [ ] Code autocomplete
- [ ] Multiple file tabs
- [ ] Theme customization
- [ ] Plugin system
- [ ] Project templates
- [ ] Integrated terminal

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please create an issue in the project repository.
