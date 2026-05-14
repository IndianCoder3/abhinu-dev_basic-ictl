# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

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
