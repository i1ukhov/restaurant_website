## Сайт для бронирования столиков в ресторане

### Описание задачи
Необходимо создать сайт для бронирования столиков в ресторане. Сайт должен быть сверстан и подключен к админке. Для выполнения задачи необходимо использовать Django и Bootstrap. Сайт должен содержать основные разделы, необходимые для бронирования столиков и управления бронированиями.

### Задача
1. Сверстать сайт для бронирования столиков.
2. Подключить сайт к админке Django.
3. Использовать Bootstrap для создания адаптивного и привлекательного интерфейса.

### Стэк используемых технологий
**Frontend:** HTML, CSS, Bootstrap, JavaScript

**Backend:** Python, Django, PostgreSQL, Git, Docker, Redis, Celery

### Запуск проекта (в PyCharm)
1. Установите виртуальное окружение.
2. Клонируйте проект.
3. Заполните файл .env по шаблону .env.pycharm_sample.
4. Установите зависимости из requerments.txt `pip3 install -r requirements.txt`.
5. Подтянуть фикстуры `python manage.py loaddata fixtures/data.json`
5. Запустите Redis
`sudo service redis-server start`
`redis-cli`.
6. Запустите проект Django `python manage.py runserver`.
9. Запустите celery-worker и celery-beat для выполнения задач.

### Запуск проекта (Docker)
1.  Заполните файл .env по шаблону .env.docker_sample.
2.  Управление с помощью команд:

`docker-compose up` – запуск проекта

`docker-compose up -d` – запуск в режиме демона

`docker-compose down` – для остановки с удалением контейнеров
  