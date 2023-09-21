pip install -r requirements.txt
pip install gunicorn
if [[ $CREATE_SUPERUSER ]];
then
  python world_champ_2022/manage.py createsuperuser --no-input
fi
python manage.py collectstatic --no-input
python manage.py migrate