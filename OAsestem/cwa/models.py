from django.db import models
from employees.models import  Employee
# Create your models here.

class Attendance_status(models.Model):
    uid = models.IntegerField(db_index=True)
    name = models.CharField(max_length=20)
    time = models.CharField( max_length=20)
    log_in = models.CharField(max_length=20)
    log_back = models.CharField(max_length=20,default='未签退')
    isActive = models.CharField(max_length=20,default='正常')

    def __str__(self):
        return '%s.%s,%s,%s,%s,%s'%(self.uid,self.name,self.time,self.log_in,self.log_back,self.isActive)
    class Meta:
        # 指定映射到数据中的表名
        db_table = 'attendance_status'
        # 定义后台中界面的名称(单数)
        verbose_name_plural = 'attendance_status'

class Extras(models.Model):
    modified_section = models.CharField( max_length=20)
    Modify_previous_information = models.CharField( max_length=20)
    message = models.CharField(max_length=120)
    user_status = models.OneToOneField(Attendance_status)

    def __str__(self):
        return '%s.%s,%s'%(self.modified_section,self.Modify_previous_information,self.message)
    class Meta:
        # 指定映射到数据中的表名
        db_table = 'extras'
        # 定义后台中界面的名称(单数)
        verbose_name_plural = 'extras'












