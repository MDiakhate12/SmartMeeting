from django.contrib import admin
from main.models import *

from easy_select2 import select2_modelform

MeetingForm = select2_modelform(Meeting, attrs={'width': '250px'})


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo','job','phone']
    list_display_links = ['id', 'user']

admin.site.register(Profile, ProfileAdmin)

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'obj', 'previous_meeting','next_meeting', 'chatroom', 'doing', 'done']
    list_display_links = ['id', 'title']
    form = MeetingForm

admin.site.register(Meeting, MeetingAdmin)


# class TranscriptionAdmin(admin.ModelAdmin):
#     list_display = ['id','author', 'meeting','info','date_posted','last_modified']
#     list_display_links = ['id', 'info']

# admin.site.register(Transcription, TranscriptionAdmin)

class GenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

admin.site.register(Gender, GenderAdmin)
