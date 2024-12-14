# Базовый каркас приложения на Django



## Подключены и настроены:

    - PostgreSQL
    - Redis
    - Dockerfile
    - Docker compose
    - Celery


### Для запуска приложения

1. В файле .env.template укажите ваши переменные
2. core/domain настройте ваши слои (DTO, Repository, Service)
3. Предварительно создайте директорию с желаемым приложением
4. 
    Установка новых приложений осуществляется командой

    ```python manage,py startapp имя_приложения core/apps/имя_приложение```
5. Модель User уже создана и настроена, дополните необходимые поля
6. После можете запустить командами:

    ```docker compose build app```

    ```docker compose up app```