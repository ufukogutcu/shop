# Generated by Django 4.2.5 on 2023-10-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
