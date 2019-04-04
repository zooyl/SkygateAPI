# SkygateAPI

### Automatic installation

Open terminal in repository directory.  
Run: ```chmod 777 ./install.sh```  
After that you can install script by ```./install.sh``` command in terminal (make sure you are in the same directory)

### Important
In ```SkygateAPI/SkyGateAPI``` folder, update ```local_settings.py.txt```  to your own settings and delete ```.txt``` from the end
of a file.

### Docker installation

In ```settings.py``` file (lines from 70 to 90), change database for ```DOCKER DB```.  
Now you are ready to go and able to run ```docker-compose up --build```  
Side note: In this case you need to create super user by running ```docker-compose run web python manage.py createsuperuser``` and after that, start server again with ```docker-compose up```.

### Manual installation
Create virtual environment on your machine, then install requirements using:
```
pip install -r requirements.txt
```
Open terminal in ```manage.py``` directory and type ```python manage.py migrate```.
After that, fill database using ```python manage.py loaddata task-exam.json``` .
Run tests ```python manage.py test``` and finally start server by ```python manage.py runserver``` command.

## Chapter II Exercises
Python files are included in ```ChapterII``` folder

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST](https://www.django-rest-framework.org/)
