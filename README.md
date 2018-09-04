Notes
-----

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py shell

python3 manage.py makemigrations polls2

python3 manage.py sqlmigrate polls2 0001


Deploy on PythonAnyWhere
------------------------

https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial

    mkvirtualenv django2 --python=/usr/bin/python3.6
    git clone https://github.com/csev/djtutorial.git

Make a Web Application in the PYAW UI

    cd /var/www
    vi dj4e_pythonanywhere_com_wsgi.py 

    import os
    import sys
    path = '/home/dj4e/djtutorial'
    if path not in sys.path:
        sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'djtutorial.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

Reload the Application in the UI...

    cd ~/djtutorial
    python manage.py migrate

    python manage.py createsuperuser

    python manage.py shell
    
