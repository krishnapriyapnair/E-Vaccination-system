# Generated by Django 3.0.8 on 2020-09-27 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0002_user_reg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='dob',
        ),
    ]
