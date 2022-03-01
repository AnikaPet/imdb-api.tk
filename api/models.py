from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return '{name}/{filename}'.format(filename=filename,name=instance.__class__.__name__)

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, related_name="company_country", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Actor(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=200, blank=True)
    birthday = models.DateField(null=True,blank=True)
    death = models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to=upload_to,default='default.jpg')

    def __str__(self):
        if self.last_name:
            return self.first_name+" "+self.last_name
        return self.first_name

class Movie(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=10000, blank=True) 
    budget = models.DecimalField(max_digits=10,decimal_places=2, blank=True)
    revenue = models.DecimalField(max_digits=10,decimal_places=2, blank=True)
    runtime = models.DurationField()
    release_date = models.DateField(null=True)
    avg_score = models.FloatField(default=0)
    count_score = models.FloatField(default=0)
    img = models.ImageField(upload_to=upload_to,default='default.jpg')

    language = models.ForeignKey(Language, related_name='movie_language', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='movie_company', on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='movie_genre', on_delete=models.SET_NULL, null=True, blank=True)

    actors = models.ManyToManyField(Actor,through="Cast")

    def __str__(self):
        return self.title

class Cast(models.Model):
    #default null = False
    actor = models.ForeignKey('Actor', related_name = 'cast_actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', related_name = 'cast_movie', on_delete=models.CASCADE)
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.movie.__str__()+" in "+self.actor.__str__()+" as "+self.character_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    reviewed_movies = models.ManyToManyField(Movie,through="Review",related_name="reviews", blank=True)
    saved_movies = models.ManyToManyField(Movie,related_name="watchlist", blank=True)

    def __str__(self):
        return self.user.username

RATINGS = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10')
)

class Review(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    rate = models.IntegerField(choices=RATINGS)
