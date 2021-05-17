# AHA Smart Greenhouse Management System
Web高级开发课程小组项目，**AHA智慧大棚管理系统**
## 环境配置
本站点基于python3.9, Django3.2开发
### 1.下载安装Miniconda
Miniconda 是一个 Anaconda 的轻量级替代，默认只包含了 python 和 conda，但是可以通过 pip 和 conda 来安装所需要的包。   
Miniconda 安装包可以到 https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ 下载。   
通过修改用户目录下的 .condarc 文件更换包安装源，Windows 用户无法直接创建名为 .condarc 的文件，可先执行 conda config --set show_channel_urls yes 生成该文件之后再修改。   
```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
### 2.配置项目环境
```
# 下载项目文件到本地
git clone https://github.com/lemonxug/aha_greenhouse.git

# 使用conda创建虚拟环境
conda create --name aha python=3.9 --file requirements.txt

# 如果上述命令未成功创建虚拟环境，可以使用以下命令先创建环境，再使用pip安装相关包。
# 若运行站点时提示缺少相关库，同样可以使用pip进行安装。
conda create --name aha python=3.9
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django requests

# 激活环境
activate aha
```
### 3.启动站点
```
# 启动站点
python manage.py runserver
```
站点地址：http://127.0.0.1:8000/     
后台地址：http://127.0.0.1:8000/admin    
管理员账户：admin/admin   

## 初始化数据库
本项目使用的是sqlite数据库，如有需要可以更换为其他数据库。
### 1.使用MySQL数据库
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
### 2.导入数据
更换数据库后，可使用backup.sql导入测试数据
   
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

# sqlite3数据库备份
sqlite3 db.sqlite3 ".dump" > backup.sql   # 导出备份
sqlite3 db.sqlite3 < cache/backup.sql     # 导入备份
```