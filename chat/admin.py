from django.contrib import admin
from chat.models import *

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'eid']
    list_display_links = ['id', 'eid']

admin.site.register(ChatRoom, ChatRoomAdmin)

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room','user','sender','date','text']
    list_display_links = ['id', 'room','user','sender','date','text']

admin.site.register(ChatMessage, ChatMessageAdmin)