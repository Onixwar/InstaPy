#!/bin/bash

# InstaPy Ubuntu/Debian Installation Script
# This script installs all necessary dependencies for InstaPy on Ubuntu/Debian

echo "Installing InstaPy dependencies for Ubuntu/Debian..."

# Update package list
sudo apt update

# Install system dependencies
echo "Installing system dependencies..."
sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    firefox \
    xvfb \
    libx11-xcb1 \
    libxcb1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libdrm2 \
    libxss1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpulse0 \
    libatspi2.0-0 \
    libcups2 \
    wget \
    tar \
    curl

# Install geckodriver
echo "Installing geckodriver..."
GECKO_VERSION="v0.33.0"
wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz"
tar -xzf "geckodriver-${GECKO_VERSION}-linux64.tar.gz"
sudo mv geckodriver /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
rm "geckodriver-${GECKO_VERSION}-linux64.tar.gz"

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv instapy_env
source instapy_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installation completed!"
echo ""
echo "To activate the virtual environment, run:"
echo "source instapy_env/bin/activate"
echo ""
echo "To run InstaPy, activate the environment and run:"
echo "python quickstart.py"
