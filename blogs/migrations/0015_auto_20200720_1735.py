# Generated by Django 3.0.6 on 2020-07-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about1',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about2',
            new_name='about_me',
        ),
    ]
