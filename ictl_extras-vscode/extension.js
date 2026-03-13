const vscode = require('vscode');

function activate(context) {

    const provider = vscode.languages.registerCompletionItemProvider(
        'ictl',
        {
            provideCompletionItems(document, position) {

                const line = document.lineAt(position).text.substring(0, position.character);

                const items = [];

                if (line.endsWith("Terminal.")) {

                    ["Echo","Ask","Style"].forEach(cmd=>{
                        items.push(new vscode.CompletionItem(cmd,vscode.CompletionItemKind.Method));
                    });

                }

                else if (line.endsWith("Math.")) {

                    ["Eval","Compare","Random"].forEach(cmd=>{
                        items.push(new vscode.CompletionItem(cmd,vscode.CompletionItemKind.Method));
                    });

                }

                else if (line.endsWith("Program.")) {

                    [
                        "Main",
                        "If",
                        "Else",
                        "Not",
                        "Loop",
                        "ForeverLoop",
                        "BreakLoop",
                        "Continue"
                    ].forEach(cmd=>{
                        items.push(new vscode.CompletionItem(cmd,vscode.CompletionItemKind.Method));
                    });

                }

                else if (line.endsWith("Variables.")) {

                    items.push(new vscode.CompletionItem("New",vscode.CompletionItemKind.Method));

                }

                else if (line.endsWith("Data.")) {

                    items.push(new vscode.CompletionItem("Compare",vscode.CompletionItemKind.Method));

                }

                else if (line.endsWith("Time.")) {

                    ["Current","Wait"].forEach(cmd=>{
                        items.push(new vscode.CompletionItem(cmd,vscode.CompletionItemKind.Method));
                    });

                }

                else {

                    [
                        "Terminal",
                        "Math",
                        "Program",
                        "Variables",
                        "Data",
                        "Time",
                        "True",
                        "False"
                    ].forEach(cmd=>{
                        items.push(new vscode.CompletionItem(cmd,vscode.CompletionItemKind.Keyword));
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
        'D'
    );

    context.subscriptions.push(provider);
}

function deactivate(){}

module.exports = {
    activate,
    deactivate
};