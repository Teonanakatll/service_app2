🔹 Работа с контейнерами
docker run -d --name my_container image_name — запустить контейнер в фоне
docker ps — показать запущенные контейнеры
docker ps -a — показать все контейнеры (включая остановленные)
docker start my_container — запустить остановленный контейнер
docker stop my_container — остановить контейнер
docker restart my_container — перезапустить контейнер
docker rm my_container — удалить контейнер

🔹 Работа с образами
docker images — список скачанных образов
docker pull image_name — скачать образ
docker rmi image_name — удалить образ
docker build -t my_image . — собрать образ из Dockerfile

🔹 Взаимодействие с контейнером
docker logs my_container — посмотреть логи контейнера
docker exec -it my_container sh — зайти внутрь контейнера (если Linux)
docker exec -it my_container bash — зайти внутрь (если есть bash)
docker cp file.txt my_container:/path/ — скопировать файл в контейнер
docker cp my_container:/path/file.txt ./ — скопировать файл из контейнера

🔹 Docker Compose
docker-compose up -d — запустить контейнеры в фоне
docker-compose down — остановить и удалить все контейнеры
docker-compose ps — посмотреть запущенные сервисы
docker-compose logs — логи всех сервисов

@@@@@@@@@@@@@@@@@@@@
docker-compose stop web-app worker flower  # Останавливаем только сервисы без базы

если тебе нужно не только собрать образы (если они изменились), но и сразу запустить контейнеры с этими образами в фоновом режиме
docker-compose up --build -d  # Пересобираем контейнеры

docker-compose run --rm web-app sh -c "python manage.py migrate"
docker-compose run --rm web-app sh -c "python manage.py shell_plus --ipython"

python manage.py dumpdata > db.json
python manage.py dumpdata app_name > db.json
python manage.py dumpdata app_name.ModelName > db.json

python manage.py loaddata db.json

command: bash -c "sleep 10 && python manage.py runserver 0.0.0.0:8000"

                                    django-cachalot
docker-compose run --rm web-app sh -c "python manage.py invalidate_cachalot (client имя прил.) clients.Client"

Если ты точно знаешь, что не хочешь иметь на диске никакие неиспользуемые контейнеры, образы,
тома и сети, и тебе нужно быстро очистить систему от всего, что не используется.
docker system prune -f

удаляет все none образы
в виндовс
FOR /F "tokens=*" %i IN ('docker images -q --filter "dangling=true"') DO docker rmi %i
в линукс
docker images -q --filter "dangling=true" | xargs docker rmi
@@@@@@@@@@@@@@@@@@@@@@@

🔹 Очистка Docker
docker system prune -f — удалить неиспользуемые контейнеры, образы и тома
docker volume prune -f — удалить неиспользуемые тома
docker image prune -f — удалить неиспользуемые образы


                                                статика
docker-compose exec web-app mkdir -p /service/static
docker-compose exec web-app python manage.py collectstatic
docker-compose exec web-app python manage.py shell

docker exec -it ... /bin/sh    войти в терминал контейнера
docker logs ...                посмотреть логи контейнера
docker-compose exec web-app python manage.py clear_cache   очистить кеш контейнера

                        nginx
docker-compose exec nginx nginx -t     проверка конфигурации nginx
docker-compose exec nginx nginx -s reload  перезапуск без остановки контейнера
ls -l /service/static/                 проверка прав к папке
chown -R nginx:nginx /static/          Измените владельца файлов и директорий внутри /static/ на пользователя, от которого работает Nginx
docker-compose restart nginx

docker-compose down -v  # Останавливает контейнеры и удаляет тома
docker volume inspect react_volume
docker volume rm react_volume

> запуск нескольких контейнеров
docker-compose --profile dev up
> 
> ssh -i ~/.ssh/id_rsa root@212.67.14.125
> HuA9W&4aOwYV

C:\Windows\System32\drivers\etc\hosts

Как проверить, раздаётся ли статика?
В контейнере запусти:

sh
Копировать
Редактировать
ls -lah /static/
Должны быть твои файлы.