# imdb-api.tk

Simple API using Django Rest Framework.
***
This is API for receiving information about movies, actors, cast information and user management.
There are 3 types of users: anonymous user, registered user and superuser. Anonymous user can brows through movies and see reviews and information about cast. Registered user has their own profile and can leave reviews or add movies to their watchlist. Superuser can manage content on the website. 
See application and docs [here](https://imdb-api.tk/)!
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
4. Change values in .env.example and rename it to .env
5. Install requirements
```
cd ap-blog.tk
pip install -r requirements.txt
```
6. Apply migrations `python3 manage.py migrate`
7. Create superuser `python3 manage.py createsuperuser`
8. Run server `python3 manage.py runserver`

Your instance is running at http://127.0.0.1:8000/ <br>
Change DEBUG = False to DEBUG = True in settings.py file. 

***
With Docker Compose
---
5. Run
```
docker-compose up
```
Your instance is running at http://0.0.0.0:8000/
