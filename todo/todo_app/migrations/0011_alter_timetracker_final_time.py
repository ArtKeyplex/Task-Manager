# Generated by Django 3.2.16 on 2022-12-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0010_alter_timetracker_final_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracker',
            name='final_time',
            field=models.IntegerField(default=0),
        ),
    ]
