# Тестовое Задание
___

## Установка и запуск

#### копируем проект
``
git clone 
``

#### Необходимо задать переменные окружения, в корневой папке проекта необходимо создать .env файл, и вставить следующие переменные 
```
#Django
DJANGO_SECRET_KEY="some_key"


#Mongo
MONGO_HOST='mongodb'
MONGO_USER='root'
MONGO_PASSWORD='mongoadmin'
MONGO_DATABASE_NAME='django_mongodb_docker'
```
## Запуск. Тесты и Миграции выполнятся во время запуска

```
docker-compose up --build
```

