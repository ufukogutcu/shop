# Generated by Django 4.2.5 on 2023-10-04 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_alter_myuser_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
    ]
