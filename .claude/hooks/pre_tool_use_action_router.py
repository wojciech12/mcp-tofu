#!/usr/bin/env python3
"""Pre-tool-use action router for Claude Code"""

import json
import sys
from pathlib import Path
from pre_commit_checks import run_format

# Add the hooks directory to the Python path
hooks_dir = Path(__file__).parent
sys.path.insert(0, str(hooks_dir))


def main():
    try:
        # Read JSON input from stdin
        input_data = sys.stdin.read().strip()
        if not input_data:
            print("No input data received")
            sys.exit(0)

        # Parse JSON
        data = json.loads(input_data)

        # Extract command from JSON
        command = data.get("tool_input", {}).get("command", "")

        print(f"🔍 Checking command: {command}")

        # Check if it's a git command
        if command.startswith("git"):
            if "git add" in command or "git commit" in command:
                print("🔍 Git operation detected - running format check...")
                if not run_format():
                    print("❌ Format check failed")
                    sys.exit(2)
                print("✅ Format check passed")

        # Allow the command to proceed
        sys.exit(0)

    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(0)


if __name__ == "__main__":
    main()
