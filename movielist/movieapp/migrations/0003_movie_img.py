# Generated by Django 3.2.13 on 2022-05-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='aaaa', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
