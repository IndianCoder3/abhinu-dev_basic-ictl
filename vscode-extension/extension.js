const vscode = require('vscode');
const path = require('path');
const { spawn } = require('child_process');

// Command documentation for IntelliSense
const commandDocs = {
    // Terminal Commands
    'Terminal.Echo': 'Print a value to the terminal output',
    'Terminal.Ask': 'Ask user for input and return the response as a string',
    'Terminal.Clear': 'Clear the terminal screen',
    'Terminal.Style': 'Set the terminal text color/style (red, green, blue, yellow, cyan, magenta, bold, reset)',
    
    // Variables
    'Variables.New': 'Create a new variable (deprecated - use direct assignment)',
    
    // Math Commands
    'Math.Eval': 'Evaluate a mathematical expression',
    'Math.Compare': 'Compare two numeric values using a comparison operator',
    'Math.Random': 'Generate a random integer between min and max (inclusive)',
    'Math.SymPy': 'Evaluate expression using SymPy symbolic math library',
    'Math.NumPy': 'Evaluate expression using NumPy numerical library',
    
    // Program Commands
    'Program.Main': 'Main program entry point',
    'Program.If': 'Conditional if statement',
    'Program.Else': 'Else clause following an if statement',
    'Program.Loop': 'Counted loop - executes block N times',
    'Program.ForeverLoop': 'Infinite loop',
    'Program.BreakLoop': 'Break out of a loop',
    'Program.Continue': 'Skip to next iteration of loop',
    
    // Lists Commands
    'Lists.Create': 'Create a new list',
    'Lists.Get': 'Get an item from a list by index (0-based)',
    'Lists.Push': 'Add an item to the end of a list',
    'Lists.Pop': 'Remove and return the last item from a list',
    'Lists.Length': 'Get the number of items in a list',
    'Lists.Clear': 'Remove all items from a list',
    'Lists.Delete': 'Delete an entire list',
    'Lists.Contains': 'Check if a list contains a specific item',
    'Lists.Set': 'Set list contents directly',
    
    // Data Commands
    'Data.Compare': 'Compare two values for strict equality (type matters)',
    'Data.LooseCompare': 'Compare two values for equality (type-insensitive)',
    'Data.ToInt': 'Convert a value to an integer',
    'Data.ToFloat': 'Convert a value to a floating-point number',
    'Data.ToString': 'Convert a value to a string',
    'Data.TypeOf': 'Get the data type of a value as a string',
    
    // Time Commands
    'Time.Current': 'Get the current date/time in specified format',
    'Time.Wait': 'Pause execution for specified number of seconds',
    
    // Kachua Commands
    'Kachua.Forward': 'Move turtle forward by specified distance',
    'Kachua.Backward': 'Move turtle backward by specified distance',
    'Kachua.Right': 'Turn turtle right by specified angle',
    'Kachua.Left': 'Turn turtle left by specified angle',
    'Kachua.PenUp': 'Lift the pen (don\'t draw)',
    'Kachua.PenDown': 'Put the pen down (start drawing)',
    'Kachua.SetColor': 'Set the pen color',
    'Kachua.SetPenWidth': 'Set the pen line width/thickness',
    'Kachua.SetSpeed': 'Set drawing speed (0=fastest, higher=slower)',
    'Kachua.GoTo': 'Move turtle to absolute position',
    'Kachua.Home': 'Move turtle back to home position (0, 0)',
    'Kachua.Clear': 'Clear all drawings from the screen',
    'Kachua.Reset': 'Reset turtle to default state',
    'Kachua.Show': 'Display the graphics window',
    'Kachua.Hide': 'Hide the turtle cursor',
    'Kachua.Stamp': 'Stamp a copy of the turtle at current position',
    'Kachua.FillStart': 'Begin a fill region',
    'Kachua.FillEnd': 'End and fill the current region',
    'Kachua.Circle': 'Draw a circle with given radius',
    'Kachua.Heading': 'Get current heading direction',
    'Kachua.SetHeading': 'Set heading direction',
    
    // GUI Commands
    'GUI.MessageBox': 'Display a simple message box',
    'GUI.NewDialogBox': 'Display a dialog box',
    'GUI.InputBox': 'Get user text input in a dialog',
    'GUI.ChoiceBox': 'Display dialog with multiple choice options',
    'GUI.Window': 'Create a new GUI window',
    'GUI.Button': 'Add a button to the window',
    'GUI.Label': 'Add a text label to the window',
    'GUI.Image': 'Display an image in the window',
    'GUI.ShowWindow': 'Display the GUI window and run event loop',
    'GUI.Spacing': 'Add vertical spacing to the window',
    'GUI.Separator': 'Add a visual separator line',
    'GUI.SetTheme': 'Set application theme (Dark or Light)',
};

function createCompletionItem(label, kind, doc, insertText) {
    const item = new vscode.CompletionItem(label, kind);
    item.documentation = new vscode.MarkdownString(commandDocs[label] || doc || '');
    if (insertText) {
        item.insertText = insertText;
    }
    return item;
}

function activate(context) {
    // Register completion provider with IntelliSense
    const provider = vscode.languages.registerCompletionItemProvider(
        'ictl',
        {
            provideCompletionItems(document, position) {
                const line = document.lineAt(position).text.substring(0, position.character);
                const items = [];

                if (line.endsWith("Terminal.")) {
                    ["Echo", "Ask", "Style", "Clear"].forEach(cmd => {
                        items.push(createCompletionItem(`Terminal.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Math.")) {
                    ["Eval", "Compare", "Random", "SymPy", "NumPy"].forEach(cmd => {
                        items.push(createCompletionItem(`Math.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Program.")) {
                    [
                        "Main",
                        "If",
                        "Else",
                        "Loop",
                        "ForeverLoop",
                        "BreakLoop",
                        "Continue"
                    ].forEach(cmd => {
                        items.push(createCompletionItem(`Program.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Variables.")) {
                    items.push(createCompletionItem('Variables.New', vscode.CompletionItemKind.Method, '', 'New'));
                }
                else if (line.endsWith("Lists.")) {
                    [
                        "Get",
                        "Create",
                        "Push",
                        "Pop",
                        "Clear",
                        "Delete",
                        "Length",
                        "Contains",
                        "Set"
                    ].forEach(cmd => {
                        items.push(createCompletionItem(`Lists.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Data.")) {
                    ["Compare", "LooseCompare", "ToInt", "ToFloat", "ToString", "TypeOf"].forEach(cmd => {
                        items.push(createCompletionItem(`Data.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Time.")) {
                    ["Current", "Wait"].forEach(cmd => {
                        items.push(createCompletionItem(`Time.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("Kachua.")) {
                    [
                        "Forward",
                        "Backward",
                        "Right",
                        "Left",
                        "PenUp",
                        "PenDown",
                        "SetColor",
                        "SetPenWidth",
                        "SetSpeed",
                        "GoTo",
                        "Home",
                        "Clear",
                        "Reset",
                        "Circle",
                        "Stamp",
                        "FillStart",
                        "FillEnd",
                        "Show",
                        "Hide",
                        "SetHeading",
                        "Heading"
                    ].forEach(cmd => {
                        items.push(createCompletionItem(`Kachua.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else if (line.endsWith("GUI.")) {
                    [
                        "MessageBox",
                        "NewDialogBox",
                        "InputBox",
                        "ChoiceBox",
                        "Window",
                        "Button",
                        "Label",
                        "Image",
                        "ShowWindow",
                        "Spacing",
                        "Separator",
                        "SetTheme"
                    ].forEach(cmd => {
                        items.push(createCompletionItem(`GUI.${cmd}`, vscode.CompletionItemKind.Method, '', cmd));
                    });
                }
                else {
                    [
                        "Terminal",
                        "Math",
                        "Program",
                        "Variables",
                        "Lists",
                        "Data",
                        "Time",
                        "Kachua",
                        "GUI",
                        "True",
                        "False"
                    ].forEach(cmd => {
                        items.push(createCompletionItem(cmd, vscode.CompletionItemKind.Keyword));
                    });
                }

                return items;
            }
        },
        '.',
        'T',
        'M',
        'P',
        'V',
        'D',
        'L',
        'K',
        'G'
    );

    // Register hover provider for IntelliSense documentation
    const hoverProvider = vscode.languages.registerHoverProvider('ictl', {
        provideHover(document, position) {
            const range = document.getWordRangeAtPosition(position, /[\w.]+/);
            if (!range) return null;
            
            const word = document.getText(range);
            const doc = commandDocs[word];
            
            if (doc) {
                return new vscode.Hover(new vscode.MarkdownString(doc));
            }
            return null;
        }
    });

    // Register run command (F5)
    const runCommand = vscode.commands.registerCommand('ictl.run', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor');
            return;
        }

        if (editor.document.languageId !== 'ictl') {
            vscode.window.showErrorMessage('Active file is not an ICTL file');
            return;
        }

        // Get ICTL installation directory from settings
        let iclPath = vscode.workspace.getConfiguration('ictl').get('installationPath');

        if (!iclPath) {
            // Ask user for ICTL installation path
            const selection = await vscode.window.showOpenDialog({
                canSelectFiles: false,
                canSelectFolders: true,
                canSelectMany: false,
                title: 'Select ICTL Installation Directory',
                openLabel: 'Select'
            });

            if (!selection || selection.length === 0) {
                vscode.window.showErrorMessage('No ICTL installation directory selected');
                return;
            }

            iclPath = selection[0].fsPath;

            // Save to settings
            await vscode.workspace.getConfiguration('ictl').update('installationPath', iclPath, vscode.ConfigurationTarget.Global);
            vscode.window.showInformationMessage(`ICTL installation path saved: ${iclPath}`);
        }

        // Save current file if modified
        if (editor.document.isDirty) {
            await editor.document.save();
        }

        const filePath = editor.document.fileName;
        const fileName = path.basename(filePath);

        // Create output terminal
        let terminal = vscode.window.terminals.find(t => t.name === 'ICTL');
        if (!terminal) {
            terminal = vscode.window.createTerminal('ICTL');
        }
        terminal.show(true);

        // Run ICTL file
        const executablePath = path.join(iclPath, process.platform === 'win32' ? 'ictl.exe' : 'ictl');
        terminal.sendText(`"${executablePath}" "${filePath}"`);
    });

    // Register configure ICTL path command
    const configCommand = vscode.commands.registerCommand('ictl.configurePath', async () => {
        const selection = await vscode.window.showOpenDialog({
            canSelectFiles: false,
            canSelectFolders: true,
            canSelectMany: false,
            title: 'Select ICTL Installation Directory',
            openLabel: 'Select'
        });

        if (!selection || selection.length === 0) {
            return;
        }

        const iclPath = selection[0].fsPath;
        await vscode.workspace.getConfiguration('ictl').update('installationPath', iclPath, vscode.ConfigurationTarget.Global);
        vscode.window.showInformationMessage(`ICTL path configured: ${iclPath}`);
    });

    context.subscriptions.push(provider, hoverProvider, runCommand, configCommand);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};