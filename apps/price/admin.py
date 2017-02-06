from django.contrib import admin
from .models import UserMessage
# Register your models here.

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','image','address')
    search_fields = ('name', 'email')

admin.site.register(UserMessage, UserMessageAdmin)

