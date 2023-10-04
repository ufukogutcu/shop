from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields if field.name!='id']

admin.site.register(Item, ItemAdmin)
