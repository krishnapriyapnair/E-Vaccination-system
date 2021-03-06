# Generated by Django 3.0.8 on 2020-11-23 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0013_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='vacci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.Vaccine'),
        ),
        migrations.CreateModel(
            name='Allocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, null=True)),
                ('alstatus', models.CharField(max_length=100)),
                ('aldate', models.CharField(max_length=100)),
                ('altime', models.CharField(max_length=100)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.User_reg')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.Vaccine')),
            ],
        ),
    ]
