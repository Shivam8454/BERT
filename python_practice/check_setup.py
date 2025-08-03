#!/usr/bin/env python3
"""
Setup check script for Python practice environment.
Run this to verify your Python installation and environment.
"""

import sys
import platform
from datetime import datetime

def check_python_version():
    """Check Python version and compatibility."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print("✅ Python version is compatible")
    else:
        print("❌ Python 3.6+ required")
        return False
    return True

def check_system_info():
    """Display system information."""
    print(f"\nSystem Information:")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python executable: {sys.executable}")

def check_basic_modules():
    """Check if basic modules are available."""
    print(f"\nChecking basic modules:")
    modules = ['os', 'sys', 'json', 'math', 're', 'datetime', 'random']
    
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")

def main():
    """Main setup check function."""
    print("🐍 Python Practice Environment Setup Check")
    print("=" * 50)
    print(f"Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if check_python_version():
        check_system_info()
        check_basic_modules()
        
        print(f"\n🎉 Setup complete! You're ready to start practicing Python.")
        print(f"\nNext steps:")
        print(f"1. Navigate to python_practice/basics/")
        print(f"2. Start with 01_variables.py")
        print(f"3. Work through exercises in order")
    else:
        print(f"\n❌ Please update Python to version 3.6 or higher")

if __name__ == "__main__":
    main()