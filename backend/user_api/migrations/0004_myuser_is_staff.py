# Generated by Django 4.2.5 on 2023-10-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_remove_myuser_is_active_remove_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]