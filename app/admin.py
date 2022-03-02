from django.contrib import admin
from app.models import Chat, Answer, Keyword, Broadcast


class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id', 'tipology', 'enable')
    search_fields = ('name', 'tipology')


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'answer', 'enable')
    search_fields = ('keyword', 'answer__message')


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['message']


class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'message')
    search_fields = ('title', 'message')



admin.site.site_title = 'Telegram Answer Bot Configuration'
admin.site.site_header = admin.site.site_title

admin.site.register(Chat, ChatAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Broadcast, BroadcastAdmin)
