# Generated by Django 3.0.6 on 2020-07-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200715_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blogs/media/'),
        ),
    ]
