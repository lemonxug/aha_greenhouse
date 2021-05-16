# AHA Smart Greenhouse Management System
Web高级开发课程小组项目，**AHA智慧大棚管理系统**
## 环境配置
本站点基于python3.9, Django3.2开发

```
# 下载项目文件到本地
git clone https://github.com/lemonxug/aha_greenhouse.git

# 使用conda创建虚拟环境
conda create --name aha python=3.9 --file requirements.txt

# 激活环境
activate aha
```
## 启动站点
```
# 启动站点
python manage.py runserver
```
站点地址：http://127.0.0.1:8000/     
后台地址：http://127.0.0.1:8000/admin    
管理员账户：admin/admin   

## 初始化觳觫库
1. 使用MySQL数据库
```
settings.py
将以下配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20
        }
    }
}
修改为：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'greenhouse',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```
2. 导入数据
使用backup.sql导入数据
   
## Django开发常用命令
```
conda create -n django   # 新建虚拟环境
conda activate django    # 激活环境
pip install django       # 安装django

django-admin startproject djangosite # 新建项目
python manage.py startapp blog # 新建APP
python manage.py runserver 8080 #启动

python manage.py makemigrations  # 数据库迁移
python manage.py migrate   # 数据库迁移

python manage.py flush # 清空数据库
python manage.py createsuperuser # 创建管理员
python manage.py changepassword username # 修改用户密码

python manage.py shell # Django项目环境终端，
你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据的测试非常方便。

python manage.py # 查看更多关于Django的命令在终端输入

# sqlite3备份数据库
sqlite3 db.sqlite3 ".dump" > backup.sql   # 导出备份
sqlite3 db.sqlite3 < cache/backup.sql     # 导入备份
```