FROM python:3.9-alpine3.16

# Установка зависимостей
RUN apk add --no-cache postgresql-client curl && \
    apk add --no-cache --virtual .build-deps postgresql-dev build-base && \
    pip install --no-cache-dir --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt && \
    rm -rf /temp && \
    apk del .build-deps

COPY service /service
COPY service/entrypoint.sh /service/entrypoint.sh

WORKDIR /service

RUN chmod +x /service/entrypoint.sh && \
    adduser --disabled-password --no-create-home service-user && \
    mkdir -p /service/static /service/media && \
    chown -R service-user:service-user /service  # Дать права на всю директорию

USER service-user

EXPOSE 8000

ENTRYPOINT ["/service/entrypoint.sh"]
CMD ["gunicorn", "service.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "info"]


#FROM python:3.9-alpine3.16
#
#RUN apk add postgresql-client postgresql-dev build-base && pip install --upgrade pip
#
## Отключает создание .pyc файлов (скомпилированного кода Python), чтобы не засорять контейнер.
#ENV PYTHONDONTWRITEBYTECODE 1
## Отключает буферизацию вывода Python, чтобы логи сразу писались в консоль, а не кэшировались
#ENV PYTHONUNBUFFERED 1
#
#COPY requirements.txt /temp/requirements.txt
#RUN pip install -r /temp/requirements.txt && rm -rf /temp
#
#COPY service /service
#
#WORKDIR /service
#
## Копируем entrypoint для миграций
#COPY entrypoint.sh /service/entrypoint.sh
#RUN chmod +x /service/entrypoint.sh
#ENTRYPOINT ["/service/entrypoint.sh"]
#
##RUN #adduser --disabled-password --no-create-home service-user && apk del build-base postgresql-dev
#RUN apk del build-base postgresql-dev
##USER service-user
#EXPOSE 8000
