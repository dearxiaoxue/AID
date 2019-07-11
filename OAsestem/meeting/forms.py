from django import forms
from django.forms import DateInput, DateTimeInput

'''练习自定义注册表单 RegisterForm
uname 
upwd
uemial
uphone
isActive
'''

MEETPLACE=(("1","请选择会议室"),
           ("第一会议室","第一会议室"),
           ("第二会议室","第二会议室"),
           ("第三会议室","第三会议室"),
           )

# 新建会议
class NewMeetForm(forms.Form):
    # meid = forms.CharField(label='会议编号')
    # mesytime = forms.CharField(label='会议发起时间')
    date = forms.CharField(label='会议日期',widget=DateInput)
    time = forms.CharField(label='会议时间',widget=DateTimeInput)
    meplace = forms.ChoiceField(label='会议地点',choices=MEETPLACE)
    metopic = forms.CharField(label='会议名称')
    # content = forms.CharField(label='会议内容')
    # statu = forms.BooleanField(label='会议状态', required=False)
    # meinitiator = forms.CharField(label='发起者　')
    meattendee = forms.CharField(widget=forms.Textarea,label='参会人员')
    # mepresent = forms.CharField(label='出席人员')
    # menopresent = forms.CharField(label='缺席人员')


# class MyModelForm(forms.ModelForm):
#     class Meta:
#         pass

# 会议查询
class SelectMeetForm(forms.Form):
    meid = forms.CharField(label='会议编号')
    mesytime = forms.CharField(label='会议发起时间')
    date = forms.CharField(label='会议日期')
    time = forms.CharField(label='会议时间')
    meplace = forms.ChoiceField(label='会议地点')
    metopic = forms.CharField(label='会议名称')
    content = forms.CharField(label='会议内容')
    statu = forms.BooleanField(label='会议状态', required=False)
    meinitiator = forms.CharField(label='发起者　')
    meattendee = forms.CharField(label='参会人员')
    mepresent = forms.CharField(label='出席人员')
    menopresent = forms.CharField(label='缺席人员')
