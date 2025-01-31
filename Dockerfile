# для некоторых пакетов (Pillow, numpy, pandas) придётся установить зависимости, Если нужен Python с меньшими
# проблемами при установке пакетов, лучше взять python:3.9-slim
FROM python:3.9-alpine3.16

# копируем файл зависимостей и папку проекта в докер контейнер
COPY requirements.txt /temp/requirements.txt
COPY service /service

# устанавливает рабочую директорию внутри контейнера.  все команды (RUN, COPY, CMD и др.) будут выполняться относительно /service
# тоесть все команды будут зпускаться из папки в которай находится файл manage.py
WORKDIR /service
# указывает, что контейнер будет использовать порт 8000 для входящих соединений. Но это не открывает порт наружу, а
# просто документирует его. Чтобы реально пробросить порт, нужно запускать контейнер с флагом -p
# docker run -p 8000:8000 my_image
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
# запускает приложение внутри контейнера, юзер только для запуска процессов в контейнере с пониженными привилегиями
# в ситеме получается просто нет пользователя с рут правами поэтому и нет уязвимостей связанных с root доступом
RUN adduser --disabled-password service-user

# чтобы команды не запускались под root указываем нашего юзера
USER service-user