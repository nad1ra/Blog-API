from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description')
    search_fields = ('name',)
    list_filter = ('description',)
