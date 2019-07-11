from django.db import models

# Create your models here.
class Email_data(models.Model):
    sender=models.CharField(max_length=30)
    receivers=models.CharField(max_length=200)
    copy_to=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    content=models.CharField(max_length=500)
    date=models.CharField(max_length=100)

    def __str__(self):
        return "%s,%s,%s,%s" % (self.id, self.sender, self.subject, self.date)

    class Meta:
        db_table = 'email'
        verbose_name = '邮件'
        verbose_name_plural = '邮件'