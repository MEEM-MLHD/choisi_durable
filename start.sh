docker-machine start choisi-durable
eval "$(docker-machine env choisi-durable)"
export URL='http://'$(docker-machine ip choisi-durable)
python -mwebbrowser $URL
docker-compose up