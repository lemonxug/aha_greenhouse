# AHA Smart Greenhouse Management System
Web高级开发课程最终项目，AHA智慧大棚管理系统
## 环境配置
python3.7, Django3.2
为了方便，MySQL和PHPMyadmin使用docker部署

```
# 使用conda创建虚拟环境
conda create --name smart_greenhouse python=3.7 --file requirements.txt

# 部分包不能自动安装，可以先创建环境，手动安装
pip install django django-redis django-tinymce  mysqlclient==1.4.4

# 激活环境
activate smart_greenhouse

# docker启动MySQL
docker run -d --rm --name mysql -v /D/MySQL:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root  mysql
# docker启动PHPMyadmin
docker run -d --rm --name phpmyadmin -p 8080:80 --link mysql:db phpmyadmin/phpmyadmin

# 启动站点
python manage.py runserver
```
## 魔改大法
to be done