from django.contrib import admin
from .models import *
# from models.book import Book
# Register your models here.

from django.contrib import admin

from .models import *
# from .models.book import Book

admin.site.register(Book)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     """Book admin."""

#     list_display = ('title', 'isbn', 'price', 'publication_date')
#     search_fields = ('title',)
#     filter_horizontal = ('authors', 'tags',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin."""

    list_display = ('name', 'email',)
    search_fields = ('name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Publisher admin."""

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin."""

    list_display = ('title',)
    search_fields = ('title',)