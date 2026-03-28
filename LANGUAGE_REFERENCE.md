# Command Reference

## Terminal Commands

| Command | Description | Example |
|---------|-------------|---------|
| `Terminal.Echo(<expr>)` | Print to console | `Terminal.Echo("Hello")` |
| `Terminal.Ask(<prompt>)` | Get user input | `Variables.X = Terminal.Ask("Enter value: ")` |
| `Terminal.Style(<style>)` | Set text color/style | `Terminal.Style("green")` |
| `Terminal.Clear` | Clear the terminal | `Terminal.Clear` |

## Variable Commands

| Command | Description | Example |
|---------|-------------|---------|
| `Variables.New(<name>)` | Declare variable | `Variables.New(MyVar)` |
| `Variables.<name> = <expr>` | Assign value | `Variables.MyVar = 42` |
| `Variables.<name>` | Read variable | `Terminal.Echo(Variables.MyVar)` |

## Math Commands

| Command | Description | Example |
|---------|-------------|---------|
| `Math.Eval(<expr>)` | Calculate expression | `Math.Eval(10 + 5 * 2)` |
| `Math.Compare(<a>, <op>, <b>)` | Compare numbers | `Math.Compare(X, ">", 5)` |
| `Data.Compare(<a>, <b>)` | Compare values (as strings) | `Data.Compare(Input, "yes")` |
| `Math.Random(<min>, <max>)` | Output a random number in the range | `Math.Random(1, 100)`

## Control Flow

| Command | Description | Example |
|---------|-------------|---------|
| `Program.Main { ... }` | Program entry point | `Program.Main { ... }` |
| `Program.If(<cond>) { ... }` | Conditional execution | `Program.If(cond) { ... }` |
`Program.Else { ... }` | Else for the If | `Program.Else { ... }`
| `Program.Loop(<n>) { ... }` | Loop N times | `Program.Loop(10) { ... }` |
| `Program.ForeverLoop { ... }` | Infinite loop | `Program.ForeverLoop { ... }` |
| `Program.BreakLoop` | Exit loop | `Program.BreakLoop` |
| `Program.Continue` | Next iteration | `Program.Continue` |
| `Program.Not(<cond>)` | Flip a condition | `Program.Not(Data.Compare("h", "h"))` |

## Time Commands
| Command | Description | Example |
|---------|-------------|---------|
| `Time.Wait(<duration in sec>)` | Wait for seconds | `Time.Wait(2.5)` |
| `Time.Current(<format>)` | Fetch current time in a format |   `Variables.Time = Time.Current("hh:mm tt")`

---

> We need more examples to show here! Use this reference and build some examples!