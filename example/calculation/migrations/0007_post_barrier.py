# Generated by Django 2.2.7 on 2020-01-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0006_post_nps'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='barrier',
            field=models.FloatField(default=0),
        ),
    ]
