# Generated by Django 2.2.7 on 2020-01-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0003_post_delete_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='regress',
            new_name='regressa',
        ),
        migrations.AddField(
            model_name='post',
            name='regressb',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='delete_date',
            field=models.DateTimeField(null=True),
        ),
    ]
