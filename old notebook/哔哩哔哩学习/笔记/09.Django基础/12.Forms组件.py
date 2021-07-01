from django import forms

class BookForm(forms.Form):      #forms组件类
    title = forms.CharField(max_length=32)
    price = forms.IntegerField()
    email = forms.EmailField()



form = BookForm({'title':'python','price':123,'email':'m5xhsy@163.com'})
print(form.cleaned_data)            # 所有干净的字段以及对应的值(字典)
print(form.changed_data)            # 所有干净字段(数组)
print(form.errors)                  # ErrorDict : {"校验错误的字段":["错误信息",]}
print(form.errors.get("name"))      # ErrorList ["错误信息",]

Django内置字段:'''
required = True,                    #是否允许为空
widget = None,                      #HTML插件
label = None,                       #用于生成Label标签或显示内容
initial = None,                     #初始值
help_text = '',                     #帮助信息(在标签旁边显示)
error_messages = None,              #错误信息{'required': '不能为空', 'invalid': '格式错误'}
show_hidden_initial = False,        #是否在当前插件后面再加一个隐藏的且具有默认值的插件（可用于检验两次输入是否一直）
validators = [],                    #自定义验证规则
localize = False,                   #是否支持本地化
disabled = False,                   #是否可以编辑
label_suffix = None                 #Label内容后缀

CharField(Field)
    max_length = None,              #最大长度
    min_length = None,              #最小长度
    strip = True                    #是否移除用户输入空白

IntegerField(Field)
    max_value = None,               #最大值
    min_value = None,               #最小值

FloatField(IntegerField)
    ...

DecimalField(IntegerField)
    max_value = None,               #最大值
    min_value = None,               #最小值
    max_digits = None,              #总长度
    decimal_places = None,          #小数位长度

BaseTemporalField(Field)
    input_formats = None            #时间格式化

DateField(BaseTemporalField)        #格式：2015 - 09 - 01
TimeField(BaseTemporalField)        #格式：11: 12
DateTimeField(BaseTemporalField)    #格式：2015 - 09 - 01 11: 12

DurationField(Field)                #时间间隔： % d % H: % M: % S. % f
    ...

RegexField(CharField)
    regex,                          #自定制正则表达式
    max_length = None,              #最大长度
    min_length = None,              #最小长度
    error_message = None,           #忽略，错误信息使用
    error_messages = {'invalid': '...'}

EmailField(CharField)
    ...

FileField(Field)
    allow_empty_file = False        #是否允许空文件

ImageField(FileField)
...
注：需要PIL模块，pip3
    install
    Pillow
    以上两个字典使用时，需要注意两点：
        - form表单中
            enctype = "multipart/form-data"
        - view函数中
            obj = MyForm(request.POST, request.FILES)

URLField(Field)
    ...

BooleanField(Field)
    ...

NullBooleanField(BooleanField)
    ...

ChoiceField(Field)
    ...
    choices = (),                   #选项，如：choices = ((0, '上海'), (1, '北京'),)
    required = True,                #是否必填
    widget = None,                  #插件，默认select插件
    label = None,                   #Label内容
    initial = None,                 #初始值
    help_text = '',                 #帮助提示

ModelChoiceField(ChoiceField)
    ...                          django.forms.models.ModelChoiceField 
    queryset,                       # 查询数据库中的数据
    empty_label = "---------",      # 默认空显示内容
    to_field_name = None,           # HTML中value的值对应的字段
    limit_choices_to = None         # ModelForm中对queryset二次筛选

ModelMultipleChoiceField(ModelChoiceField)
    ...
django.forms.models.ModelMultipleChoiceField

TypedChoiceField(ChoiceField)
    coerce = lambda val: val        #对选中的值进行一次转换
    empty_value = ''                #空值的默认值

MultipleChoiceField(ChoiceField)
...

TypedMultipleChoiceField(MultipleChoiceField)
    coerce = lambda val: val        #对选中的每一个值进行一次转换
    empty_value = ''                #空值的默认值

ComboField(Field)
    fields = ()                     #使用多个验证，如下：即验证最大长度20，又验证邮箱格式
    fields.ComboField(fields=[fields.CharField(max_length=20), fields.EmailField(), ])

MultiValueField(Field)
    PS: 抽象类，子类中可以实现聚合多个字典去匹配一个值，要配合MultiWidget使用

SplitDateTimeField(MultiValueField)
    input_date_formats = None       #格式列表：['%Y--%m--%d', '%m%d/%Y', '%m/%d/%y']
    input_time_formats = None       #格式列表：['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']

FilePathField(ChoiceField)          #文件选项，目录下文件显示在页面中
    path,                           #文件夹路径
    match = None,                   #正则匹配
    recursive = False,              #递归下面的文件夹
    allow_files = True,             #允许文件
    allow_folders = False,          #允许文件夹
    required = True,
    widget = None,
    label = None,
    initial = None,
    help_text = ''

GenericIPAddressField
    protocol = 'both',              #both, ipv4, ipv6支持的IP格式
    unpack_ipv4 = False             #解析ipv4地址，如果是::ffff: 192.0时候，可解析为192PS：protocol必须为both才能启用

SlugField(CharField)
    数字，字母，下划线，减号（连字符）
    ...

UUIDField(CharField)        uuid类型
'''
Django内置插件:'''
TextInput(Input)                    文本
NumberInput(TextInput)              数字
EmailInput(TextInput)               邮箱
URLInput(TextInput)         
PasswordInput(TextInput)            密码
HiddenInput(TextInput)
Textarea(Widget)
DateInput(DateTimeBaseInput)        日期
DateTimeInput(DateTimeBaseInput)    日期
TimeInput(DateTimeBaseInput)        
CheckboxInput                       
Select
NullBooleanSelect
SelectMultiple                      单选
RadioSelect
CheckboxSelectMultiple
FileInput
ClearableFileInput
MultipleHiddenInput
SplitDateTimeWidget
SplitHiddenDateTimeWidget
SelectDateWidget
'''
常用选择插件'''
from django.forms import fields
# 单radio，值为字符串
# user = fields.CharField(
#     initial=2,
#     widget=widgets.RadioSelect(choices=((1,'上海'),(2,'北京'),))
# )
  
# 单radio，值为字符串
# user = fields.ChoiceField(
#     choices=((1, '上海'), (2, '北京'),),
#     initial=2,
#     widget=widgets.RadioSelect
# )
  
# 单select，值为字符串
# user = fields.CharField(
#     initial=2,
#     widget=widgets.Select(choices=((1,'上海'),(2,'北京'),))
# )
  
# 单select，值为字符串
# user = fields.ChoiceField(
#     choices=((1, '上海'), (2, '北京'),),
#     initial=2,
#     widget=widgets.Select
# )
  
# 多选select，值为列表
# user = fields.MultipleChoiceField(
#     choices=((1,'上海'),(2,'北京'),),
#     initial=[1,],
#     widget=widgets.SelectMultiple
# )
  
  
# 单checkbox
# user = fields.CharField(
#     widget=widgets.CheckboxInput()
# )
  
  
# 多选checkbox,值为列表
# user = fields.MultipleChoiceField(
#     initial=[2, ],
#     choices=((1, '上海'), (2, '北京'),),
#     widget=widgets.CheckboxSelectMultiple
# )
'''



视图函数'''
from django.forms import ValidationError    #抛错
from django import forms
from django.forms import widgets        #添加类
class BookForm(forms.Form):
    username = forms.CharField(
        label='账号',
        min_length=6,
        max_length=10,
        error_messages={
            'max_length':'用户名长读最多10位',
            'min_length':'用户名长读最少6位',
            'required': '不能为空',
            'invalid': '格式错误'
        },
        widget = widgets.TextInput(attrs={'class':'form-control'})  #添加类，bootstrap
    )
    password = forms.CharField(
        label='密码',
        max_length=12,
        min_length=8,
        error_messages={
            'max_length': '密码最多12位',
            'min_length': '密码最少8位',
            'required': '密码不能为空'
        },
        widget = widgets.PasswordInput(attrs={'class':'form-control'})
    )
    eg_password = forms.CharField(
        label='确认密码',
        max_length=12,
        min_length=8,
        error_messages={
            'max_length': '确认密码最多12位',
            'min_length': '确认密码最少8位',
            'required': '确认密码不能为空'
        },
        widget=widgets.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱不能为空',  # required,校验不能为空的固定用法
            'invalid': '邮箱格式错误',  # invalid,专门用来校验邮箱格式错误的固定用法
        },
        widget = widgets.EmailInput(attrs={'class':'form-control'})
    )
    def clean_username(self):   #局部钩子
        print(self.cleaned_data)
        val = self.cleaned_data.get('username')
        ret = User.objects.filter(username=val)
        if not ret:
            return val
        else:
            raise ValidationError('用户名已存在')

    def clean_password(self):   #局部钩子
        val = self.cleaned_data.get('password')     #局部cleaned_data获取的是当前字段的数据
        print(val)
        if val.isalpha():
            raise ValidationError('密码不能是纯字母')
        elif val.isdigit():
            raise ValidationError('密码不能是纯数字')
        else:
            return val

    def clean(self):    #全局钩子
        pswd = self.cleaned_data.get('password')    #全局cleaned_data获取的是全部数据
        eg_pswd = self.cleaned_data.get('eg_password')
        if pswd == eg_pswd and pswd and eg_pswd:
            return self.cleaned_data
        else:
            self.add_error('eg_password','密码不一致')       #将错误添加到errors字典
            raise ValidationError('密码不一致')


def forms(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():     #判断
            dic = form.cleaned_data
            del dic['eg_password']
            User.objects.create_user(**dic)
            return HttpResponse('ok')
        else:
            # eg_error = form.errors.get("__all__")
            return render(request,'forms.html',{'form':form})
    # fm = BookForm({'user':'','pswd':'','email':''})
    # print(fm.is_valid())
    # print(fm.cleaned_data)
    # print(fm.errors.get('pswd'))
    # # from django.forms.utils import ErrorDict
    # return render(request,'forms.html',{'fm':fm.errors.get('email')})
    form = BookForm()
    return render(request,'forms.html',{'form':form})
    '''
视图函数补充'''
给所有input标签添加class
    sex = forms.ChoiceField(
        label='性别',
        choices=((1,'男'),(2,'女')),
        error_messages={
            'invalid': '格式错误',
            'required': '性别不能为空'
        },
        widget=widgets.Select(attrs={'class':'form-control'})       #单选
    )
    city = forms.ModelChoiceField(
        label='城市',
        queryset=(City.objects.all()),
        widget=widgets.Select(attrs={'class':'form-control'}),      #单选
        error_messages={
            'invalid': '格式错误',
            'required': '城市不能为空'
        },
    )
    lick = forms.ModelMultipleChoiceField(
        label='爱好',
        queryset=(Lick.objects.all()),
        widget=widgets.SelectMultiple(attrs={'class':'form-control'}),      #多选
        error_messages = {
            'invalid': '格式错误',
            'required': '爱好不能为空'
        },
    )
    date = forms.DateField(
        label='出生日期',
        widget=widgets.DateInput(attrs={'class':'form-control','type':'date'})      #日期
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class':'abc'})

'''
html
方法一:'''
    直接form渲染
'''
方法二:'''
    <div class="container">
        <div class="row">
            <div class="col-md-4 col-md-offset-4">
                <form action="" novalidate method="post">
                    {% csrf_token %}
                        <div class="form-group">
                            <label for="id_user">账号</label>
                             {{ form.username }}
                            <div style="height: 15px">
                                <span class="error">{{ form.errors.username.0 }}</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="id_pswd">密码</label>
                            {{ form.password }}
                            <div style="height: 15px">
                                <span class="error">{{ form.errors.password.0 }}</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="id_pswd">密码</label>
                            {{ form.eg_password }}
                            <div style="height: 15px">
                                <span class="error">{{ form.errors.eg_password.0 }}</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="id_email">邮箱</label>
                            {{ form.email }}
                            <div style="height: 15px">
                                <span class="error">{{ form.errors.email.0 }}</span>
                            </div>
                        </div>
                    <input type="submit" value="提交" class="btn btn-success pull-right">
                </form>
            </div>
        </div>
    </div>

'''
方法三:'''
<div class="container">
        <div class="row">
            <div class="col-lg-4 col-lg-offset-4 col-md-4 col-md-offset-4 col-sm-4 col-sm-offset-4 col-xs-6 col-xs-offset-3 ">
                <form action="" method="post" novalidate>
                    {% csrf_token %}
                    {% for foo in form %}
                        <div class="form-group">
                            <label for="">{{ foo.label }}</label>
                            {{ foo }}
                            <div style="height: 12px;float: right;">
                                <span style="line-height: 12px;font-size:12px;color: red;">
                                        {{ foo.errors.0 }}
                                </span>
                            </div>
                        </div>
                    {% endfor %}
                    <div style="margin-top:20px;display: block">
                        <input type="submit" value="提交" class="btn btn-success pull-right">
                    </div>
                </form>
            </div>
        </div>
    </div>
'''

