# Generated by Django 2.2.7 on 2019-11-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_admin',
            field=models.BooleanField(default=False),
        ),
    ]
