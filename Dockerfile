FROM python:3.9-alpine3.16

RUN apk add postgresql-client postgresql-dev build-base && pip install --upgrade pip

#RUN pip install --upgrade pip

# Отключает создание .pyc файлов (скомпилированного кода Python), чтобы не засорять контейнер.
ENV PYTHONDONTWRITEBYTECODE 1
# Отключает буферизацию вывода Python, чтобы логи сразу писались в консоль, а не кэшировались
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements_dev.txt
RUN pip install -r /temp/requirements_dev.txt && rm -rf /temp

COPY service /service

WORKDIR /service

## Сначала работаем от имени root для добавления пользователя nginx и изменения прав
#USER root
## Создаём группу и пользователя nginx
#RUN addgroup -S nginx && adduser -S nginx -G nginx
## Меняем владельца файлов на пользователя nginx
#RUN chown -R nginx:nginx /service/static/
## Устанавливаем разрешения на файлы
#RUN chmod -R 755 /service/static/

#RUN #adduser --disabled-password --no-create-home service-user && apk del build-base postgresql-dev
RUN apk del build-base postgresql-dev
#USER service-user
EXPOSE 8000

# Каждый RUN, COPY, ADD и другие команды создают новый слой, и если содержимое
# какого-то слоя изменится, то все последующие слои (ниже по Dockerfile) будут пересозданы.

#FROM --platform=linux/amd64 python:3.9-alpine3.16
#
## Установка зависимостей, включая curl
#RUN apk add --no-cache \
#    bash \
#    curl \
#    postgresql-dev \
#    postgresql-client \
#    build-base \
#    && curl -sSL https://github.com/vishnubob/wait-for-it/releases/download/v2.3.0/wait-for-it.sh -o /usr/local/bin/wait-for-it \
#    && chmod +x /usr/local/bin/wait-for-it
#
## Копирование зависимостей и исходного кода
#COPY requirements.txt /temp/requirements.txt
#COPY service /service
#
#WORKDIR service
#
## Установка Python зависимостей
#RUN pip install --no-cache-dir -r /temp/requirements.txt
#
## Удаление временных пакетов для уменьшения размера контейнера
#RUN apk del build-base postgresql-dev curl
#
## Создание пользователя для безопасности
#RUN adduser --disabled-password --no-create-home service-user
#
## Переключение на нового пользователя
#USER service-user
#
#EXPOSE 8000