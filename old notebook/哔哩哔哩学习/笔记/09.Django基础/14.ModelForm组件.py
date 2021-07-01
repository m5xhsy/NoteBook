from django import froms
class UserInfos(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=["username",'password','date','email','lick','city']
        # exclude='date'    #排除字段
        labels={            #label
            'username':'用户名',
            'password':'密码',
            'date':'出生日期',
            'email':'邮箱',
            'lick':'爱好',
            'city':'城市',
        },
        error_messages={            #错误信息
            'username':{
                'max_length': '密码长读不能超过12位',
                'min_length': '密码长读不能低于6位',
                'required': '密码不能为空'
            }
        },
        from django.forms import widgets as wid     #widgets与widget重名，所以重命名函数
        widgets = {         #widget
            'username':wid.PasswordInput(attrs={'class':'from-c1'}),
            'date':wid.DateInput(attrs={'type':'date'})
        }

    ag_password = forms.CharField(          #补充组件
        label='确认密码',
        max_length=12,
        min_length=6,
        error_messages={
            'max_length': '密码长读不能超过12位',
            'min_length': '密码长读不能低于6位',
            'required': '密码不能为空'
        },
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for filed in self.fields.values():
            filed.error_messages={"required":"不能为空"}        #批量处理错误信息
            filed.widget.attrs.update({'class':'form-control'})     #批量添加类





def index(request):     #添加
    if request.method == 'POST':
        dic = request.POST
        form = UserInfos(dic)
        if form.is_valid():
            # del dic['ag_password']
            # del dic['csrfmiddlewaretoken']
            # user_obj = AbstractUser.objects.filter(username=dic.get('username'))[0]
            # user_obj.lick.add(dic['lick'])
            # del dic['lick']
            # AbstractUser.objects.create_user(**dic)a
            form.save()
            return HttpResponse('ok')
        else:
            print(2)

            return render(request, 'index.html', {'form': form})

    form = UserInfos()
    return render(request,'index.html',{'form':form})

def index_edit(request,uid):    #编辑
    user_obj = UserInfo.objects.filter(id = uid).first()        #获取queryset对象
    if request.method == 'GET':
        form = UserInfos(instance=user_obj)
        return render(request,'index.html',{'form':form})
    else:
        form = UserInfos(request.POST,instance=user_obj)        #实例化时添加instance为更新操作
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            return render(request,'index.html',form)