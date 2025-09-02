# 🐧 InstaPy Linux Installation Guide

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/InstaPy/InstaPy.git
cd InstaPy
```

### 2. Run installation script
```bash
# Ubuntu/Debian
chmod +x install_ubuntu.sh
./install_ubuntu.sh

# CentOS/RHEL/Fedora
chmod +x install_centos.sh
./install_centos.sh

# Generic Linux
chmod +x install_linux.sh
./install_linux.sh
```

### 3. Start InstaPy
```bash
chmod +x run_instapy.sh
./run_instapy.sh
```

## Manual Installation

### System Dependencies
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y python3 python3-pip python3-venv firefox xvfb \
    libx11-xcb1 libxcb1 libxrandr2 libasound2 libpangocairo-1.0-0 \
    libatk1.0-0 libcairo-gobject2 libgtk-3-0 libgdk-pixbuf2.0-0 \
    libdbus-1-3 libdrm2 libxss1 libxcomposite1 libxdamage1 \
    libxext6 libxfixes3 libxrandr2 libgbm1 libasound2 libpulse0 \
    libatspi2.0-0 libcups2 wget tar curl

# CentOS/RHEL/Fedora
sudo dnf install -y python3 python3-pip python3-venv firefox \
    xorg-x11-server-Xvfb libX11 libXcb libXrandr alsa-lib pango \
    cairo atk gtk3 gdk-pixbuf2 dbus libdrm libXScrnSaver \
    libXcomposite libXdamage libXext libXfixes mesa-libgbm \
    pulseaudio-libs at-spi2-atk cups-libs wget tar curl
```

### Install geckodriver
```bash
GECKO_VERSION="v0.33.0"
wget "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz"
tar -xzf "geckodriver-${GECKO_VERSION}-linux64.tar.gz"
sudo mv geckodriver /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
rm "geckodriver-${GECKO_VERSION}-linux64.tar.gz"
```

### Python Setup
```bash
python3 -m venv instapy_env
source instapy_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Troubleshooting

### Check compatibility
```bash
python check_compatibility.py
```

### Monitor status
```bash
python monitor.py --detailed
```

### Restart services
```bash
chmod +x restart_instapy.sh
./restart_instapy.sh
```

## Docker (Alternative)

```bash
# Build and run
docker-compose up -d

# Or manual build
docker build -t instapy .
docker run -it --rm instapy
```

## Systemd Service

```bash
# Copy service file
sudo cp instapy.service /etc/systemd/system/

# Edit service file (update user and paths)
sudo nano /etc/systemd/system/instapy.service

# Enable and start
sudo systemctl enable instapy
sudo systemctl start instapy
sudo systemctl status instapy
```

## Support

- Check logs: `tail -f logs/instapy.log`
- Monitor processes: `python monitor.py`
- View system status: `htop` or `top`
- Check Firefox: `firefox --version`
- Check geckodriver: `geckodriver --version`

## Common Issues

1. **Display not found**: Start Xvfb with `Xvfb :99 -screen 0 1024x768x24 &`
2. **Firefox not found**: Install Firefox browser
3. **Permission denied**: Check file permissions with `chmod +x *.sh`
4. **Dependencies missing**: Run installation script again
5. **Process conflicts**: Use restart script to clean up

For more details, see [README_LINUX.md](README_LINUX.md)
