# Generated by Django 4.2.6 on 2023-10-29 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_datecompleted_task_datacompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='datacompleted',
            new_name='datecompleted',
        ),
    ]
