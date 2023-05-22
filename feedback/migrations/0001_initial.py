# Generated by Django 4.1.8 on 2023-05-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=120)),
                ('description', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_cont', models.TextField(max_length=120, verbose_name='Comment')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='feedback.feedback')),
            ],
        ),
    ]
