**CMDB**

    使用python的 django 框架研发，所用python 版本 3.4, django 版本 1.10.6
    

**安装/运行**

    1. 安装 python >= 3.4
    
    2. git clone https://github.com/charlesxs/cmdb.git && cd cmdb
    
    3. pip install -r requirements.txt
    
    4. mysql 创建 cmdb 数据库 和授权账户
        
        例子:
        
            mysql> create database default charset 'utf8';
            
            mysql> grant all on cmdb.* to cmdb@'127.0.0.1' identified by 'xxxxxxx';
    
    5. 修改 cmdb/settings.py ， 修改数据库的用户名和密码
    
    6. python manage.py makemigrations && python manage.py migrate
    
    7. 导入初始化数据 （内部包含有一点点测试数据）
    
        mysql -uroot cmdb < sql/cmdb.sql
        
        初始化 用户: admin 密码: admin
    
    8. python manage.py runserver 0.0.0.0:8000
    
    
**使用**

_添加服务器_

![addserver](/../screenshots/screenshots/addserver-001.png)

![addserver](/../screenshots/screenshots/addserver-002.png)


_添加网络资产_

![addserver](/../screenshots/screenshots/addnetwork-001.png)


_资产列表_

![addserver](/../screenshots/screenshots/asset_list-001.png)

_资产详情页_

![addserver](/../screenshots/screenshots/detail-001.png)


_机房_

![addserver](/../screenshots/screenshots/idc-001.png)

_机房视图_

![view](/../screenshots/screenshots/view-001.png)


_业务管理_

![addserver](/../screenshots/screenshots/user-001.png)


