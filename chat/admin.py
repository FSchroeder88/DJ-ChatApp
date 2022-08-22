from django import forms
from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text', 'created_at', 'time', 'author', 'receiver')
    list_display = ('created_at', 'time', 'author', 'text', 'chat', 'receiver')
    search_fields = ('text',)

# Register your models here.

admin.site.register(Message, MessageAdmin),
admin.site.register(Chat)