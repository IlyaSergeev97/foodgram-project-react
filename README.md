# Проект «Foodgram»


Проект "Продуктовый помощник": сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Технологии
* Python 3.2
* DRF
* JWT
* Docker


## Установка и запуск

### Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git@github.com:IlyaSergeev97/yamdb_final.git
```

### Запуск проекта на сервере
Установите Docker и Docker-compose:
```bash
sudo apt install docker.io
```
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```bash
sudo chmod +x /usr/local/bin/docker-compose
```
Проверьте корректность установки Docker-compose:
```bash
sudo  docker-compose --version
```

Отредактируйте файл nginx/default.conf и в строке server_name впишите IP виртуальной машины (сервера).

Скопируйте подготовленные файлы docker-compose.yaml и nginx/default.conf из вашего проекта на сервер:

Зайдите в репозиторий на локальной машине и отправьте файлы на сервер:
```bash
scp docker-compose.yaml <username>@<host>:/home/<username>/docker-compose.yaml
scp default.conf <username>@<host>:/home/<username>/nginx/default.conf
```

Cоздайте .env файл:
На сервере создайте файл nano .env и заполните переменные окружения (или создайте этот файл локально и скопируйте файл по аналогии с предыдущим шагом):

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db

Зайдите на боевой сервер и выполните команды:

На сервере соберите docker-compose:
```bash
sudo docker-compose up -d --build
```

Создаем и применяем миграции:
```bash
sudo docker-compose exec backend python manage.py makemigrations --noinput
sudo docker-compose exec backend python manage.py migrate --noinput
```
Подгружаем статику:
```bash
sudo docker-compose exec backend python manage.py collectstatic --noinput 
```

Создать суперпользователя Django:
```bash
sudo docker-compose exec backend python manage.py createsuperuser
```
### Развёрнутый проект
 После успешнего деплоя проект будет доступен по адрессу:
 ```bash
http://<ipбоевогосервера>
```
### Проект доступен по адресу
 ```bash
http://51.250.19.0
```
