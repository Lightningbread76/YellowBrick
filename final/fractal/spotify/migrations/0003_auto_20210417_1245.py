# Generated by Django 3.2 on 2021-04-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_rename_users_spotifytoken_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotifytoken',
            name='id',
        ),
        migrations.AlterField(
            model_name='spotifytoken',
            name='user',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
