# 📱 Подробная инструкция по установке и настройке InstaPy на Ubuntu Linux

## 🎯 Обзор

Это подробное руководство по установке и настройке InstaPy на Ubuntu Linux. InstaPy - это инструмент для автоматизации Instagram, который позволяет автоматизировать различные действия в социальной сети.

## 📋 Системные требования

### Минимальные требования
- **ОС**: Ubuntu 18.04 LTS или новее
- **RAM**: 2 GB (рекомендуется 4 GB)
- **Диск**: 5 GB свободного места
- **Интернет**: Стабильное подключение

### Рекомендуемые требования
- **ОС**: Ubuntu 20.04 LTS или 22.04 LTS
- **RAM**: 8 GB
- **Диск**: 10 GB свободного места
- **Процессор**: 2 ядра (рекомендуется 4 ядра)

## 🚀 Быстрая установка (автоматическая)

### Шаг 1: Скачивание проекта
```bash
# Клонируем репозиторий
git clone https://github.com/your-repo/InstaPy.git
cd InstaPy

# Или скачиваем архив
wget https://github.com/your-repo/InstaPy/archive/main.zip
unzip main.zip
cd InstaPy-main
```

### Шаг 2: Запуск автоматической установки
```bash
# Делаем скрипт исполняемым
chmod +x install_ubuntu.sh

# Запускаем установку
./install_ubuntu.sh
```

Скрипт автоматически:
- Установит все системные зависимости
- Скачает и настроит geckodriver
- Создаст виртуальное окружение Python
- Установит все Python пакеты
- Проверит совместимость системы

## 🔧 Ручная установка (пошаговая)

### Шаг 1: Обновление системы
```bash
# Обновляем список пакетов
sudo apt update

# Обновляем систему
sudo apt upgrade -y

# Перезагружаемся (если нужно)
sudo reboot
```

### Шаг 2: Установка системных зависимостей
```bash
# Устанавливаем Python и pip
sudo apt install -y python3 python3-pip python3-venv

# Устанавливаем Firefox
sudo apt install -y firefox

# Устанавливаем Xvfb (виртуальный дисплей)
sudo apt install -y xvfb

# Устанавливаем необходимые библиотеки
sudo apt install -y wget curl tar unzip

# Устанавливаем дополнительные библиотеки
sudo apt install -y libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
    libxss1 libxtst6 libnss3 libcups2 libdrm2 libxkbcommon1 \
    libatspi2.0-0 libgtk-3-0 libgbm1 libasound2
```

### Шаг 3: Установка geckodriver
```bash
# Создаем директорию для драйверов
sudo mkdir -p /opt/geckodriver
cd /opt/geckodriver

# Скачиваем последнюю версию geckodriver
wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-v0.33.0-linux64.tar.gz

# Распаковываем архив
tar -xzf geckodriver-v0.33.0-linux64.tar.gz

# Делаем исполняемым
chmod +x geckodriver

# Создаем символическую ссылку
sudo ln -sf /opt/geckodriver/geckodriver /usr/local/bin/geckodriver

# Проверяем установку
geckodriver --version
```

### Шаг 4: Создание пользователя для InstaPy (рекомендуется)
```bash
# Создаем пользователя
sudo adduser instapy

# Добавляем в группу sudo (если нужно)
sudo usermod -aG sudo instapy

# Переключаемся на пользователя
su - instapy
```

### Шаг 5: Настройка рабочей директории
```bash
# Создаем рабочую директорию
mkdir -p ~/InstaPy
cd ~/InstaPy

# Копируем файлы проекта (если не клонировали)
cp -r /path/to/your/InstaPy/* .
```

### Шаг 6: Создание виртуального окружения Python
```bash
# Создаем виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Обновляем pip
pip install --upgrade pip setuptools wheel
```

### Шаг 7: Установка Python зависимостей
```bash
# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

# Проверяем установку
pip list
```

## ✅ Проверка установки

### Запуск проверки совместимости
```bash
# Активируем виртуальное окружение
source venv/bin/activate

# Запускаем проверку
python check_compatibility.py
```

### Ожидаемый вывод:
```
✅ Python версия: 3.8.10
✅ ОС: Linux
✅ Firefox: установлен
✅ geckodriver: установлен
✅ Xvfb: доступен
✅ Python пакеты: все установлены
✅ DISPLAY: настроен
✅ Права на скрипты: корректны
```

## 🚀 Первый запуск

### Шаг 1: Настройка конфигурации
```bash
# Создаем файл конфигурации
cp quickstart.py quickstart_my_config.py

# Редактируем конфигурацию
nano quickstart_my_config.py
```

### Шаг 2: Базовая конфигурация
```python
# Пример базовой конфигурации
from instapy import InstaPy

# Создаем экземпляр InstaPy
session = InstaPy(
    username="your_username",
    password="your_password",
    headless_browser=True,  # Запуск в фоновом режиме
    bypass_suspicious_attempt=True,
    bypass_with_mobile=True
)

# Логинимся
session.login()

# Простая активность (лайк 10 постов)
session.like_by_tags(['python', 'programming'], amount=10)

# Завершаем сессию
session.end()
```

### Шаг 3: Запуск InstaPy
```bash
# Активируем виртуальное окружение
source venv/bin/activate

# Запускаем в фоновом режиме
python quickstart_my_config.py

# Или используем готовый скрипт
./run_instapy.sh
```

## 🔧 Настройка фонового режима

### Настройка Xvfb
```bash
# Создаем виртуальный дисплей
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &

# Устанавливаем переменную DISPLAY
export DISPLAY=:99

# Добавляем в ~/.bashrc для автоматической настройки
echo 'export DISPLAY=:99' >> ~/.bashrc
echo 'Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &' >> ~/.bashrc
source ~/.bashrc
```

### Настройка systemd сервиса
```bash
# Копируем файл сервиса
sudo cp instapy.service /etc/systemd/system/

# Редактируем файл сервиса
sudo nano /etc/systemd/system/instapy.service

# Перезагружаем systemd
sudo systemctl daemon-reload

# Включаем автозапуск
sudo systemctl enable instapy

# Запускаем сервис
sudo systemctl start instapy

# Проверяем статус
sudo systemctl status instapy
```

## 📊 Мониторинг и управление

### Проверка процессов
```bash
# Запускаем мониторинг
python monitor.py

# Или используем системные команды
ps aux | grep instapy
ps aux | grep firefox
ps aux | grep Xvfb
```

### Управление через скрипты
```bash
# Быстрый запуск
./run_instapy.sh

# Перезапуск
./restart_instapy.sh

# Остановка всех процессов
pkill -f instapy
pkill -f firefox
pkill -f Xvfb
```

## 🐳 Использование Docker (альтернатива)

### Установка Docker
```bash
# Устанавливаем Docker
sudo apt install -y docker.io docker-compose

# Добавляем пользователя в группу docker
sudo usermod -aG docker $USER

# Перезагружаемся
sudo reboot
```

### Запуск в Docker
```bash
# Собираем образ
docker build -t instapy .

# Запускаем контейнер
docker run -d --name instapy-container instapy

# Или используем docker-compose
docker-compose up -d
```

## 🔒 Безопасность

### Настройка файрвола
```bash
# Устанавливаем ufw
sudo apt install -y ufw

# Включаем файрвол
sudo ufw enable

# Разрешаем SSH
sudo ufw allow ssh

# Разрешаем HTTP/HTTPS
sudo ufw allow 80
sudo ufw allow 443

# Проверяем статус
sudo ufw status
```

### Настройка пользователей
```bash
# Создаем отдельного пользователя для InstaPy
sudo adduser instapy --disabled-password --gecos ""

# Ограничиваем доступ
sudo chown -R instapy:instapy /home/instapy/InstaPy
sudo chmod 700 /home/instapy/InstaPy
```

## 🚨 Устранение неполадок

### Частые проблемы и решения

#### 1. Ошибка "geckodriver not found"
```bash
# Проверяем путь
which geckodriver

# Если не найден, добавляем в PATH
echo 'export PATH=$PATH:/opt/geckodriver' >> ~/.bashrc
source ~/.bashrc
```

#### 2. Ошибка "DISPLAY not set"
```bash
# Запускаем Xvfb
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &

# Устанавливаем DISPLAY
export DISPLAY=:99
```

#### 3. Ошибка "Firefox not found"
```bash
# Проверяем установку Firefox
firefox --version

# Переустанавливаем если нужно
sudo apt remove --purge firefox
sudo apt install -y firefox
```

#### 4. Проблемы с правами доступа
```bash
# Проверяем права
ls -la

# Исправляем права
chmod +x *.sh
chmod 644 *.py
```

#### 5. Ошибки Python пакетов
```bash
# Обновляем pip
pip install --upgrade pip

# Переустанавливаем пакеты
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Логи и отладка
```bash
# Просмотр логов InstaPy
tail -f logs/instapy.log

# Просмотр логов Firefox
tail -f ~/.mozilla/firefox/*/geckodriver.log

# Просмотр системных логов
sudo journalctl -u instapy -f
```

## 📚 Дополнительные настройки

### Настройка прокси
```python
# В конфигурации InstaPy
session = InstaPy(
    username="your_username",
    password="your_password",
    proxy_address="proxy.example.com",
    proxy_port=8080,
    proxy_username="proxy_user",
    proxy_password="proxy_pass"
)
```

### Настройка задержек
```python
# Настройка задержек между действиями
session.set_action_delays(
    like_delay=30,
    comment_delay=60,
    follow_delay=45,
    unfollow_delay=35
)
```

### Настройка фильтров
```python
# Фильтр по языку
session.set_mandatory_language(False)
session.set_mandatory_words(['python', 'coding'])

# Фильтр по пользователям
session.set_do_follow(enabled=True, percentage=50)
session.set_do_like(enabled=True, percentage=70)
```

## 🔄 Автоматизация и планировщик

### Настройка cron
```bash
# Открываем crontab
crontab -e

# Добавляем задачу (запуск каждый час)
0 * * * * cd /home/instapy/InstaPy && ./run_instapy.sh

# Добавляем задачу (запуск каждый день в 9:00)
0 9 * * * cd /home/instapy/InstaPy && ./run_instapy.sh
```

### Настройка systemd timer
```bash
# Создаем файл timer
sudo nano /etc/systemd/system/instapy.timer

# Содержимое файла:
[Unit]
Description=Run InstaPy every hour
Requires=instapy.service

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

## 📈 Оптимизация производительности

### Настройка Firefox
```python
# Оптимизация Firefox для автоматизации
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('--disable-extensions')
firefox_options.add_argument('--disable-plugins')
firefox_options.add_argument('--disable-images')
```

### Настройка системы
```bash
# Оптимизация памяти
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf

# Оптимизация файловой системы
echo 'noatime,nodiratime' | sudo tee -a /etc/fstab
```

## 🆘 Получение помощи

### Полезные команды
```bash
# Проверка версий
python3 --version
pip --version
firefox --version
geckodriver --version

# Проверка процессов
ps aux | grep -E "(instapy|firefox|Xvfb)"

# Проверка портов
netstat -tlnp | grep -E "(80|443|8080)"

# Проверка дискового пространства
df -h

# Проверка памяти
free -h
```

### Контакты поддержки
- **GitHub Issues**: [Создать issue](https://github.com/your-repo/InstaPy/issues)
- **Документация**: [README_LINUX.md](README_LINUX.md)
- **Миграция**: [MIGRATE_TO_LINUX.md](MIGRATE_TO_LINUX.md)

## 🎉 Поздравляем!

Вы успешно установили и настроили InstaPy на Ubuntu Linux! Теперь вы можете:

- ✅ Автоматизировать Instagram активности
- ✅ Запускать бота в фоновом режиме
- ✅ Мониторить производительность
- ✅ Управлять через systemd сервисы
- ✅ Использовать Docker для развертывания

## 📝 Следующие шаги

1. **Настройте конфигурацию** под ваши нужды
2. **Протестируйте** на тестовом аккаунте
3. **Настройте мониторинг** и логирование
4. **Изучите дополнительные возможности** InstaPy
5. **Настройте резервное копирование** конфигурации

Удачи в использовании InstaPy! 🚀
