# Generated by Django 4.2.5 on 2024-01-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_gamer_gamer_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='gameThumbnails',
            field=models.ImageField(help_text='.jpg, .png, .jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Games Thumbnails'),
        ),
        migrations.AlterField(
            model_name='games',
            name='video',
            field=models.FileField(help_text='.mp4 supported only', upload_to='videos/', verbose_name='Video'),
        ),
    ]
