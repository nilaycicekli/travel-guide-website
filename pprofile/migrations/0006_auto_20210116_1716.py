# Generated by Django 3.1.5 on 2021-01-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('pprofile', '0005_auto_20210116_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='liked',
            field=models.ManyToManyField(related_name='liked', to='home.Content'),
        ),
        migrations.AddField(
            model_name='profile',
            name='saved',
            field=models.ManyToManyField(related_name='saved', to='home.Content'),
        ),
    ]