from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category', )
    search_fields = ('name', 'year', 'genre', 'category', )
    list_filter = ('year', 'genre', 'category', )
    empty_value_display = '-пусто-'


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review)
admin.site.register(Comment)
