# Generated by Django 3.2.5 on 2021-07-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='discord_id',
            field=models.CharField(max_length=50, verbose_name='discord_id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='download (2).jpeg', upload_to='profile_pics'),
        ),
    ]