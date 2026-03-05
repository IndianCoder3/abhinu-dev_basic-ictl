# main.py
import sys
from parser import parse_file
from runtime import run_program
from error_handler import ICTLError
from shell import ICTLShell


def main():
    """Main entry point for ICTL interpreter."""
    # if a filename is provided, run that program; otherwise launch interactive shell
    if len(sys.argv) == 1:
        # no arguments - drop into interactive mode
        shell = ICTLShell()
        shell.run()
        return

    file = sys.argv[1]

    # if the first argument isn't an .ictl file, forward everything to shell.py
    if not file.lower().endswith(".ictl"):
        import shell as _shell_module
        _shell_module.sys.argv = sys.argv[:]
        _shell_module.main()
        return

    try:
        program = parse_file(file)
        run_program(program)
    except ICTLError as e:
        # ICTL errors are formatted with line info
        print(str(e))
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ Error: File '{file}' not found")
        sys.exit(1)
    except IOError as e:
        print(f"❌ Error: Cannot read file '{file}': {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
