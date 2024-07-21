# Сервис терминологии

### Описание

Независимый сервис терминологии, который хранит коды данных и их контекст. Используется для обмена данными между различными сторонами.

Используемый стек:

- Python
- Django, DRF
- Drf_yasg
- Pytest
- SQLite

### Инструкция по запуску проекта и работе с ним

Скачивание проекта:

```bash
git clone https://github.com/Vital-yano/terminology_service
cd terminology_service
```

Переименуйте файл .env.example и .env, заранее изменив переменные окружения.

Установка виртуального окружения и зависимостей:

```bash
python -m venv venv && source venv/bin/activate && pip install -r req.txt
```

Применение миграций:

```bash
python manage.py migrate
```

Создание суперюзера (логин и пароль - "admin"):

```bash
python manage.py create_initial_superuser
```

Запуск тестов

```bash
pytest
```

Swagger расположен по адресу:

```
127.0.0.1:8000/refbooks/swagger/
```

Административная панель расположена по адресу:

```
127.0.0.1:8000/admin
```
