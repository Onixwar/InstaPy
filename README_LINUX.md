# InstaPy для Linux

Этот документ содержит инструкции по установке и запуску InstaPy на Linux системах.

## Системные требования

- Linux (Ubuntu 18.04+, CentOS 7+, RHEL 7+, Fedora 28+)
- Python 3.7+
- Firefox браузер
- Xvfb (для headless режима)
- Минимум 2GB RAM
- Минимум 1GB свободного места на диске

## Быстрая установка

### Ubuntu/Debian
```bash
chmod +x install_ubuntu.sh
./install_ubuntu.sh
```

### CentOS/RHEL/Fedora
```bash
chmod +x install_centos.sh
./install_centos.sh
```

### Общий Linux
```bash
chmod +x install_linux.sh
./install_linux.sh
```

## Ручная установка

### 1. Установка системных зависимостей

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv firefox xvfb \
    libx11-xcb1 libxcb1 libxrandr2 libasound2 libpangocairo-1.0-0 \
    libatk1.0-0 libcairo-gobject2 libgtk-3-0 libgdk-pixbuf2.0-0 \
    libdbus-1-3 libdrm2 libxss1 libxcomposite1 libxdamage1 \
    libxext6 libxfixes3 libxrandr2 libgbm1 libasound2 libpulse0 \
    libatspi2.0-0 libcups2 wget tar curl
```

#### CentOS/RHEL/Fedora:
```bash
# Для dnf (Fedora, CentOS 8+)
sudo dnf install -y python3 python3-pip python3-venv firefox \
    xorg-x11-server-Xvfb libX11 libXcb libXrandr alsa-lib pango \
    cairo atk gtk3 gdk-pixbuf2 dbus libdrm libXScrnSaver \
    libXcomposite libXdamage libXext libXfixes mesa-libgbm \
    pulseaudio-libs at-spi2-atk cups-libs wget tar curl

# Для yum (CentOS 7, RHEL 7)
sudo yum install -y python3 python3-pip python3-venv firefox \
    xorg-x11-server-Xvfb libX11 libXcb libXrandr alsa-lib pango \
    cairo atk gtk3 gdk-pixbuf2 dbus libdrm libXScrnSaver \
    libXcomposite libXdamage libXext libXfixes mesa-libgbm \
    pulseaudio-libs at-spi2-atk cups-libs wget tar curl
```

### 2. Установка geckodriver

```bash
GECKO_VERSION="v0.33.0"
wget "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz"
tar -xzf "geckodriver-${GECKO_VERSION}-linux64.tar.gz"
sudo mv geckodriver /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
rm "geckodriver-${GECKO_VERSION}-linux64.tar.gz"
```

### 3. Создание виртуального окружения

```bash
python3 -m venv instapy_env
source instapy_env/bin/activate
pip install --upgrade pip
```

### 4. Установка Python зависимостей

```bash
pip install -r requirements.txt
```

## Запуск InstaPy

### 1. Активация виртуального окружения

```bash
source instapy_env/bin/activate
```

### 2. Запуск примера

```bash
python quickstart.py
```

### 3. Запуск в headless режиме

```bash
# Запуск Xvfb
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99

# Запуск InstaPy
python quickstart.py
```

## Решение проблем

### Ошибка "geckodriver not found"
```bash
# Проверьте, что geckodriver установлен
which geckodriver

# Если не найден, добавьте в PATH
export PATH=$PATH:/usr/local/bin
```

### Ошибка "Firefox not found"
```bash
# Установите Firefox
sudo apt install firefox  # Ubuntu/Debian
sudo dnf install firefox  # Fedora/CentOS 8+
sudo yum install firefox  # CentOS 7/RHEL 7
```

### Ошибка "Display not found"
```bash
# Запустите Xvfb
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
```

### Проблемы с правами доступа
```bash
# Сделайте скрипты исполняемыми
chmod +x install_*.sh

# Проверьте права на geckodriver
ls -la /usr/local/bin/geckodriver
```

## Настройка для продакшена

### 1. Создание systemd сервиса

Создайте файл `/etc/systemd/system/instapy.service`:

```ini
[Unit]
Description=InstaPy Service
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/instapy
Environment=DISPLAY=:99
ExecStart=/usr/bin/Xvfb :99 -screen 0 1024x768x24
ExecStop=/bin/kill -TERM $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2. Автозапуск

```bash
sudo systemctl enable instapy
sudo systemctl start instapy
```

## Мониторинг

### Логи
Логи InstaPy сохраняются в папке `logs/` в рабочей директории.

### Мониторинг процесса
```bash
# Проверка статуса
ps aux | grep instapy

# Проверка логов
tail -f logs/instapy.log
```

## Безопасность

- Используйте виртуальное окружение
- Не запускайте от имени root
- Ограничьте доступ к файлам конфигурации
- Регулярно обновляйте зависимости

## Поддержка

При возникновении проблем:

1. Проверьте логи в папке `logs/`
2. Убедитесь, что все зависимости установлены
3. Проверьте версии Python и Firefox
4. Создайте issue в GitHub репозитории

## Лицензия

InstaPy распространяется под лицензией GPLv3.
