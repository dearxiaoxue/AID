from django.db import models


#
#
# Create your models here.
class Employee(models.Model):
    em_name = models.CharField(max_length=30, unique=True)
    em_age = models.IntegerField()
    em_born = models.DateField()
    gender = models.CharField(max_length=30)
    level = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    school = models.CharField(max_length=30)
    email_id = models.EmailField()
    email_pword = models.CharField(max_length=30)
    username = models.ForeignKey('login.Users', on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s,%s,%s" % (self.id, self.em_name, self.department, self.email_id)

    class Meta:
        db_table = 'employee'
        verbose_name = '员工'
        verbose_name_plural = '员工'
