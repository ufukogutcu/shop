from django.contrib import admin

from .models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields if field.name!='id']

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name!='id']

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
