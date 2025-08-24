#!/usr/bin/env python3
"""Pre-commit checks for Claude Code hooks"""

import subprocess
import sys


def run_format():
    """Run format check"""
    print("🎨 Running format...")
    try:
        subprocess.run("just fmt", shell=True, check=True)
        print("✅ Format completed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Format failed")
        return False


def main():
    success = run_format()
    sys.exit(0 if success else 2)


if __name__ == "__main__":
    main()
