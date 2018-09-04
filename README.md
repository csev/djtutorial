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
    
    from polls2.models import Choice, Question
    from django.utils import timezone
    q = Question(question_text="Answer to the Ultimate Question", pub_date=timezone.now())
    q.save()
    q = Question.objects.get(pk=1)
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.create(choice_text='Pizza', votes=0)
    q.choice_set.create(choice_text='42', votes=0)
    q.choice_set.create(choice_text='Water', votes=0)

