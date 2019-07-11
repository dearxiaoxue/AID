from django.db import models


# Create your models here.
class Meeting(models.Model):
    meid = models.CharField(max_length=30, db_index=True)  # 会议编号
    mesytime = models.CharField(max_length=30,db_index=True)  # 会议发起时间
    date = models.CharField(max_length=30,db_index=True)  # 会议开会日期
    time = models.CharField(max_length=30)  # 会议开会时间
    meplace = models.CharField(max_length=30)  # 会议地点
    metopic = models.CharField(max_length=50)  # 会议主题
    content = models.CharField(max_length=500, null=True)  # 会议内容
    statu = models.CharField(max_length=50, default='未开')  # 会议状态
    meinitiator = models.CharField(max_length=30)  # 会议发起人
    merecorder = models.CharField(max_length=30)  # 会议记录人
    meattendee = models.CharField(max_length=500)  # 会议参会人员
    mepresent = models.CharField(max_length=500, null=True)  # 会议出席人员
    menopresent = models.CharField(max_length=500, null=True)  # 会议缺席人员

    def __str__(self):
        return "%s,%s,%s,%s,%s" % (self.id, self.meid,self.date, self.metopic, self.statu)

    class Meta:
        db_table = 'meeting'
        verbose_name = '会议'
        verbose_name_plural = '会议'
