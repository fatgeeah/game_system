# Generated by Django 4.2.5 on 2024-01-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamer_username', models.CharField(max_length=255)),
                ('gamer_first_name', models.CharField(max_length=255)),
                ('gamer_last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gamer_games', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_names', models.CharField(max_length=100)),
                ('gameThumbnails', models.ImageField(help_text='.jpg,.png ,.jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Games Thumbnails')),
                ('video', models.FileField(help_text='.mp4 spported only', upload_to='videos/', verbose_name='Video')),
            ],
        ),
    ]
