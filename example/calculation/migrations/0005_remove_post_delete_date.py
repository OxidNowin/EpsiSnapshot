# Generated by Django 2.2.7 on 2020-01-21 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0004_auto_20200114_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='delete_date',
        ),
    ]
