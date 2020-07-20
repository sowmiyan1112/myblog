from django.db import models


class Article(models.Model):
    topic=models.CharField(max_length=250)
    date=models.DateTimeField()
    image=models.ImageField(blank=True, null=True, upload_to='media/')
    content=models.TextField()
    para=models.TextField(default="para")
    thumb=models.ImageField(blank=True, null=True, upload_to='media/')
    published=models.BooleanField(default=True)
    link=models.URLField(blank=True,null=True)
    number=models.IntegerField(blank=True, null =True)
    slug=models.SlugField(default="slug")


class About(models.Model):
    about=models.TextField()
    about_me=models.TextField()
