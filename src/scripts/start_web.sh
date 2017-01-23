#sh /src/scripts/wait.sh

cd /src
export DJANGO_SETTINGS_MODULE=choisi_durable.settings
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages
uwsgi --socket :8000 --wsgi-file /src/choisi_durable/wsgi.py --chdir /src/choisi_durable --master --processes 4 --threads 2 --py-autoreload 3
