# Generated by Django 3.2.16 on 2022-12-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_alter_timetracker_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetracker',
            name='counting',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
