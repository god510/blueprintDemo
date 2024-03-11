# 在Flask中使用蓝图
在Flask中使用蓝图（Blueprints）可以让你在不同的文件中定义路由，然后在应用的__init__.py文件中将它们组合起来。这样做可以让你的应用更加模块化，易于管理和扩展。

#首先，你会有一个项目结构类似于这样：
```
/yourapp
    /blueprints
        /home
            __init__.py
            views.py
        /admin
            __init__.py
            views.py
    __init__.py
    app.py

```

在每个蓝图的目录中，你会有一个__init__.py文件和一个views.py文件。__init__.py文件定义了蓝图，而views.py文件包含了路由和视图函数。


# 创建虚拟环境
python -m venv env 

# 激活虚拟环境
 & .\env\Scripts\Activate.ps1

# 安装flask
pip install flask  -i  https://pypi.org/simple/

