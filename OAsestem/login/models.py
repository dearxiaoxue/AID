from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    intro = models.CharField(max_length=20)

    def __str__(self):
        return "%s,%s,%s,%s" % (self.id, self.username, self.password, self.intro)

    class Meta:
        db_table = 'users'
        verbose_name = '账户'
        verbose_name_plural = '账户'
