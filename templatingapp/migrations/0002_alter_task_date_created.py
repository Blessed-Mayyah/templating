# Generated by Django 5.0.4 on 2024-05-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateField(),
        ),
    ]