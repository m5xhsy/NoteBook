from django.db import models
#ORM:   object relation mapping        对象关系映射
# Create your models here.
#单表创建
class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)  #999999.99
    pub_date = models.DateField()   #1999-12-12     DataTinmeField()包含时分秒
    publish = models.CharField(max_length=32)
#多表创建
class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)  # 999999.99
    pub_date = models.DateField(auto_now_add=True)      #自动添加当前时间
    publish = models.ForeignKey(to = 'Publish',to_field = 'id',on_delete = models.CASCADE,limit_choices_to={"pk":3},db_constraint=False)   # db_constraint=False #是否建立约束        #pk=3
    author_book = models.ManyToManyField(to = 'Author')
    class Meta:
        unique_together = ("title","pub_date")      #联合唯一
        db_table =

class Publish(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    ad = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length = 32,related_name = "xxx")   #起别名
    age = models.IntegerField(max_length = 32)
    email = models.CharField(max_length = 32)
    gander = models.IntegerField(choices=((1,'男'),(2,'女')),default=1)
    # obj = UserInfo.filter(pk = 1)
    # obj.gander          #取出来值为1
    # obj.get_gander_display()    #取出来的值为对应的值

# class Author_book(models.Model):
#     id = models.AutoField(primary_key = True)
#     author = models.IntegerField(max_length = 32)
#     book = models.IntegerField(max_length = 32)
pymysql'''settings同目录下init.py文件
    import pymysql
    pymysql.version_info = (1, 3, 13, "final", 0)
    pymysql.install_as_MySQLdb()
'''


字段'''
<1> CharField
        字符串字段, 用于较短的字符串.
        CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.

<2> IntegerField
       #用于保存一个整数.

<3> FloatField
        一个浮点数. 必须 提供两个参数:

        参数    描述
        max_digits    总位数(不包括小数点和符号)
        decimal_places    小数位数
                举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:

                models.FloatField(..., max_digits=5, decimal_places=2)
                要保存最大值一百万(小数点后保存10位)的话,你要这样定义:

                models.FloatField(..., max_digits=19, decimal_places=10)
                admin 用一个文本框(<input type="text">)表示该字段保存的数据.

<4> AutoField
        一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段;
        自定义一个主键：my_id=models.AutoField(primary_key=True)
        如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.

<5> BooleanField
        A true/false field. admin 用 checkbox 来表示此类字段.

<6> TextField
        一个容量很大的文本字段.
        admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).

<7> EmailField
        一个带有检查Email合法性的 CharField,不接受 maxlength 参数.

<8> DateField
        一个日期字段. 共有下列额外的可选参数:
        Argument    描述
        auto_now    当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
        auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
        （仅仅在admin中有意义...)

<9> DateTimeField
         一个日期时间字段. 类似 DateField 支持同样的附加选项.

<10> ImageField
        类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        如果提供这两个参数,则图片将按提供的高度和宽度规格保存.    
<11> FileField
     一个文件上传字段.
     要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting,
     该格式将被上载文件的 date/time
     替换(so that uploaded files don't fill up the given directory).
     admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) .

     注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
            （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
            (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
             WEB服务器用户帐号是可写的.
            （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
             使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
             出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
             叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.

<12> URLField
      用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且
      没有返回404响应).
      admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)

<13> NullBooleanField
       类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要用 BooleanField 加 null=True 选项
       admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.

<14> SlugField
       "Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.#它们通常用于URLs
       若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  #在
       以前的 Django 版本,没有任何办法改变50 这个长度.
       这暗示了 db_index=True.
       它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate
       the slug, via JavaScript,in the object's admin form: models.SlugField
       (prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.

<13> XMLField
        一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.

<14> FilePathField
        可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
        参数    描述
        path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目.
        Example: "/home/images".
        match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名. 
        注意这个正则表达式只会应用到 base filename 而不是
        路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
        recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
        这三个参数可以同时使用.
        match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
        FilePathField(path="/home/images", match="foo.*", recursive=True)
        ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif

<15> IPAddressField
        一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
<16> CommaSeparatedIntegerField
        用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.

'''
参数'''
(1)null
    如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.

(1)blank 
    如果为True，该字段允许不填。默认为False。
    要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
    如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。

(2)default
    字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。

(3)primary_key
    如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
    Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
    否则没必要设置任何一个字段的primary_key=True。

(4)unique
    如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
    
(5)choices
    由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
'''

Django模型之Meta选项详解'''Book._meta.model_name
Django模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性。而可用的选项大致包含以下几类

abstract
    这个属性是定义当前的模型是不是一个抽象类。所谓抽象类是不会对应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段。

Options.abstract
    如果abstract = True 这个model就是一个抽象类

app_label
    这个选型只在一种情况下使用，就是你的模型不在默认的应用程序包下的models.py文件中，这时候需要指定你这个模型是哪个应用程序的。
    Options.app_label
    如果一个model定义在默认的models.py，例如如果你的app的models在myapp.models子模块下，你必须定义app_label让Django知道它属于哪一个app
    app_label = 'myapp'

db_table
    db_table是指定自定义数据库表明的。Django有一套默认的按照一定规则生成数据模型对应的数据库表明。
    Options.db_table
    定义该model在数据库中的表名称
    　　db_table = 'Students'
    如果你想使用自定义的表名，可以通过以下该属性
    　　table_name = 'my_owner_table'

db_teblespace
    Options.db_teblespace
    定义这个model所使用的数据库表空间。如果在项目的settin中定义那么它会使用这个值

get_latest_by
    Options.get_latest_by
    在model中指定一个DateField或者DateTimeField。这个设置让你在使用model的Manager上的lastest方法时，默认使用指定字段来排序

managed
    Options.managed
    默认值为True，这意味着Django可以使用syncdb和reset命令来创建或移除对应的数据库。默认值为True,如果你不希望这么做，可以把manage的值设置为False

order_with_respect_to
    这个选项一般用于多对多的关系中，它指向一个关联对象，就是说关联对象找到这个对象后它是经过排序的。指定这个属性后你会得到一个get_xxx_order()和set_xxx_order()的方法，通过它们你可以设置或者回去排序的对象

ordering
    这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。这是一个字符串的元组或列表，没有一个字符串都是一个字段和用一个可选的表明降序的'-'构成。当字段名前面没有'-'时，将默认使用升序排列。使用'?'将会随机排列
        ordering=['order_date'] # 按订单升序排列
        ordering=['-order_date'] # 按订单降序排列，-表示降序
        ordering=['?order_date'] # 随机排序，？表示随机
        ordering=['-pub_date','author'] # 以pub_date为降序，在以author升序排列
permissions
    permissions主要是为了在Django Admin管理模块下使用的，如果你设置了这个属性可以让指定的方法权限描述更清晰可读。Django自动为每个设置了admin的对象创建添加，删除和修改的权限。
    permissions = (('can_deliver_pizzas','Can deliver pizzas'))

proxy
    这是为了实现代理模型使用的，如果proxy = True,表示model是其父的代理 model 

unique_together
    unique_together这个选项用于：当你需要通过两个字段保持唯一性时使用。比如假设你希望，一个Person的FirstName和LastName两者的组合必须是唯一的，那么需要这样设置：
    unique_together = (("first_name", "last_name"),)
    一个ManyToManyField不能包含在unique_together中。如果你需要验证关联到ManyToManyField字段的唯一验证，尝试使用signal(信号)或者明确指定through属性。

verbose_name
    verbose_name的意思很简单，就是给你的模型类起一个更可读的名字一般定义为中文，我们：
    verbose_name = "学校"

verbose_name_plural
    这个选项是指定，模型的复数形式是什么，比如：
    verbose_name_plural = "学校"
    如果不指定Django会自动在模型名称后加一个’s’
'''


数据库迁移'''
    djiango会把settings中的INSTALLED_APPS中的models对应的类创建成数据库中的表

语法:
    python manage.py makemigrations
    python manage.py migrate
'''
QuerySet特性'''
1.可以切片使用：不支持负的索引
    book_list=models.Book.objects.all()
    print(book_list)   #<QuerySet [<Book: python>, <Book: go>]>
    book_list[0:1]   #<QuerySet [<Book: python>]>
2.可迭代
    book_list=models.Book.objects.all()
     for obj in book_list: 
    　　　　print(obj.title,obj.price)
3.惰性查询:
    创建查询集不会带来任何数据库的访问,对这个查询集求值时，才会真正运行这个查询
    query = Person.objects.filter(first_name="Dave")
    queryset=Book.objects.all() 此时只是创建了查询集query,并没有运行，因此并没有执行相应的sql语句
    要真正从数据库获得数据，需要遍历queryset:
    for article in queryset:
        print(article.title)    # hits database
    print(queryset) # hits database 对queryset进行了查询，sql语句执行
4.缓存机制：
    当遍历queryset时，所有匹配的记录会从数据库获取，然后转换成Django的model。这些model会保存在queryset内置的cache中，
    如果再次遍历这个queryset，将直接使用缓存中的结果
    执行下列代码，queryset执行两次，但sql只执行了一次
    queryset=Book.objects.all()
    for obj in queryset:
        print(obj.title)
    for obj1 in queryset:
        print(obj1.title)
    使用同一查询集，sql只执行一次
    queryResult=models.Book.objects.all()
    print([a.title for a in queryResult])
    print([a.create_time for a in queryResult])
    执行下列代码，queryset执行两次，sql执行了两次
    for obj in Book.objects.all():
            print(obj.title)
    for obj1 in Book.objects.all():
        print(obj1.title)
    重复获取查询集对象中一个特定的索引需要每次都查询数据库
    queryset = Entry.objects.all()
    print queryset[5] # Queries the database
    print queryset[5] # Queries the database again
 

queryset优化     
    exists()与iterator()方法
    queryset的cache最有用的地方是可以有效的测试queryset是否包含数据，只有有数据时才会去遍历
    1.if语句会触发queryset的执行
        book_list=models.Book.objects.all()
        if book_list:  #执行sql，查询数据库
            for obj in queryset:
            print(obj.title)
    2.当需求只是否判断数据是否存在，而不需要遍历所有的数据。这种情况，简单的使用if语句进行判断也会完全执行整个queryset
    并且把数据放入cache
        book_list=models.Book.objects.all() 
        if book_list: #我们并不需要所有的数据，但是ORM仍然会获取所有记录！ 
        　　print("ok") 用exists()方法来检查是否有数据： 
        book_list=models.Book.objects.all() 　　
        　　if book_list.exists(): # 没有数据从数据库获取，从而节省了带宽和内存。只取第一条内容 print("ok")
    3.处理成千上万的记录时，将它们一次装入内存是很浪费的。更糟糕的是，巨大的queryset可能会锁住系统进程，让你的程序濒临崩溃。
    要避免在遍历数据的同时产生queryset cache，可以使用iterator()方法来获取数据，处理完数据就将其丢弃
    复制代码
        queryset = Book.objects.all()
        iter=queryset.iterator() 可以一次只从数据库获取少量数据，这样可以节省内存
        print(type(iter))   <class 'generator'> 生成器
        for obj in iter:
            print(obj.title)
    再次遍历没有打印,因为迭代器已经在上一次遍历(next)到最后一次了,没得遍历了
        for obj in iter:
            print(obj.title)
    queryset的cache是用于减少程序对数据库的查询, 使用exists()和iterator()方法可以优化程序对内存的使用。不过，由于它们并不会生成queryset cache
    可能会造成额外的数据库查询。

'''

增删改查-单表操作'''
import App.models from Book     #在views中引入表(类)
def index(request):             #视图函数
#增:
    #方式一
    book = Book(title = 'python',princ = '22.50',pub_data = '1995-2-10',pulish = '人民出版社')
    book.save()
    print(book.id)
    #方式二
    book = Book.objects.create(title = 'python',princ = '22.50',pub_data = '1995-2-10',pulish = '人民出版社')    #返回值为当前实例化对象
    print(book.id)
    #方式三：批量插入
    book_list = []
    for i in range(100):
        book_obj = Book(title = 'book'+str(i),price=random.random()*100)
        book_list.append(book_obj)
        Book.objects.bulk_create(book_list)
#删
    Book.objects.filter(title = 'python').delete()
#改
    user_obj = User.objects.filter(username=user, password=pswd).first()
    Book.objects.update_or_create(user= user_obj ,defaults={
        'token':'xxx'
    })  # 查找user_obj,如果有token则更新，没有则添加
    Book.objects.filter(id = 1).update(title = 'python')        #只能filter，不能get
#查
    ret = Book.objects.all()                                            #objects管理器调用 返回QuerySet对象 全部
    ret = Book.objects.filter(title = 'python')                         #objects管理器调用 返回QuerySet对象
    ret = Book.objects.get(title = 'python')                            #objects管理器调用 返回模型对象
    ret = Book.objects.exclude(id = 20)                                 #objects管理器调用 返回QuerySet对象 排除，与filter相反
    ret = Book.objects.first()                                          #QuerySet对象调用  返回模型对象     相当于all().first()
    ret = Book.objects.last()                                           #QuerySet对象调用  返回模型对象     相当于all().last()
    ret = Book.objects.all().order_by("price",'-id')                    #QuerySet对象调用  返回QuerySet对象 先按price排序，相同的按id反序排序(加' - '为倒序)
    ret = Book.objects.all().count()                                    #QuerySet对象调用  返回int类型      查询个数
    ret = Book.objects.all().reverse()                                  #QuerySet对象调用  返回QuerySet对象 反向排序
    ret = Book.objects.all().exists()                                  #QuerySet对象调用  返回bool值       判断标中有没有值
    ret = Book.objects.all().values('title','price')                    #QuerySet对象调用  返回QuerySet字典 [{'title':'python','price':23},{'title':'linux','price':30}]
    ret = Book.objects.all().values_list('title','price')               #QuerySet对象调用  返回QuerySet元组 [('title',23,),('price',30,)]
    ret = Book.objects.all().values_list('title','price').distinct()    #QuerySet对象调用  返回QuerySet对象 去重 只对值操作，不能对对象操作

    模糊查询
        ret = Book.objects.filter(price__gt = 200)                      #大于200
        ret = Book.objects.filter(price__lt = 200)                      #小于200
        ret = Book.objects.filter(price__gte = 200)                     #大于等于200
        ret = Book.objects.filter(price__lte = 200)                     #小于等于200
        ret = Book.objects.filter(prine__in = [100,200,300])            #在列表里面的值
        ret = Book.objects.filter(title__startswith = 'py')             #py开头的
        ret = Book.objects.filter(title__istartswith = 'py')            #py开头 不区分大小写
        ret = Book.objects.filter(title_contains = 'py')                #包含py
        ret = Book.objects.filter(title__range = [200,300])             #列表范围内的值
        ret = Book.objects.filter(dete__year = 2020,date__month=7)      #指定范围时间的 Mysql数据库要去setting里面设置USE_TZ = False 保持时序一致#
        ret = Book.objects.filter(dete__year__gt = 2020)                #大于2020
'''

表操作'''
多表操作
    添加记录
        一对多添加
            Book.objects.create(
                title = 'python',
                price = 12,
                publish_id = 1
                #publish = pub_obj   #前提：pub_obj = Publish.objects.filter(name = 'xxx').first()
            )
        多对多添加
            book = Book.objects.filter(id = 1).first()  #找到id等于1的书
            book.author.add(1,2)         #给他添加Author表中id等于1和2的作者
            book.author.remove(1)       #删除这本书的作者1
            book.author.clear()         #删除这本书所有作者
            book.author.set([1,2])      #重置这本书的作者为1和2,相当于先clear再add
    查询记录
        1.跨表查询
            -- 基于对象
                一对多
                    (1)查询属名为Linux的书的作者的名字和Email
                    book = Book.objects.filter(title = 'linux').first()
                    print(book.publish_id)
                    pub= Publish.objects.filter(id = book.publish_id).first()
                    print(pub.name,pub.email)
                    
                    (2)查询书名为Linux的书的出版社(正向查询)
                    publish = Book.objects.filter(title='linux').first().publish.name
                    print(publish)
                    
                    (3)查询清华出版社出版的所有的书(方向查询，表面__set)
                    pub_obj = Publish.objects.filter(name = '清华出版社').first()
                    lis = pub_obj.book_set.all().values('title')
                    print(lis)


                多对多
                    (1)查询书名为JavaScript的书的所有作者
                    book = Book.objects.filter(title = 'javaScript').first()
                    au = book.author.all()
                    for it in au:
                        print(it.name)
                    
                    (2)查询李四写的所有书(反向查询 表名__set)
                    au = Author.objects.filter(name = '李四').first()
                    lis = au.book_set.all().values('title')         #方向查询如果字段起了别名，可以用别名代替，表名加__set     lis = au.xxx.all()  
                    print(lis)


                一对一
                    (1)查询李四的电话
                    author = Author.objects.filter(name = '李四').first()
                    print(author.ad.tel)
                    
                    (2)查询电话为177的作者名字(反向查询 直接点表名)
                    ad_obj = AuthorDetail.objects.filter(tel = 177).first()
                    print(ad_obj.author.name)
            -- 基于双下划线
                (1)查询python基础的出版社名字
                    ret = Book.objects.filter(title = 'python基础').values('publish__name')
                    print(ret)
                   
                    ret = Publish.objects.filter(book__title='python').values('name')
                    print(ret)
                (2)查询人民出版社出版的所有书籍
                    ret = Publish.objects.filter(name='人民出版社').values('book__title')
                    print(ret)
    
                    ret = Book.objects.filter(publish__name='人民出版社').values('title')
                    print(ret)
            
                (3)查询python基础的作者的年龄
                    ret = Book.objects.filter(title='python基础').values('author__age')
                    print(ret)
    
                    ret = Author.objects.filter(book__title='python基础').values('age')
                    print(ret)
            
                (4)查询皮皮出版的所有书籍
                    ret = Book.objects.filter(author__name='皮皮').values('title')
                    print(ret)
    
                    ret = Author.objects.filter(name='皮皮').values('book__title')
                    print(ret)
            
                (5)查询皮皮的电话
                    ret = Author.objects.filter(name='皮皮').values('ad__tel')
                    print(ret)
                    
                    ret = AuthorDetail.objects.filter(author__name='皮皮').values('tel')
                    print(ret)
            
                (6)查询查询电话为177的作者的名字
                    ret = AuthorDetail.objects.filter(tel=177).values('author__name')
                    print(ret)
                    
                    ret = Author.objects.filter(ad__tel=177).values('name')
                    print(ret)
                
                (7)查询人民出版社出版的书和作者名字
                    ret = Publish.objects.filter(name='人民出版社').values_list('book__title','book__author__name')
                    print(ret)
                    
                    ret = Book.objects.filter(publish__name='人民出版社').values_list('title','author__name')
                    print(ret)
                    
                    ret = Author.objects.filter(book__publish__name='人民出版社').values_list('book__title','name')
                
                (8)查询电话以158开头的作者的书和书的出版社
                    ret = Author.objects.filter(ad__tel__startswith='158').values('book__title','book__publish__name')
                    print(ret)
                    
                    ret = AuthorDetail.objects.filter(tel__startswith='158').values_list('author__book__title','author__book__publish__name')
                    print(ret)
        2.分组查询
            from django.db.models import Avg,Max,Sum,Min,Count
            (1)计算所有的书籍
                ret = Book.objects.all().aggregate(c = Count('id'))
                print(ret)
            
            (2)以出版社分组，计算每个出版社出版的书籍个数
                # ret = Book.objects.values("publish_id").annotate(c = Count(1))
                # print(ret)
        
            #跨表
                (1)以出版社名称和和作者以及作者id分组，计算每个作者在出版社出的书
                    ret = Book.objects.values('publish__name','author__id','author__name').annotate(c = Count(1))
                    print(ret)
                    
                (2)以每个作者以及作者id分组，计算每个作者出的所有书籍以及出版最贵的书的价格
                    ret = Book.objects.values("author__name",'author').annotate(c=Count(1), d=Max('price'))
                    print(ret)
        
        
            # ret = Book.objects.values('author__id','author__name').annotate(d = Avg('price'))
            # print(ret)
            #
            # ret = Book.objects.annotate(d = Avg('price')).values('author__id','author__name','d')
            # print(ret)
        
            # ret = Book.objects.annotate(cou = Count('author__id')).values('title','cou').filter(cou__gt=1)
            # print(ret)
        
            # ret = Book.objects.values('author__name','author').annotate(c = Count(1)).filter(c__gt=1)
            # print(ret)
        3.F与Q查询
            from django.db.models import F,Q
            ret = Book.objects.all().filter(price__gt=F(字段))
            ret = Book.objects.filter((Q(price__gt=100) | ~Q(name="python")) & Q(author__name="李四"))        #或 |   非 ~   且 & (且可以用逗号表示,如果最外层嵌套用逗号表示且，那么Q函数要放最前面)
        补充
            q = Q()
            q.connector = "or"      #默认是且
            q.children.append(('name','xxx'),('sex','男'))
            User.objects.filter(q)
            
        '''


如果想打印转换过程中的sql，需要在settings中进行如下配置：'''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}　　
'''

取别名用法'''
class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50)
    age = models.IntegerField(verbose_name='年龄')

class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=100)
    author = models.ForeignKey(Author, verbose_name='作者', related_name='bs', related_query_name='b')






Author.objects.filter(b__name='learn_python')
#通过related_query_name查询书名为learn_python的作者
author = Author.objects.get(pk=1)
author.bs.all()
通过related_name来查询该作者所有的书

'''