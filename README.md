# imdb-api.tk

Simple API using Django Rest Framework.
***
This is API for website ............... It is web service for receiving information about movies and cast information and user management.
See application [here](https://imdb-api.tk/)!
***
Installation
---
How to install an instance of this project:
1. Open terminal and make new directory for project 
```
mkdir project 
cd project
```
2. Clone git repository `git clone https://github.com/AnikaPet/imdb-api.tk.git`
3. Create and activate virtual enviroment
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Install requirements
```
cd ap-blog.tk
pip install -r requirements.txt
```
5. Apply migrations `python3 manage.py migrate`
6. Create superuser `python3 manage.py createsuperuser`
7. Run server `python3 manage.py runserver`

Your instance is running at http://127.0.0.1:8000/
Change DEBUG = False to DEBUG = True in settings.py file. 
