# Generated by Django 2.2.5 on 2019-09-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190907_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default='no url', max_length=1000),
        ),
    ]
