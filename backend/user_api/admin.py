from django.contrib import admin

from .models import MyUser, Address

class MyUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MyUser._meta.fields if field.name!='id']

class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields if field.name!='id']

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Address, AddressAdmin)