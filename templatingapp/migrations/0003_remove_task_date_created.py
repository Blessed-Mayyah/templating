# Generated by Django 5.0.4 on 2024-05-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatingapp', '0002_alter_task_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_created',
        ),
    ]
