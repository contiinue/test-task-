echo '>>> Do migrations'

python app/manage.py makemigrations
python app/manage.py migrate

echo  '>>> Do Tests'

python app/manage.py test api.tests.TemplateApiTest

echo '>>> Starting server'

python app/manage.py runserver 0.0.0.0:8000

echo '>>> Server started'