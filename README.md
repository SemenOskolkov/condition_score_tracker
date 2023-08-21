## Трекер оценки настроения и энергии

### Описание проекта

Приложение предназначенное для сбора оценки по 5-ти бальной шкале показателей настроения и энергии, обработки и
предоставлении отчетов респондентам через Telegram бота.

Приложение запускается через платформу Docker.

### Основные системные требования:

* Python 3.11
* Django 4.2
* Django REST framework 3.14
* TelegramBotAPI 4.12
* Docker 4.21
* Зависимости (Python) из файла **requirements.txt**

### Установка необходимого ПО

#### Создание телеграмм бота
https://core.telegram.org/bots#how-do-i-create-a-bot

#### Установка Docker
https://docs.docker.com/engine/install/

#### проверка версии Docker
```
docker version
```

### Запуск проекта

1. Загрузите проект из Github, воспользовавшись командой
```
git clone git@github.com:SemenOskolkov/condition_score_tracker.git
```

2. Перейдите в директорию проекта **condition_score_tracker**;
```
cd condition_score_tracker
```

3. Создайте в корне проекта файл **.env** для работы с переменным окружением
```
touch .env
```

4. Заполните файл **.env**, используя шаблон из файла **.env.sample**

5. Создайте образ docker контейнера
```
docker-compose build
```

6. Запустите docker контейнер в фоновом режиме
```
docker-compose up -d
```

Чтобы остановить работу контейнера, используйте команду
```
docker-compose down
```
