# ICTL VS Code Extension Build Instructions

## Prerequisites

1. Install Node.js (https://nodejs.org/)
2. Install VS Code Extension Manager:
   ```
   npm install -g @vscode/vsce
   ```

## Building the Extension

1. Open a terminal in the `ictl_extras-vscode` folder
2. Run the build script:
   ```bash
   ./build.bat
   ```
   Or manually:
   ```bash
   vsce package
   ```

3. This will create a `.vsix` file that can be installed in VS Code

## Manual Installation

1. In VS Code, open the Command Palette (`Ctrl+Shift+P`)
2. Run `Extensions: Install from VSIX...`
3. Select the generated `.vsix` file

## Files Created

- `package.json` - Extension manifest
- `language-configuration.json` - Language configuration
- `syntaxes/ictl.tmLanguage.json` - TextMate grammar for syntax highlighting
- `snippets/ictl.json` - Code snippets
- `README.md` - Documentation
- `example.ictl` - Test file
- `build.bat` - Build script
- `.vscodeignore` - Files to exclude from packaging