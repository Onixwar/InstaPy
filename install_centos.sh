#!/bin/bash

# InstaPy CentOS/RHEL/Fedora Installation Script
# This script installs all necessary dependencies for InstaPy on CentOS/RHEL/Fedora

echo "Installing InstaPy dependencies for CentOS/RHEL/Fedora..."

# Detect package manager
if command -v dnf &> /dev/null; then
    PKG_MANAGER="dnf"
elif command -v yum &> /dev/null; then
    PKG_MANAGER="yum"
else
    echo "Error: No supported package manager found (dnf or yum)"
    exit 1
fi

# Update package list
echo "Updating package list..."
sudo $PKG_MANAGER update -y

# Install system dependencies
echo "Installing system dependencies..."
sudo $PKG_MANAGER install -y \
    python3 \
    python3-pip \
    python3-venv \
    firefox \
    xorg-x11-server-Xvfb \
    libX11 \
    libXcb \
    libXrandr \
    alsa-lib \
    pango \
    cairo \
    atk \
    gtk3 \
    gdk-pixbuf2 \
    dbus \
    libdrm \
    libXScrnSaver \
    libXcomposite \
    libXdamage \
    libXext \
    libXfixes \
    mesa-libgbm \
    pulseaudio-libs \
    at-spi2-atk \
    cups-libs \
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
