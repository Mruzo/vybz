# Generated by Django 4.1.8 on 2023-05-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='summary',
            field=models.CharField(max_length=120),
        ),
    ]
