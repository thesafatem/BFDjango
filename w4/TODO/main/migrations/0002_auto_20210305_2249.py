# Generated by Django 3.1.7 on 2021-03-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mark',
            field=models.BooleanField(null=True, verbose_name='Статус'),
        ),
    ]
