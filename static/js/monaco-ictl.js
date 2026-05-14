// == Basic ICTL Studio Online ==
// static/js/monaco-ictl.js
// Licensed under MIT License (https://opensource.org/licenses/MIT)
// Source: https://github.com/abhinu-gupt/abhinu-dev_basic-ictl

(function () {
  if (typeof require === 'undefined') return;

  let socket = null;
  let term = null;

  require.config({
    paths: { 'vs': 'https://cdn.jsdelivr.net/npm/monaco-editor@0.36.1/min/vs' }
  });

  require(['vs/editor/editor.main'], function () {
    // 1. Register Language
    monaco.languages.register({ id: 'ictl' });

    // 2. Language Configuration (Auto-brackets & Auto-tab)
    monaco.languages.setLanguageConfiguration('ictl', {
      brackets: [['{', '}'], ['[', ']'], ['(', ')']],
      autoClosingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: '"', close: '"' },
      ],
      surroundingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: '"', close: '"' },
      ],
      onEnterRules: [
        {
          beforeText: new RegExp(`^\\s*.*\\{\\s*$`),
          action: { indentAction: monaco.languages.IndentAction.Indent }
        }
      ]
    });

    // 3. Syntax Highlighting
    monaco.languages.setMonarchTokensProvider('ictl', {
      tokenizer: {
        root: [
          [/\/\/.*/, 'comment'],
          [/"([^"\\]|\\.)*"/, 'string'],
          [/\b\d+(\.\d+)?\b/, 'number'],
          [/\b(Program|Variables|Terminal|Math|Data|Time|Lists|Kachua|GUI)\b/, 'keyword'],
          [/[{}()\[\]]/, '@brackets'],
          [/[A-Za-z_]\w*/, 'identifier']
        ]
      }
    });

    // 4. Smart Hierarchical Autocomplete
    monaco.languages.registerCompletionItemProvider('ictl', {
      triggerCharacters: ['.'],
      provideCompletionItems: (model, position) => {
        const lineContent = model.getLineContent(position.lineNumber).substring(0, position.column - 1);
        
        // --- LEVEL 2: Commands after the dot ---
        if (lineContent.endsWith('Terminal.')) {
          return {
            suggestions: [
              { label: 'Echo', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Echo("${1}")', insertTextRules: 4 },
              { label: 'Ask', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Ask("${1}")', insertTextRules: 4 },
              { label: 'Style', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Style("${1}")', insertTextRules: 4 },
              { label: 'Clear', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Clear' }
            ]
          };
        }
        if (lineContent.endsWith('Program.')) {
          return {
            suggestions: [
              { label: 'Main', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'Main {\n\t$0\n}', insertTextRules: 4 },
              { label: 'If', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'If(${1}) {\n\t$0\n}', insertTextRules: 4 },
              { label: 'Else', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'Else {\n\t$0\n}', insertTextRules: 4 },
              { label: 'Loop', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'Loop(${1}) {\n\t$0\n}', insertTextRules: 4 },
              { label: 'ForeverLoop', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'ForeverLoop {\n\t$0\n}', insertTextRules: 4 },
              { label: 'BreakLoop', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'BreakLoop' },
              { label: 'Continue', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'Continue' },
              { label: 'Not', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Not(${1})', insertTextRules: 4 }
            ]
          };
        }
        if (lineContent.endsWith('Math.')) {
          return {
            suggestions: [
              { label: 'Eval', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Eval(${1})', insertTextRules: 4 },
              { label: 'Compare', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Compare(${1}, "${2:>}", ${3})', insertTextRules: 4 },
              { label: 'Random', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Random(${1:min}, ${2:max})', insertTextRules: 4 }
            ]
          };
        }
        if (lineContent.endsWith('Variables.')) {
          return { 
            suggestions: [
              { label: 'New', kind: monaco.languages.CompletionItemKind.Function, insertText: 'New("${1}")', insertTextRules: 4 },
              { label: 'MyVar', kind: monaco.languages.CompletionItemKind.Variable, insertText: 'MyVar = ${1}', insertTextRules: 4 },
              { label: 'X', kind: monaco.languages.CompletionItemKind.Variable, insertText: 'X = ${1}', insertTextRules: 4 },
              { label: 'Name', kind: monaco.languages.CompletionItemKind.Variable, insertText: 'Name = "${1}"', insertTextRules: 4 }
            ] 
          };
        }
        if (lineContent.endsWith('Lists.')) {
          return {
            suggestions: [
              { label: 'Get', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Get("${1}", ${2:index})', insertTextRules: 4 },
              { label: 'Create', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Create("${1}")', insertTextRules: 4 },
              { label: 'Push', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Push("${1}", ${2:value})', insertTextRules: 4 },
              { label: 'Pop', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Pop("${1}")', insertTextRules: 4 },
              { label: 'Clear', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Clear("${1}")', insertTextRules: 4 }
            ]
          };
        }
        if (lineContent.endsWith('Data.')) {
          return { 
            suggestions: [
              { label: 'Compare', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Compare(${1}, ${2})', insertTextRules: 4 },
              { label: 'ToInt', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ToInt("${1}")', insertTextRules: 4 },
              { label: 'ToFloat', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ToFloat("${1}")', insertTextRules: 4 },
              { label: 'ToString', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ToString(${1})', insertTextRules: 4 }
            ] 
          };
        }
        if (lineContent.endsWith('Kachua.')) {
          return {
            suggestions: [
              { label: 'Forward', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Forward(${1:distance})', insertTextRules: 4 },
              { label: 'Backward', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Backward(${1:distance})', insertTextRules: 4 },
              { label: 'Right', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Right(${1:angle})', insertTextRules: 4 },
              { label: 'Left', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Left(${1:angle})', insertTextRules: 4 },
              { label: 'PenUp', kind: monaco.languages.CompletionItemKind.Function, insertText: 'PenUp' },
              { label: 'PenDown', kind: monaco.languages.CompletionItemKind.Function, insertText: 'PenDown' },
              { label: 'SetColor', kind: monaco.languages.CompletionItemKind.Function, insertText: 'SetColor("${1:color}")', insertTextRules: 4 },
              { label: 'SetPenWidth', kind: monaco.languages.CompletionItemKind.Function, insertText: 'SetPenWidth(${1:width})', insertTextRules: 4 },
              { label: 'SetSpeed', kind: monaco.languages.CompletionItemKind.Function, insertText: 'SetSpeed(${1:speed})', insertTextRules: 4 },
              { label: 'GoTo', kind: monaco.languages.CompletionItemKind.Function, insertText: 'GoTo(${1:x}, ${2:y})', insertTextRules: 4 },
              { label: 'Home', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Home' },
              { label: 'Clear', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Clear' },
              { label: 'Reset', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Reset' },
              { label: 'Circle', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Circle(${1:radius})', insertTextRules: 4 },
              { label: 'Stamp', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Stamp' },
              { label: 'FillStart', kind: monaco.languages.CompletionItemKind.Function, insertText: 'FillStart' },
              { label: 'FillEnd', kind: monaco.languages.CompletionItemKind.Function, insertText: 'FillEnd' },
              { label: 'Show', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Show' },
              { label: 'Hide', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Hide' },
              { label: 'SetHeading', kind: monaco.languages.CompletionItemKind.Function, insertText: 'SetHeading(${1:angle})', insertTextRules: 4 },
              { label: 'Heading', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Heading' }
            ]
          };
        }
        if (lineContent.endsWith('GUI.')) {
          return {
            suggestions: [
              { label: 'MessageBox', kind: monaco.languages.CompletionItemKind.Function, insertText: 'MessageBox("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'NewDialogBox', kind: monaco.languages.CompletionItemKind.Function, insertText: 'NewDialogBox("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'InputBox', kind: monaco.languages.CompletionItemKind.Function, insertText: 'InputBox("${1:prompt}", "${2:title}")', insertTextRules: 4 },
              { label: 'ChoiceBox', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ChoiceBox("${1:title}", "${2:message}", "${3:option1}", "${4:option2}")', insertTextRules: 4 },
              { label: 'Window', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Window("${1:title}", ${2:600}, ${3:400})', insertTextRules: 4 },
              { label: 'Button', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Button("${1:label}", "${2:kheerName}")', insertTextRules: 4 },
              { label: 'Label', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Label("${1:text}")', insertTextRules: 4 },
              { label: 'Image', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Image("${1:url_or_path}")', insertTextRules: 4 },
              { label: 'ShowWindow', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ShowWindow' },
              { label: 'Spacing', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Spacing(${1:height})', insertTextRules: 4 },
              { label: 'Separator', kind: monaco.languages.CompletionItemKind.Function, insertText: 'Separator' },
              { label: 'SetTheme', kind: monaco.languages.CompletionItemKind.Function, insertText: 'SetTheme("${1:Dark|Light}")', insertTextRules: 4 },
              { label: 'TextField', kind: monaco.languages.CompletionItemKind.Function, insertText: 'TextField("${1:placeholder}", "${2:label}")', insertTextRules: 4 },
              { label: 'GetTextField', kind: monaco.languages.CompletionItemKind.Function, insertText: 'GetTextField("${1:field_id}")', insertTextRules: 4 },
              { label: 'ColorPicker', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ColorPicker("${1:label}")', insertTextRules: 4 },
              { label: 'ColorPalette', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ColorPalette(${1})', insertTextRules: 4 },
              { label: 'DatePicker', kind: monaco.languages.CompletionItemKind.Function, insertText: 'DatePicker("${1:label}")', insertTextRules: 4 },
              { label: 'ColorMap', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ColorMap' },
              { label: 'InfoDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'InfoDialog("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'WarningDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'WarningDialog("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'ErrorDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ErrorDialog("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'ConfirmDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'ConfirmDialog("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'OkCancelDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'OkCancelDialog("${1:title}", "${2:message}")', insertTextRules: 4 },
              { label: 'FileOpenDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'FileOpenDialog("${1:Open File}", "${2:All Files (*)}")', insertTextRules: 4 },
              { label: 'FileSaveDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'FileSaveDialog("${1:Save File}", "${2:All Files (*)}")', insertTextRules: 4 },
              { label: 'FolderDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'FolderDialog("${1:Select Folder}")', insertTextRules: 4 },
              { label: 'InputDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'InputDialog("${1:title}", "${2:message}", "${3:default}")', insertTextRules: 4 },
              { label: 'MultiChoiceDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'MultiChoiceDialog("${1:title}", "${2:message}", "${3:opt1}", "${4:opt2}")', insertTextRules: 4 },
              { label: 'NumberDialog', kind: monaco.languages.CompletionItemKind.Function, insertText: 'NumberDialog("${1:title}", "${2:message}", ${3:0}, ${4:100}, ${5:0})', insertTextRules: 4 }
            ]
          };
        }

        // --- LEVEL 1: Main Namespaces ---
        return {
          suggestions: [
            { label: 'Terminal', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Terminal' },
            { label: 'Program', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Program' },
            { label: 'Variables', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Variables' },
            { label: 'Math', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Math' },
            { label: 'Time', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Time' },
            { label: 'Data', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Data' },
            { label: 'Lists', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Lists' },
            { label: 'Kachua', kind: monaco.languages.CompletionItemKind.Class, insertText: 'Kachua' },
            { label: 'GUI', kind: monaco.languages.CompletionItemKind.Class, insertText: 'GUI' }
          ]
        };
      }
    });

    // 5. Initialize Editor
    window.editor = monaco.editor.create(document.getElementById('monaco-container'), {
      value: 'Program.Main {\n\tTerminal.Echo("Hello ICTL")\n}',
      language: 'ictl',
      theme: localStorage.getItem('theme') === 'dark' ? 'vs-dark' : 'vs',
      automaticLayout: true,
      minimap: { enabled: false },
      formatOnType: true
    });


    // Update status bar when cursor moves
    window.editor.onDidChangeCursorPosition((e) => {
      const statusElement = document.getElementById('cursor-pos');
      const line = e.position.lineNumber;
      const col = e.position.column;
      statusElement.innerText = `Ln ${line}, Col ${col}`;
    });

    // Shortcuts for Save, Open, New, Run
    // 1. Setup Ctrl+S for Saving
    window.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, function() {
        saveFile(); // Triggers your existing save function
    });

    // 2. Setup Ctrl+O for Opening
    window.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyO, function() {
        openFile(); // Triggers your existing open function
    });

    // 3. Setup Ctrl+N for New File
    window.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyN, function() {
        window.newFile(); // Triggers your existing new file function
    });

    // 4. Setup F5 for running
    window.editor.addCommand(monaco.KeyCode.F5, function() {
        startExecution();
    });
    
    // Status Bar Config
    // 1. Update Stats (Lines/Chars) whenever text changes
    window.editor.onDidChangeModelContent(() => {
      const model = window.editor.getModel();
      const lineCount = model.getLineCount();
      const charCount = model.getValueLength(); // Gets total characters
      document.getElementById('stats-count').innerText = `Lines: ${lineCount}, Chars: ${charCount}`;
    });

    // 2. Update Cursor Position (Keep your existing listener, just verify ID matches)
    window.editor.onDidChangeCursorPosition((e) => {
      const statusElement = document.getElementById('cursor-pos');
      statusElement.innerText = `Ln ${e.position.lineNumber}, Col ${e.position.column}`;
    });

    // 3. Change Indent Spacing
    window.changeIndent = function() {
      const newSpace = prompt("Enter indent spacing (2 or 4):", "4");
      if (newSpace === "2" || newSpace === "4") {
        window.editor.getModel().updateOptions({ tabSize: parseInt(newSpace) });
        event.target.innerText = `Spaces: ${newSpace}`;
      }
    };

    // 4. Update Tab Size Indicator
    window.editor.getModel().onDidChangeOptions((e) => {
        const tabSize = window.editor.getModel().getOptions().tabSize;
        // Find the element by checking the text content or giving it an ID
        const indentElement = document.querySelector('.status-right .clickable:first-child');
        if (indentElement) {
            indentElement.innerText = `Spaces: ${tabSize}`;
        }
    });
  });

  // Support F5 and Ctrl+S/O/N globally too
  window.addEventListener('keydown', function(e) {
    // Check if the key is F5
    if (e.key === 'F5') {
      // 1. Stop the browser from refreshing
      e.preventDefault();
      
      // 2. Trigger your run function
      if (typeof startExecution === 'function') {
        startExecution();
      }
    }
    
    // Do the same for Ctrl+S globally
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
      e.preventDefault();
      saveFile();
    }
    // Do the same for Ctrl+N globally
    if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
      e.preventDefault();
      newFile();
    }
    // Do the same for Ctrl+O globally
    if ((e.ctrlKey || e.metaKey) && e.key === 'o') {
      e.preventDefault();
      openFile();
    }
  });

  // --- 6. Execution & UI Logic (Same as before) ---
  window.startExecution = function () {
    const code = window.editor.getValue();
    document.getElementById('editor-view').classList.add('hidden');
    document.getElementById('edit-ribbon').classList.add('hidden');
    document.getElementById('execution-view').classList.remove('hidden');
    document.getElementById('exec-ribbon').classList.remove('hidden');

    if (!term) {
      term = new Terminal({ cursorBlink: true, theme: { background: '#000' } });
      term.open(document.getElementById('terminal-container'));
      term.onData(data => {
        if (socket && socket.readyState === WebSocket.OPEN) {
          socket.send(JSON.stringify({ cmd: 'input', text: data }));
        }
      });
    }
    term.clear();
    term.writeln("\x1b[32m--- Starting Program ---\x1b[0m\r\n");

    const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
    socket = new WebSocket(protocol + window.location.host + '/ws');
    socket.onopen = () => socket.send(JSON.stringify({ cmd: 'run', code: code }));
    socket.onmessage = (event) => {
      const msg = event.data;
      if (msg.startsWith("JSON:")) {
        const data = JSON.parse(msg.substring(5));
        if (data.event === "finished" || data.event === "stopped") term.writeln("\r\n\x1b[31m--- Program Exited ---\x1b[0m");
      } else term.write(msg.replace(/\n/g, '\r\n'));
    };
    socket.onerror = (err) => term.writeln("\r\n[Error] Connection failed.");
  };

  window.stopExecution = function () {
    if (socket) { socket.send(JSON.stringify({ cmd: 'stop' })); socket.close(); }
    document.getElementById('execution-view').classList.add('hidden');
    document.getElementById('exec-ribbon').classList.add('hidden');
    document.getElementById('editor-view').classList.remove('hidden');
    document.getElementById('edit-ribbon').classList.remove('hidden');
  };

  window.newFile = () => { if (confirm("Clear all code?")) window.editor.setValue('Program.Main {\n\t\n}'); };
  window.saveFile = () => {
    const blob = new Blob([window.editor.getValue()], { type: 'text/plain' });
    const a = document.createElement('a');
    a.download = "my_program.ictl"; a.href = URL.createObjectURL(blob); a.click();
  };
  window.openFile = () => {
    const input = document.createElement('input'); input.type = 'file';
    input.onchange = (e) => {
      const reader = new FileReader();
      reader.onload = (event) => window.editor.setValue(event.target.result);
      reader.readAsText(e.target.files[0]);
    };
    input.click();
  };

  // 1. Function to toggle and SAVE
  window.toggleTheme = function() {
    const isDark = document.body.classList.toggle('dark-theme');
    const themeBtn = document.getElementById('themeBtn');
    
    // Save the choice to the browser's memory
    localStorage.setItem('theme', isDark ? 'dark' : 'light');

    if (window.monaco) {
      if (isDark) {
        monaco.editor.setTheme('vs-dark');
        themeBtn.innerHTML = '<span class="material-symbols-outlined">light_mode</span> Switch Theme to Light';
      } else {
        monaco.editor.setTheme('vs');
        themeBtn.innerHTML = '<span class="material-symbols-outlined">dark_mode</span> Switch Theme to Dark';
      }
    }
  };

  // 2. Function to LOAD the theme when the script runs
  (function checkSavedTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-theme');
      // Note: Monaco theme is set in the editor's initialization block
    }
  })();
})();