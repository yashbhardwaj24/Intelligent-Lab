# Generated by Django 3.2.7 on 2022-05-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_options'),
        ('discord', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='user.Profile'),
        ),
    ]
