# yamdb_final
 Учебный проект yamdb_final

## Статус проекта
![Workflow status](https://github.com/mysm/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

Проект **YaMDb** собирает отзывы пользователей на различные произведения.

### Алгоритм регистрации пользователей

1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес  `email`.
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

### Пользовательские роли
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** (`user`) — может, как и **Аноним**, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять **свои** отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор** (`moderator`) — те же права, что и у **Аутентифицированного пользователя** плюс право удалять **любые** отзывы и комментарии.
- **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям. 
- **Суперюзер Django** — обладет правами администратора (`admin`)

### Как запустить проект:

Клонируйте репозиторий проекта c GitHub

```commandline

$ git clone https://github.com/mysm/infra_sp2.git

```

Перейдите в папку infra_sp2/infra и создать в ней файл .env с переменными окружения, необходимыми для работы приложения.

```commandline

cd infra/

```

Пример содержания файла .env

```

DB_ENGINE=django.db.backends.postgresql

DB_NAME=postgres

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

DB_HOST=db

DB_PORT=5432

SECRET_KEY='secret_key'

```

Запустите docker-compose:

```dockerfile

docker-compose up -d

```

В результате будут созданы и запущены в фоновом режиме необходимые для работы приложения контейнеры: db, web, nginx.

В контейнере web выполните миграции, создайте суперпользователя и собрите статику:

```dockerfile

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 

```

Убедитесь, что проект доступен по адресу http://localhost/


Выполнить импорт начальных данных можно командой

```dockerfile

$ docker-compose exec web python manage.py import_csv --csv_file путь_к_файлу --model имя_таблицы

```
например,

```dockerfile

$ docker-compose exec web python manage.py import_csv --csv_file .\static\data\users.csv --model reviews.User

```

При этом файлы с данными для импорта в формате CSV. Кодировка файлов - UTF-8.
Имена столбцов в файле должны совпадать с именами полей таблиц в базе данных.


## Автор

Михаил Мыслицкий