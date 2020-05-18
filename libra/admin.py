from django.contrib import admin
from .models import *

class bookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in book._meta.fields]

    class Meta:
        model = book

admin.sites.site.register(book, bookAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in category._meta.fields]

    class Meta:
        model = category

admin.sites.site.register(category, categoryAdmin)

class authorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in author._meta.fields]

    class Meta:
        model = author

admin.sites.site.register(author, authorAdmin)

# Register your models here.
