from django.contrib import admin
from .models import Article
from .models import About


class ArticleAdmin(admin.ModelAdmin):
    list_display=('number','topic','date')

admin.site.register(Article,ArticleAdmin)



admin.site.register(About)
