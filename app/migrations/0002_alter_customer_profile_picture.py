# Generated by Django 4.1.1 on 2022-10-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='retest/static/images/'),
        ),
    ]
