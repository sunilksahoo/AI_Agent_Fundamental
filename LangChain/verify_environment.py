#!/usr/bin/env python3
"""
Environment Verification Script
Verify that the LangChain lab environment is properly configured.
"""

import sys
import os
from pathlib import Path


LANGCHAIN_DIR = Path(__file__).resolve().parent
VENV_DIR = LANGCHAIN_DIR / ".venv"
MARKERS_DIR = LANGCHAIN_DIR / "markers"
CODE_DIR = LANGCHAIN_DIR / "code"
MINIMUM_PYTHON = (3, 10)

def verify_environment():
    """Verify that all required packages and environment variables are available."""
    print("🔍 Verifying LangChain Lab Environment")
    print("=" * 60)

    # Check Python version
    python_version = sys.version_info
    print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    python_supported = python_version >= MINIMUM_PYTHON
    if not python_supported:
        print("❌ LangChain dependencies require Python 3.10 or newer")

    # Check if running in virtual environment
    print("\n📦 Virtual Environment Check:")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
    else:
        if VENV_DIR.exists():
            print(f"⚠️  Virtual environment exists at {VENV_DIR}")
            print(f"   Please activate it with: source {VENV_DIR}/bin/activate")
            print("   Then run this script again!")
            return False
        else:
            print("⚠️  No virtual environment detected")
            print("   To create one for this project, run from the LangChain folder:")
            print("   python3.12 -m venv .venv")
            print("   source .venv/bin/activate")

    # Check required packages
    print("\n📚 Required Packages:")
    packages_to_check = [
        ('openai', 'OpenAI SDK'),
        ('langchain', 'LangChain Core'),
        ('langchain_openai', 'LangChain OpenAI'),
        ('pydantic', 'Data Validation')
    ]

    missing_packages = []

    for package, description in packages_to_check:
        try:
            __import__(package)
            print(f"✅ {description} ({package}) - Installed")
        except ImportError:
            print(f"❌ {description} ({package}) - Missing")
            missing_packages.append(package)

    # Check environment variables
    print("\n🔑 API Configuration:")
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = os.getenv('OPENAI_API_BASE')

    if api_key:
        print("✅ OPENAI_API_KEY - Configured")
    else:
        print("⚠️  OPENAI_API_KEY - Not set (will be configured in tasks)")

    if api_base:
        print("✅ OPENAI_API_BASE - Configured")
    else:
        print("⚠️  OPENAI_API_BASE - Not set (will be configured in tasks)")

    # Check directories
    print("\n📁 Required Directories:")
    directories = [MARKERS_DIR, CODE_DIR]
    for directory in directories:
        if directory.exists():
            print(f"✅ {directory} - Exists")
        else:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✅ {directory} - Created")

    # Final status
    print("\n" + "=" * 60)
    if missing_packages or not python_supported:
        print("❌ ENVIRONMENT INCOMPLETE")
        if missing_packages:
            print(f"\nMissing packages: {', '.join(missing_packages)}")
        if not python_supported:
            print("\nUse Python 3.10 or newer to create this project's virtual environment.")
        print("\nTo fix, run:")
        print(f"  cd {LANGCHAIN_DIR}")
        print("  python3.12 -m venv .venv")
        print("  source .venv/bin/activate")
        print("  python -m pip install -r requirements.txt")
        return False
    else:
        print("🎉 ENVIRONMENT READY!")
        print("\nYou can now proceed with the LangChain tasks:")
        print("  - Task 1: OpenAI vs LangChain comparison")
        print("  - Task 2: Multi-model support")
        print("  - Task 3: Prompt templates")
        print("  - Task 4: Output parsers")
        print("  - Task 5: Complete chain composition")

        # Create verification marker
        with (MARKERS_DIR / "environment_verified.txt").open("w") as f:
            f.write("VERIFIED")

        if VENV_DIR.exists():
            print("\n💡 Remember to activate the virtual environment:")
            print(f"   source {VENV_DIR}/bin/activate")

        return True

if __name__ == "__main__":
    success = verify_environment()
    sys.exit(0 if success else 1)
