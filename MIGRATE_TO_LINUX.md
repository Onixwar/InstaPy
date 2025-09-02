# 🚀 Миграция InstaPy на Linux

## Обзор изменений

Проект InstaPy был проанализирован и исправлен для оптимальной работы на Linux системах. Вот что было исправлено:

## 🔧 Основные исправления

### 1. Обновление зависимостей (requirements.txt)
- ✅ Обновлен Selenium до версии 4.x
- ✅ Заменен устаревший webdriverdownloader на webdriver-manager
- ✅ Обновлены все пакеты до совместимых версий
- ✅ Добавлен psutil для мониторинга

### 2. Исправление browser.py
- ✅ Убрана поддержка устаревшего DesiredCapabilities
- ✅ Обновлен код для Selenium 4.x
- ✅ Исправлены проблемы с кодировкой
- ✅ Улучшена обработка ошибок

### 3. Исправление instapy.py
- ✅ Убраны устаревшие импорты
- ✅ Исправлены проблемы с кодировкой
- ✅ Обновлен код для совместимости

### 4. Улучшение settings.py
- ✅ Улучшено определение операционной системы
- ✅ Добавлена поддержка путей Linux по умолчанию

## 📁 Новые файлы для Linux

### Скрипты установки
- `install_linux.sh` - Общий скрипт для Linux
- `install_ubuntu.sh` - Для Ubuntu/Debian
- `install_centos.sh` - Для CentOS/RHEL/Fedora

### Скрипты управления
- `run_instapy.sh` - Быстрый запуск
- `restart_instapy.sh` - Перезапуск сервисов
- `check_compatibility.py` - Проверка совместимости
- `monitor.py` - Мониторинг процессов

### Docker поддержка
- `Dockerfile` - Контейнер для InstaPy
- `docker-compose.yml` - Оркестрация контейнеров
- `.dockerignore` - Оптимизация сборки

### Системные файлы
- `instapy.service` - Systemd сервис
- `README_LINUX.md` - Подробная документация для Linux
- `INSTALL_LINUX.md` - Краткая инструкция по установке

## 🚀 Быстрый старт на Linux

### 1. Клонирование и настройка
```bash
git clone <your-repo-url>
cd InstaPy
chmod +x *.sh
```

### 2. Установка зависимостей
```bash
# Ubuntu/Debian
./install_ubuntu.sh

# CentOS/RHEL/Fedora
./install_centos.sh

# Общий Linux
./install_linux.sh
```

### 3. Запуск
```bash
./run_instapy.sh
```

## 🔍 Проверка совместимости

```bash
python check_compatibility.py
```

## 📊 Мониторинг

```bash
# Базовый мониторинг
python monitor.py

# Детальный мониторинг
python monitor.py --detailed

# Сохранение статуса
python monitor.py --json
```

## 🐳 Docker альтернатива

```bash
# Быстрый запуск
docker-compose up -d

# Ручная сборка
docker build -t instapy .
docker run -it --rm instapy
```

## ⚙️ Системная интеграция

### Systemd сервис
```bash
sudo cp instapy.service /etc/systemd/system/
sudo systemctl enable instapy
sudo systemctl start instapy
```

### Автозапуск
```bash
sudo systemctl enable instapy
```

## 🛠️ Устранение неполадок

### Проверка процессов
```bash
# Проверка статуса
python monitor.py

# Остановка всех процессов
./restart_instapy.sh

# Проверка логов
tail -f logs/instapy.log
```

### Частые проблемы
1. **Xvfb не запущен**: `Xvfb :99 -screen 0 1024x768x24 &`
2. **Firefox не найден**: Установите Firefox браузер
3. **geckodriver не найден**: Проверьте PATH или переустановите
4. **Права доступа**: `chmod +x *.sh`

## 📈 Преимущества новой версии

- ✅ **Совместимость**: Работает с современными версиями Python и Selenium
- ✅ **Производительность**: Оптимизировано для Linux серверов
- ✅ **Надежность**: Улучшена обработка ошибок и восстановление
- ✅ **Мониторинг**: Встроенные инструменты для отслеживания состояния
- ✅ **Автоматизация**: Скрипты для установки и управления
- ✅ **Контейнеризация**: Docker поддержка для развертывания
- ✅ **Системная интеграция**: Systemd сервисы для продакшена

## 🔄 Обновление существующих установок

### 1. Резервное копирование
```bash
cp -r ~/InstaPy ~/InstaPy_backup
```

### 2. Обновление кода
```bash
cd ~/InstaPy
git pull origin main
```

### 3. Обновление зависимостей
```bash
source instapy_env/bin/activate
pip install -r requirements.txt --upgrade
```

### 4. Проверка совместимости
```bash
python check_compatibility.py
```

## 📞 Поддержка

При возникновении проблем:

1. Запустите `python check_compatibility.py`
2. Проверьте логи: `tail -f logs/instapy.log`
3. Используйте мониторинг: `python monitor.py --detailed`
4. Обратитесь к документации: `README_LINUX.md`

## 🎯 Следующие шаги

1. **Тестирование**: Проверьте работу на тестовой системе
2. **Настройка**: Адаптируйте конфигурацию под ваши нужды
3. **Мониторинг**: Настройте регулярный мониторинг
4. **Автоматизация**: Настройте автозапуск через systemd
5. **Резервное копирование**: Настройте регулярное резервное копирование

---

**Удачи с InstaPy на Linux! 🐧✨**
