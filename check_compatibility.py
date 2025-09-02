#!/usr/bin/env python3
"""
InstaPy Compatibility Checker for Linux
This script checks if your system is compatible with InstaPy
"""

import sys
import platform
import subprocess
import importlib
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.7+")
        return False

def check_os():
    """Check operating system compatibility"""
    print("🔍 Checking operating system...")
    system = platform.system().lower()
    if system == "linux":
        print(f"✅ {system.capitalize()} - Compatible")
        return True
    else:
        print(f"❌ {system.capitalize()} - This script is for Linux only")
        return False

def check_firefox():
    """Check if Firefox is installed"""
    print("🔍 Checking Firefox installation...")
    try:
        result = subprocess.run(['firefox', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Firefox is installed")
            return True
        else:
            print("❌ Firefox is not working properly")
            return False
    except FileNotFoundError:
        print("❌ Firefox is not installed")
        return False
    except subprocess.TimeoutExpired:
        print("✅ Firefox is installed (timeout during version check)")
        return True

def check_geckodriver():
    """Check if geckodriver is installed"""
    print("🔍 Checking geckodriver installation...")
    try:
        result = subprocess.run(['geckodriver', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ geckodriver is installed")
            return True
        else:
            print("❌ geckodriver is not working properly")
            return False
    except FileNotFoundError:
        print("❌ geckodriver is not installed")
        return False
    except subprocess.TimeoutExpired:
        print("✅ geckodriver is installed (timeout during version check)")
        return True

def check_xvfb():
    """Check if Xvfb is available"""
    print("🔍 Checking Xvfb availability...")
    try:
        result = subprocess.run(['which', 'Xvfb'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Xvfb is available")
            return True
        else:
            print("❌ Xvfb is not available")
            return False
    except Exception:
        print("❌ Could not check Xvfb")
        return False

def check_python_packages():
    """Check required Python packages"""
    print("🔍 Checking Python packages...")
    required_packages = [
        'selenium',
        'requests',
        'urllib3',
        'certifi',
        'chardet',
        'idna',
        'PyYAML',
        'jsonschema',
        'regex',
        'emoji',
        'clarifai',
        'protobuf',
        'grpcio',
        'future',
        'six',
        'plyer'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("✅ All required packages are installed")
        return True

def check_display():
    """Check if DISPLAY is set"""
    print("🔍 Checking DISPLAY environment...")
    display = os.environ.get('DISPLAY')
    if display:
        print(f"✅ DISPLAY is set to: {display}")
        return True
    else:
        print("⚠️  DISPLAY is not set (this is normal for headless servers)")
        return True

def check_permissions():
    """Check file permissions"""
    print("🔍 Checking file permissions...")
    current_dir = Path.cwd()
    install_scripts = ['install_linux.sh', 'install_ubuntu.sh', 'install_centos.sh']
    
    for script in install_scripts:
        script_path = current_dir / script
        if script_path.exists():
            if script_path.stat().st_mode & 0o111:  # Check if executable
                print(f"✅ {script} is executable")
            else:
                print(f"⚠️  {script} is not executable (run: chmod +x {script})")
        else:
            print(f"❌ {script} not found")
    
    return True

def main():
    """Main compatibility check"""
    print("🚀 InstaPy Linux Compatibility Checker")
    print("=" * 50)
    
    checks = [
        check_python_version,
        check_os,
        check_firefox,
        check_geckodriver,
        check_xvfb,
        check_python_packages,
        check_display,
        check_permissions
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Error during check: {e}")
            results.append(False)
        print()
    
    # Summary
    print("=" * 50)
    print("📊 COMPATIBILITY SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("🎉 All checks passed! Your system is compatible with InstaPy.")
        print("\nTo get started:")
        print("1. Run: chmod +x install_*.sh")
        print("2. Run: ./install_linux.sh (or appropriate for your distro)")
        print("3. Activate virtual environment: source instapy_env/bin/activate")
        print("4. Run InstaPy: python quickstart.py")
    else:
        print(f"⚠️  {passed}/{total} checks passed. Some issues need to be resolved.")
        print("\nCommon solutions:")
        print("- Install missing packages: sudo apt install <package> (Ubuntu/Debian)")
        print("- Install missing packages: sudo dnf install <package> (Fedora/CentOS)")
        print("- Install geckodriver manually")
        print("- Check README_LINUX.md for detailed instructions")
    
    return passed == total

if __name__ == "__main__":
    import os
    success = main()
    sys.exit(0 if success else 1)
