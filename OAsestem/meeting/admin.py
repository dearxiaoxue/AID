from django.contrib import admin
from .models import Meeting
# Register your models here.
#声明管理器类

# Register your models here.



class MeetingManager(admin.ModelAdmin):
    list_display = ['id','meid','mesytime','date','time',
                    'meplace','metopic','content','statu',
                    'meinitiator','merecorder','meattendee','mepresent','menopresent']
    list_display_links = ['id', 'meid','meplace','metopic']
    search_fields = ['meid','meplace','metopic']



#注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Meeting,MeetingManager)
