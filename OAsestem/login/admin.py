from django.contrib import admin
from .models import Users
# Register your models here.
#声明管理器类

# Register your models here.

class UsersManager(admin.ModelAdmin):
    list_display = ['id','username','password']
    list_display_links = ['id','username','password']
    search_fields = ['username','password']



#注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Users,UsersManager)