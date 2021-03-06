# Generated by Django 4.0.2 on 2022-02-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_actor_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='reviewed_movies',
            field=models.ManyToManyField(blank=True, related_name='reviews', through='api.Review', to='api.Movie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='saved_movies',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='api.Movie'),
        ),
    ]
