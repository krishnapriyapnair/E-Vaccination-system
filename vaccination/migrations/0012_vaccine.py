# Generated by Django 3.0.8 on 2020-11-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0011_auto_20201122_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=100)),
                ('vdescri', models.CharField(max_length=100)),
                ('vdate', models.CharField(max_length=100)),
                ('vqty', models.CharField(max_length=100)),
            ],
        ),
    ]