# Generated by Django 3.2.7 on 2022-04-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220425_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
