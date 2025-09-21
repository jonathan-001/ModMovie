from django.contrib import admin
from .models import Movie, Category, Tag


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release_date', 'rating', 'view_count')
    search_fields = ('title', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'tags')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}