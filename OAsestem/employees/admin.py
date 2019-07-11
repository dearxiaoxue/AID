from django.contrib import admin
from .models import Employee
# Register your models here.
#声明管理器类

# Register your models here.



class EmployeeManager(admin.ModelAdmin):
    list_display = ['id','em_name','em_age','em_born','gender',
                    'level','department','school','email_id','email_pword','username']
    list_display_links = ['id', 'em_name', 'email_id','username']
    search_fields = ['em_name', 'email_id']



#注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Employee,EmployeeManager)
