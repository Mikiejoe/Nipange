# Generated by Django 4.2.4 on 2023-09-07 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='members',
            unique_together={('phone', 'group')},
        ),
    ]