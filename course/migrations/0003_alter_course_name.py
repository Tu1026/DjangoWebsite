# Generated by Django 3.2.5 on 2021-07-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=10, verbose_name='What is the course code?'),
        ),
    ]