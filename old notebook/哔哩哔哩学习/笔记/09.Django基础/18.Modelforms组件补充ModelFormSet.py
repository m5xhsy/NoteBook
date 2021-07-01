from django.forms import modelform_factory


class BookModelForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = ['publishi','auther']      #注意，编辑哪个字段这里就写哪个

def xxx(request,id):
    if request.method == "GET":
        model_formset_cls = modelform_factory(model=Book,form=BookModelForm,extel=)        #返回一个类
        queryset = Book.objects.filter(id = id)
        formset = model_formset_cls(queryset = queryset)
        return render(request,'xxx.html',locals())
    else:
        model_formset_cls = modelform_factory(model=Book, form=BookModelForm, extel=)  # 返回一个类
        queryset = Book.objects.filter(id=id)
        formset = model_formset_cls(request.POST)
        if formset.is_valid():
            form.save()         #发生错误用formset.error查看错误
        return render(request.path)



{{ formset.management_form }}       #必须得带
{% for form in formset %}
    <tr>
        {{ form.id }}
        <td>{{ form.instance.title }}</td>      #加instance表示不渲染
        <td>{{ form.publish }}</td>
        <td>{{ form.author }}</td>
    </tr>

{% endfor %}

