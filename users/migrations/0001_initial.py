# Generated by Django 4.2.4 on 2023-09-08 09:42

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', users.models.UserID(editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('balance', models.FloatField(default=0.0)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
