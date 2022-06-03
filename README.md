# django-ecommerce


### 💡 How to run

After cloning the repo, do the following to setup the app:

1- from the backend folder, execute those lines:

2- Create your virtual environnement

3- Create your database postgresql and configure settings file

```python
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
