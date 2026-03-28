<!-- history.md -->
# 🕒 History
## 5th March 2026
### Initial commit
- Created the project structure
- Released v1.0.0:
  - All Commands:
    - Terminal:
      - Clear: Clear the terminal
      - Echo(): Echo a message
      - Style(): Change the style of the terminal (colors)
    - Data and Math:
      - Math:
        - Compare: Compare two numbers
        - Eval: Evaluate a mathematical expression (orignally used Python's `eval()` function)
      - Data:
        - Compare: Compare two strings if they are equal
    - Variables:
      - Set: Set a variable
      - <name>: Get a variable / Set a variable value (=)
    - Program:
      - Main {...} : The main program block
      - Loop(n) {...} : Loop n times
      - ForeverLoop {...} : Loop forever
      - BreakLoop : Break the current loop (useful with ForeverLoop)
      - If(condition) {...} : If condition is true

---

## 8th March 2026
### Releasing Guide Files as .md (now removed)
- Used to exist in the project but was removed
- You may check the commit history to see the guide files

---

## 10th March 2026
### Switching from PyInstaller to Nuitka
PyInstaller, the standard tool for packaging Python applications was replaced with Nuitka, as it provides better performance as Nuitka uses C.

### Python Code Optimization
Python code was optimized to improve performance. Also, experiments were conducted to replace Python's `eval()` function with a custom parser.

---

## 13th March 2026
### Adding New Commands
- Added new commands to the language:
    - Time:
        - Current(<format>) : Fetches the current time in the specified format, for example: `Time.Current("YYYY-MM-DD HH:MM:SS")`
        - Wait(<secs>) : Wait for the specified number of seconds
    - Math:
        - Random(<min>, <max>) : Generates a random number between min and max.

---

## 14th - 16th March 2026
### Readme Updates
- Updated the README.md file to reflect the changes made to the project.
- Fixed errors in README

---

## 27th March 2026
### Reorganizing the files
- Reorganized the files to improve the structure of the project.
- Clearly seprated the logos, source code, compiled executables, and other files.
- Got rid of unnecessary files.
- Removed Guide Files.

### Setup ICTL Studio Website
- Setup the ICTL Studio website at https://basic-ictl-web-studio.onrender.com/
- Coded the website using Flask, HTML, CSS, and JavaScript.
- Code is merged within the `code` folder, while the code used by Render is seprated into a seprate folder (`ICTL-StudioOnline_Release`).

## 28th March 2026
### Create HISTORY.md
- Created HISTORY.md to keep track of the changes made to the project.

### Create `/editor.html`
- Created `/editor.html` to allow users to edit ICTL code in their browser easily (iFrame points to the ICTL Studio website).

