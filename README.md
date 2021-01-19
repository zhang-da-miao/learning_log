# study note 
这是一个用django框架编写的学习笔记。  
实现功能：注册，用户登陆登出，编辑、添加notes和topic并与对应用户绑定。
***

### 待办事项
####缺陷  
users模块
- [x] 1.注册功能未正常运行(2021.1.19)
- [x] 2.注册网页模版没有在正确的位置(2021.1.19)

####功能预告  
users模块
- [ ] 1.第三方登陆
- [ ] 2.用户资料
- [ ] 3.用户头像

learning_logs模块
- [ ] 1.评论功能
- [ ] 2.点赞功能

### 目录结构
```
├── README.md
├── db.sqlite3
├── learning_log
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── utils.py
│   └── wsgi.py
├── learning_logs
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── templates
│   ├── base.html
│   ├── edit_entry.html
│   ├── index.html
│   ├── new_entry.html
│   ├── new_topic.html
│   ├── topic.html
│   ├── topics.html
│   └── users
│       ├── login.html
│       └── register.html
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```