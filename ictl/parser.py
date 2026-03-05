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
        "Program.Loop",
        "Program.ForeverLoop"
    )
    return any(header.startswith(prefix) for prefix in valid_prefixes)
