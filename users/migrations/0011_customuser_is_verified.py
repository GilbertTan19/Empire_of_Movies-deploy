# Generated by Django 3.0.1 on 2020-06-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customuser_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
