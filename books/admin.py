from django.contrib import admin
from .models import Book, Reviews

class ReviewInline(admin.TabularInline):
    model = Reviews


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display=("title","author","price",)

admin.site.register(Book, BookAdmin)