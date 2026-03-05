
echo Building ICTL Language Support Extension...

REM Check if vsce is installed
vsce --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing vsce...
    npm install -g @vscode/vsce
)

REM Package the extension
vsce package

echo Extension packaged successfully!
echo Install the .vsix file using VS Code's "Install from VSIX" command.