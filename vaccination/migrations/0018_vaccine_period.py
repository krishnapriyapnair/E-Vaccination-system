# Generated by Django 3.0.8 on 2021-01-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0017_remove_vaccine_vdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='period',
            field=models.CharField(max_length=100, null=True),
        ),
    ]