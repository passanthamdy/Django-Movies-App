# Generated by Django 4.0.5 on 2022-06-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_production_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='production_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
