#!/bin/bash

# InstaPy Quick Start Script for Linux
# This script quickly starts InstaPy with proper environment setup

set -e

echo "🚀 Starting InstaPy on Linux..."

# Check if virtual environment exists
if [ ! -d "instapy_env" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run the installation script first:"
    echo "  ./install_linux.sh"
    exit 1
fi

# Check if Xvfb is running
if ! pgrep -x "Xvfb" > /dev/null; then
    echo "🔧 Starting Xvfb virtual display..."
    Xvfb :99 -screen 0 1024x768x24 -ac &
    export DISPLAY=:99
    sleep 2
    echo "✅ Xvfb started on display :99"
else
    echo "✅ Xvfb is already running"
    export DISPLAY=:99
fi

# Check if geckodriver is available
if ! command -v geckodriver &> /dev/null; then
    echo "❌ geckodriver not found in PATH"
    echo "Please install geckodriver or add it to PATH"
    exit 1
fi

# Check if Firefox is available
if ! command -v firefox &> /dev/null; then
    echo "❌ Firefox not found in PATH"
    echo "Please install Firefox browser"
    exit 1
fi

# Activate virtual environment
echo "🐍 Activating Python virtual environment..."
source instapy_env/bin/activate

# Check Python dependencies
echo "📦 Checking Python dependencies..."
if ! python -c "import selenium, requests, urllib3" 2>/dev/null; then
    echo "❌ Required Python packages not found!"
    echo "Please install dependencies: pip install -r requirements.txt"
    exit 1
fi

# Create necessary directories
mkdir -p logs db

# Set environment variables
export PYTHONUNBUFFERED=1
export INSTAPY_WORKSPACE=$(pwd)

echo "✅ Environment setup complete!"
echo "📁 Working directory: $(pwd)"
echo "🖥️  Display: $DISPLAY"
echo "🐍 Python: $(which python)"
echo "🦊 Firefox: $(which firefox)"
echo "🚗 Geckodriver: $(which geckodriver)"
echo ""

# Check if quickstart.py exists
if [ -f "quickstart.py" ]; then
    echo "🎯 Starting InstaPy with quickstart.py..."
    python quickstart.py
else
    echo "📝 quickstart.py not found, starting Python interpreter..."
    echo "You can now import and use InstaPy:"
    echo "  from instapy import InstaPy"
    echo "  session = InstaPy(username='your_username', password='your_password')"
    echo ""
    python
fi
