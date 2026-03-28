# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

from error_handler import SyntaxErrorICTL

def parse_file(path):
    """
    Parse an ICTL program file.
    
    Args:
        path (str): Path to the .ictl file
        
    Returns:
        list: Parsed program structure
        
    Raises:
        SyntaxErrorICTL: On parsing errors
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise SyntaxErrorICTL(f"File not found: {path}")
    except IOError as e:
        raise SyntaxErrorICTL(f"Cannot read file {path}: {e}")

    program = []
    stack = []
    line_number = 0

    for line_number, raw in enumerate(lines, 1):
        line = raw.strip()

        if not line or line.startswith("#"):
            continue

        if line.endswith("{"):
            header = line[:-1].strip()
            
            # Validate block header format
            if not _is_valid_block_header(header):
                raise SyntaxErrorICTL(
                    f"Invalid block header: '{header}'",
                    line=line_number,
                    context=raw.rstrip()
                )
            
            block = {"header": header, "lines": []}

            if stack:
                stack[-1]["lines"].append(block)
            else:
                program.append(block)

            stack.append(block)
            continue

        if line == "}":
            if not stack:
                raise SyntaxErrorICTL(
                    "Unexpected closing brace '}'",
                    line=line_number,
                    context=raw.rstrip(),
                    col=1
                )
            stack.pop()
            continue

        if stack:
            stack[-1]["lines"].append(line)
        else:
            program.append(line)

    if stack:
        raise SyntaxErrorICTL(
            f"Unclosed block '{stack[-1]['header']}'",
            line=line_number,
            context=f"End of file reached"
        )

    return program


def _is_valid_block_header(header):
    """Check if a block header is valid."""
    valid_prefixes = (
        "Program.Main",
        "Program.If",
        "Program.Else",
        "Program.Loop",
        "Program.ForeverLoop"
    )
    return any(header.startswith(prefix) for prefix in valid_prefixes)
