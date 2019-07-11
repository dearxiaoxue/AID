from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from .models import Email_data
from email.mime.text import MIMEText
from email.header import Header
from time import ctime


# Create your views here.
def e_mail(request):
    if request.method=='GET':
        return render(request,'mail.html')
    else:
        sender=request.POST.get('sender')
        receivers = request.POST.get('receiver')
        copy_to= request.POST.get('copy_to')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "cdy58571230@163.com"  # 用户名
        mail_pass = "bingfeng5857"  # 授权密码，非登录密码
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(sender)
        message['To'] = receivers# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message['Cc'] = copy_to
        message['Subject'] = subject # 邮件主题
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
            Email_data.objects.create(
                sender=sender,
                receivers=receivers,
                copy_to=copy_to,
                subject=subject,
                content=content,
                date=ctime()
            )
            return HttpResponse('发送成功')
        except smtplib.SMTPException as e:
            print(e)
            return HttpResponse('发送失败')