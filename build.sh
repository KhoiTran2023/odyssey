pip install -r requirements.txt
pip install gunicorn
if [[ $CREATE_SUPERUSER ]];
then python webmaster/manage.py createsuperuserfi --no-input
python manage.py collectstatic --no-input
python manage.py migrate