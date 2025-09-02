# InstaPy

[![Build Status](https://travis-ci.org/InstaPy/InstaPy.svg?branch=master)](https://travis-ci.org/InstaPy/InstaPy)
[![PyPI version](https://badge.fury.io/py/instapy.svg)](https://badge.fury.io/py/instapy)
[![Python 3.5|3.6|3.7|3.8|3.9](https://img.shields.io/pypi/pyversions/instapy.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 🤖 Instagram Bot - Automated Instagram Interactions

**InstaPy** is a tool for automated Instagram interactions using Python and Selenium. It provides a simple and efficient way to automate Instagram activities while respecting Instagram's limits and best practices.

## ✨ Features

- **Automated Interactions**: Like, comment, follow, unfollow, and more
- **Smart Targeting**: Target users by hashtags, locations, or specific criteria
- **Rate Limiting**: Built-in protection against Instagram's rate limits
- **Multi-Platform Support**: Works on Windows, macOS, and Linux
- **Headless Mode**: Run without GUI for server environments
- **Extensive Logging**: Detailed logs for monitoring and debugging
- **Plugin System**: Extensible architecture for custom functionality

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Firefox browser
- Internet connection

### Installation

#### Option 1: Using pip (Recommended)
```bash
pip install instapy
```

#### Option 2: From source
```bash
git clone https://github.com/InstaPy/InstaPy.git
cd InstaPy
pip install -r requirements.txt
```

### Basic Usage

```python
from instapy import InstaPy

# Create an InstaPy session
session = InstaPy(username="your_username", password="your_password")

# Login
session.login()

# Like posts by hashtag
session.like_by_tags(['python', 'programming'], amount=5)

# Follow users by hashtag
session.follow_by_tags(['python'], amount=3)

# End the session
session.end()
```

## 🐧 Linux Support

InstaPy has been optimized for Linux systems with dedicated installation scripts and monitoring tools.

### Quick Linux Installation

#### Ubuntu/Debian
```bash
chmod +x install_ubuntu.sh
./install_ubuntu.sh
```

#### CentOS/RHEL/Fedora
```bash
chmod +x install_centos.sh
./install_centos.sh
```

#### Generic Linux
```bash
chmod +x install_linux.sh
./install_linux.sh
```

### Linux Features

- **Automatic Dependency Installation**: Scripts install all required system packages
- **Headless Mode Support**: Optimized for server environments with Xvfb
- **Systemd Integration**: Ready-to-use service files for production deployment
- **Docker Support**: Containerized deployment with Docker and docker-compose
- **Monitoring Tools**: Built-in monitoring and status checking scripts

### Linux Monitoring

```bash
# Check system compatibility
python check_compatibility.py

# Monitor InstaPy status
python monitor.py

# Detailed monitoring
python monitor.py --detailed

# Save status to JSON
python monitor.py --json
```

## 🐳 Docker Support

### Quick Docker Start
```bash
# Build and run with docker-compose
docker-compose up -d

# Or build manually
docker build -t instapy .
docker run -it --rm instapy
```

## 📚 Documentation

- [Complete Documentation](https://instapy.org/)
- [Quick Start Guide](docs/quickstart.md)
- [Linux Installation Guide](README_LINUX.md)
- [API Reference](docs/api.md)
- [Examples](examples/)

## 🔧 Configuration

### Basic Settings
```python
session = InstaPy(
    username="your_username",
    password="your_password",
    headless_browser=True,  # Run without GUI
    disable_image_load=True,  # Faster performance
    page_delay=25,  # Wait time between actions
)
```

### Advanced Settings
```python
# Set custom delays
session.set_action_delays(
    enabled=True,
    like=3,
    comment=5,
    follow=4,
    unfollow=8
)

# Set quotas
session.set_quota_supervisor(
    enabled=True,
    peak_comments_daily=50,
    peak_follows_daily=100,
    peak_likes_daily=200
)
```

## 🛡️ Safety Features

- **Rate Limiting**: Automatic delays between actions
- **Quota Management**: Daily limits for interactions
- **Smart Delays**: Randomized delays to avoid detection
- **Blacklist Support**: Exclude specific users or hashtags
- **Activity Logging**: Track all interactions for compliance

## 📊 Monitoring & Analytics

### Built-in Monitoring
```python
# Get current statistics
followers = session.get_followers()
following = session.get_following()

# Log activity
session.log_followers()
session.log_following()
```

### External Monitoring
```bash
# Check process status
python monitor.py

# View logs
tail -f logs/instapy.log

# System monitoring
htop
```

## 🔌 Plugins

InstaPy supports plugins for extended functionality:

- **Telegram Integration**: Get notifications via Telegram
- **Custom Analytics**: Build custom reporting
- **API Extensions**: Add new Instagram interaction methods

## 🚨 Important Notes

- **Respect Instagram's Terms**: Use responsibly and within limits
- **Rate Limiting**: Don't exceed recommended interaction rates
- **Account Safety**: Use dedicated accounts for automation
- **Legal Compliance**: Ensure compliance with local laws and regulations

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/InstaPy/InstaPy.git
cd InstaPy
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the GPL v3 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Selenium](https://selenium.dev/) - Web automation framework
- [Firefox](https://www.mozilla.org/firefox/) - Web browser
- [Python](https://www.python.org/) - Programming language

## 📞 Support

- **Documentation**: [https://instapy.org/](https://instapy.org/)
- **Issues**: [GitHub Issues](https://github.com/InstaPy/InstaPy/issues)
- **Discussions**: [GitHub Discussions](https://github.com/InstaPy/InstaPy/discussions)
- **Wiki**: [GitHub Wiki](https://github.com/InstaPy/InstaPy/wiki)

## ⚠️ Disclaimer

This tool is for educational and research purposes. Users are responsible for complying with Instagram's Terms of Service and applicable laws. The developers are not responsible for any misuse of this tool.

---

**Made with ❤️ by the InstaPy Community**
