# 常用命令
conda create -n django
conda activate django
pip install django
django-admin startproject djangosite # 新建项目
python manage.py startapp blog # 新建APP
python manage.py runserver 8080 #启动

python manage.py makemigrations
python manage.py migrate

python manage.py flush # 清空数据库
python manage.py createsuperuser # 创建管理员
python manage.py changepassword username # 修改用户密码

python manage.py shell # Django项目环境终端
你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据的测试非常方便。
python manage.py # 查看更多关于Django的命令在终端输入

# 数据模型字段及属性
1、AutoField   ---自增列 = int(11)    如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、CharField   ---字符串字段  单行输入，用于较短的字符串，如要保存大量文本, 使用 TextField。必须 max_length 参数，django会根据这个参数在数据库层和校验层限制该字段所允许的最大字符数。
3、BooleanField   ---布尔类型=tinyint(1)   不能为空，Blank=True
4、ComaSeparatedIntegerField   ---用逗号分割的数字=varchar   继承CharField，所以必须 max_lenght 参数，
5、DateField   ---日期类型 date   对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、DateTimeField   ---日期类型 datetime   同DateField的参数
7、Decimal   ---十进制小数类型 = decimal   必须指定整数位max_digits和小数位decimal_places
8、EmailField   ---字符串类型（正则表达式邮箱） =varchar   对字符串进行正则表达式   一个带有检查 Email 合法性的 CharField，不接受 maxlength 参数。
9、FloatField   ---浮点类型 = double   浮点型字段。 必须提供两个 参数， 参数描述：
max_digits：总位数(不包括小数点和符号）
decimal_places：小数位数。如：要保存最大值为 999 (小数点后保存2位)，你要这样定义字段：FloatField(…，max_digits=5， decimal_places=2)，要保存最大值一百万(小数点后保存10位)的话，你要这样定义：FloatField(…，max_digits=19， decimal_places=10)
10、IntegerField   ---整形   用于保存一个整数

1、null   数据库中字段是否可以为空（null=True）
2、db_column  数据库中字段的列名(db_column="test")
3、db_tablespace
4、default  数据库中字段的默认值
5、primary_key  数据库中字段是否为主键(primary_key=True)
6、db_index  数据库中字段是否可以建立索引(db_index=True)
7、unique  数据库中字段是否可以建立唯一索引(unique=True)
8、unique_for_date  数据库中字段【日期】部分是否可以建立唯一索引
9、unique_for_month  数据库中字段【月】部分是否可以建立唯一索引
10、unique_for_year  数据库中字段【年】部分是否可以建立唯一索引
11、auto_now  更新时自动更新当前时间
12、auto_now_add  创建时自动更新当前时间
13、verbose_name  Admin中显示的字段名称
14、blankAdmin  中是否允许用户输入为空表单提交时可以为空
15、editableAdmin  中是否可以编辑
16、help_textAdmin  中该字段的提示信息
17、choicesAdmin  中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作

# QuerySet API
<1>all():         查询所有结果
<2>filter(**kwargs)    它包含了与所给筛选条件相匹配的对象
<3>get(**kwargs):     返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
<4>exclude(**kwargs)    它包含了与所给筛选条件不匹配的对象
<5>values(*field)     返回一个ValueQuerySet 一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
<6>values_list(*field)   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
<7>order_by(*field)    对查询结果排序
<8>reverse()        对查询结果反向排序
<9>distinct()       从返回结果中剔除重复纪录
<10>count()        返回数据库中匹配查询(QuerySet)的对象数量。
<11>first()        返回第一条记录
<12>last()         返回最后一条记录
<13>exists()        如果QuerySet包含数据，就返回True，否则返回False
<14>annotate()       使用聚合函数
<15>dates()        根据日期获取查询集
<16>datetimes()      根据时间获取查询集
<17>none()         创建空的查询集
<18>union()        并集
<19>intersection()     交集
<21>difference()      差集
<22>select_related()    附带查询关联对象
<23>prefetch_related()   预先查询
<24>extra()        附加SQL查询
<25>defer()        不加载指定字段
<26>only()         只加载指定的字段
<27>using()        选择数据库
<28>select_for_update()  锁住选择的对象，直到事务结束。only
<29>raw()         接收一个原始的SQL查询

# ORM QuerySet查询
from django.db.models import Avg, Max, Min, Count, Sum
res = models.Publish.objects.values("name").annotate(in_price = Min("book__price"))
print(res)
模板
Django模板存放方式有两种方法：
1、在项目根下创建templates目录，然后把模板存入在templates目录里，多个APP的话，就直接在templates目录下建立与APP名相同名称的目录即可。Django会自动查找到，这种方法简单、直观，适合个人或小项目。
2、各个APP下单独建立一个templates目录，然后再建立一个与项目名相同的的目录，把模板放到对应的目录里。这样的方法适合大项目多人协作，每个人只负责各自的APP项目的时候。多样式多站点(域名)的情况也适用，不同的APP用不同的模板样式，不同的域名。
两种方法，模板调用方法一样：
return render(request, 'app/index.html', context)

# 模板语言
字段
{{ object.headline }}
{{ now|date }}

列表
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}

字典
{% for key,values in mydict.items  %}
<li>{{ key }}：{{ values }}</li>
{% endfor %}

if
{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

模板包含
{% include 'head.html' %}
<div>中部</div>
{% include 'footer.html' %}

模板继承
{% extends "base.html" %}

block
{% block content %}
<div>中部</div>
{% endblock %}

载入静态文件
{% load static %}

为 URL 名称添加命名空间
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>