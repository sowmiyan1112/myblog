# Generated by Django 3.0.6 on 2020-07-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
