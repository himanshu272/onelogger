# Generated by Django 2.0.5 on 2018-06-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='hit_count',
            field=models.IntegerField(default=0),
        ),
    ]
