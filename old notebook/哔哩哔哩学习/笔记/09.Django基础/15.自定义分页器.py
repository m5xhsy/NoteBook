####视图函数
class ParameterError(Exception): #只能单数的错误
    def __init__(self,error):
        print("ParameterError:只能为单数")

class Page(object):
    def __init__(self,obj,page,page_count,max_page=11):
        '''
        :param obj: 要分页的对象
        :param page: 当前页码
        :param page_count:  每页数据数
        :param max_page:    #最大显示分页数(只能为单数)
        '''
        self.page_count = page_count
        self.max_page = max_page
        self.obj = obj
        if self.max_page % 2 == 0:
            raise ParameterError()  #总分页数为双数抛错
        try:
            self.page = int(page)    #判断page是不是数字
        except Exception:
            self.page = 1            #不是数字则跳转到首页
        num = obj.count()       #总数据
        if num % page_count:    #总页数
            self.page_sum = num // self.page_count + 1
        else:
            self.page_sum = num // self.page_count
        if self.page > self.page_sum:
            self.page = self.page_sum
        elif self.page < 0:
            self.page = 1

    @property
    def page_data(self):
        '''
        :return:每一页的数据
        '''
        self.start = (self.page - 1) * self.page_count
        self.end = self.page *self.page_count
        return self.obj[self.start:self.end]

    @property
    def page_bar(self):
        '''
        :return: 分页器按钮html模板
        '''
        html_page = ["<li><a href='?page=1'>首页</a><li>"]
        if self.page == 1:
            previous_page = "<li class='disabled'><a>上一页</a><li>"
        else:
            previous_page = "<li><a href='?page=%s'>上一页</a><li>"%(self.page - 1)
        html_page.append(previous_page)
        margin = self.max_page//2
        if self.page_sum < self.max_page:  # 总分页数小于最大分页数
            for i in range(1,self.page_sum+1):
                if i == self.page:
                    show_page = "<li class='active'><a href='?page=%s'>%s</a><li>"%(i,i)
                else:
                    show_page = "<li><a href='?page=%s'>%s</a><li>"%(i,i)
                html_page.append(show_page)
        elif self.page_sum >= self.max_page and self.page < margin+1:   #page小于左五
            for i in range(1, self.max_page + 1):
                if i == self.page:
                    show_page = "<li class='active'><a href='?page=%s'>%s</a><li>" % (i, i)
                else:
                    show_page = "<li><a href='?page=%s'>%s</a><li>" % (i, i)
                html_page.append(show_page)
        elif self.page_sum >= self.max_page and self.page > self.page_sum-margin:   #page大于右五
            for i in range(self.page_sum+1-self.max_page, self.page_sum+1):
                if i == self.page:
                    show_page = "<li class='active'><a href='?page=%s'>%s</a><li>" % (i, i)
                else:
                    show_page = "<li><a href='?page=%s'>%s</a><li>" % (i, i)
                html_page.append(show_page)
        else:       #左五右五
            for i in range(self.page-margin,self.page+margin+1):
                if i == self.page:
                    show_page = "<li class='active'><a href='?page=%s'>%s</a><li>" % (i, i)
                else:
                    show_page = "<li><a href='?page=%s'>%s</a><li>" % (i, i)
                html_page.append(show_page)
        if self.page == self.page_sum:
            previous_page = "<li class='disabled'><a>下一页</a><li>"
        else:
            previous_page = "<li><a href='?page=%s'>下一页</a><li>"%(self.page + 1)
        html_page.append(previous_page)
        end_page = "<li><a href='?page=%s'>尾页</a><li>"%(self.page_sum)
        html_page.append(end_page)
        html_str = ""
        for itm in range(len(html_page)):
            html_str += html_page[itm]
        return html_str

def div_book(request):
    page = request.GET.get('page')
    book_list = Book.objects.all()
    book_obj = Page(book_list,page,page_count=10,max_page=11)
    return render(request,'div_book.html',{'book_obj':book_obj})




#html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/style/bootstrap.css">
    <style>
        ul{
            display: block;
            position: relative;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
        }
        .top{
            width: 100%;
            height: 50px;
            background-color: #67ffff;
            text-align: center;
            line-height: 50px;
            font-size: 32px;
            color: #5a6268;
        }
        td{
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="top">
        <span>图书管理</span>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-offset-2 col-md-8">
                <table class="table table-striped">
                    <tr>
                        <td>编号</td>
                        <td>书名</td>
                        <td>价格</td>
                    </tr>
                    {% for book in book_obj.page_data %}
                        <tr>
                            <td>{{ book.id }}</td>
                            <td>{{ book.title }}</td>
                            <td>{{ book.price }}</td>
                        </tr>
                    {% endfor %}
                </table>
            </div>
        </div>
    </div>
<div>
    <nav aria-label="Page navigation">
        <ul class="pagination">
            {{ book_obj.page_bar|safe }}
        </ul>
    </nav>
 </div>
</body>
</html> 
'''




####保存搜索条件
- views.py
from app.page import Page
def div_book(request):
    book_list = Book.objects.all()
    book_obj = Page(request,book_list,page_count=10,max_page=11)
    return render(request,'div_book.html',{'book_obj':book_obj})

- page.py
import copy
class ParameterError(Exception): #只能单数的错误
    pass
class Page(object):
    def __init__(self,request,obj,page_count,max_page=11):
        '''
        :param obj: 要分页的对象
        :param reuqest: request对象
        :param page_count:  每页数据数
        :param max_page:    #最大显示分页数(只能为单数)
        '''

        self.page_count = page_count
        self.max_page = max_page
        self.obj = obj
        self.page = request.GET.get('page')
        self.hunt = copy.deepcopy(request.GET)      #将request.GET对象copy成可编辑字典，可以调用urlencode()转换为urlencode格式
        if self.max_page % 2 == 0:
            raise ParameterError('最大分页数不能为双数')  #最大分页数为双数抛错
        try:
            self.page = int(self.page)    #判断page是不是数字
        except Exception:
            self.hunt['page'] = 1            #不是数字则跳转到首页
            self.page = 1
        num = self.obj.count()       #总数据
        if num % self.page_count:    #总页数
            self.page_sum = num // self.page_count + 1
        else:
            self.page_sum = num // self.page_count
        if self.page > self.page_sum:
            self.page = self.page_sum
        elif self.page < 0:
            self.page = 1

    @property
    def page_data(self):
        '''
        :return:每一页的数据
        '''
        self.start = (self.page - 1) * self.page_count
        self.end = self.page *self.page_count
        return self.obj[self.start:self.end]

    @property
    def page_bar(self):
        '''
        :return: 分页器按钮html模板
        '''
        html_page = []
        self.hunt['page'] = 1
        home_page="<li><a href='?%s'>首页</a><li>"%(self.hunt.urlencode())
        html_page.append(home_page)
        self.hunt['page'] = self.page - 1
        if self.page == 1:
            previous_page = "<li class='disabled'><a>上一页</a><li>"
        else:
            previous_page = "<li><a href='?%s'>上一页</a><li>"%(self.hunt.urlencode())
        html_page.append(previous_page)
        margin = self.max_page//2
        if self.page_sum < self.max_page:  # 总分页数小于最大分页数
            for i in range(1,self.page_sum+1):
                self.hunt['page'] = i
                if i == self.page:
                    show_page = "<li class='active'><a href='?%s'>%s</a><li>"%(self.hunt.urlencode(),i)
                else:
                    show_page = "<li><a href='?%s'>%s</a><li>"%(self.hunt.urlencode(),i)
                html_page.append(show_page)
        elif self.page_sum >= self.max_page and self.page < margin+1:   #page小于左五
            for i in range(1, self.max_page + 1):
                self.hunt['page'] = i
                if i == self.page:
                    show_page = "<li class='active'><a href='?%s'>%s</a><li>"%(self.hunt.urlencode(),i)
                else:
                    show_page = "<li><a href='?%s'>%s</a><li>"%(self.hunt.urlencode(), i)
                html_page.append(show_page)
        elif self.page_sum >= self.max_page and self.page > self.page_sum-margin:   #page大于右五
            for i in range(self.page_sum+1-self.max_page, self.page_sum+1):
                self.hunt['page'] = i
                if i == self.page:
                    show_page = "<li class='active'><a href='?%s'>%s</a><li>" % (self.hunt.urlencode(), i)
                else:
                    show_page = "<li><a href='?%s'>%s</a><li>" % (self.hunt.urlencode(), i)
                html_page.append(show_page)
        else:       #左五右五
            for i in range(self.page-margin,self.page+margin+1):
                self.hunt['page'] = i
                if i == self.page:
                    show_page = "<li class='active'><a href='?%s'>%s</a><li>" % (self.hunt.urlencode(), i)
                else:
                    show_page = "<li><a href='?%s'>%s</a><li>" % (self.hunt.urlencode(), i)
                html_page.append(show_page)
        if self.page == self.page_sum:
            previous_page = "<li class='disabled'><a>下一页</a><li>"
        else:
            self.hunt['page'] = self.page + 1
            previous_page = "<li><a href='?%s'>下一页</a><li>"%(self.hunt.urlencode())
        html_page.append(previous_page)
        self.hunt['page'] = self.page_sum
        end_page = "<li><a href='?%s'>尾页</a><li>"%(self.hunt.urlencode())
        html_page.append(end_page)
        html_str = ""
        for itm in range(len(html_page)):
            html_str += html_page[itm]
        return html_str
