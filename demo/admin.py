from django.contrib import admin
from .models import Book


# Register your models here.
# admin.site.register(Book) # generic view from admin

@admin.register(Book)  # Additional and dynamic view for admin
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description']  # fields in edit view
    list_display = ['title', 'price']  # fields in search view
    list_filter = ['title', 'publishedOn']  # fields to be used for filtering in search view
    search_fields = ['title', 'description']  # fields to be used for searching in search view
