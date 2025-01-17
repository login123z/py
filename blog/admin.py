from django.contrib import admin
from blog.models import Category,Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug'] # отображение id, title, slug
    search_fields = ['title'] # поиск по title
    ordering = ['id'] # сортировка по id]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'is_active',]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['is_active', 'category']
    list_editable = ['is_active', 'category']