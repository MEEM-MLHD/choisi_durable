docker-machine start choisi-durable
eval "$(docker-machine env choisi-durable)"
docker-compose run -e DJANGO_SETTINGS_MODULE=choisi_durable.settings -w /src web bash