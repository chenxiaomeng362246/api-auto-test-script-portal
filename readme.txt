晓猛笔记
一、项目介绍
1.运行项目要在python2.7 上
2.修改项目路径下的venv->lib->orig-prefix.txt 内容为本电脑安装的python 解释器的路径
3.选择File->settings->Python Interpreter->选择当前在项目内部的虚拟环境，
内部虚拟环境已经安装了依赖包ndlib-3.3.16 ，放在文件夹lib上 运行命令，如果使用local本地环境
则需要对依赖包cd到解压后路径,python setup.py install，安装才能调用相关组件

2.pip install rsa
  pip install ddt

3.对应的运行计划地址是
https://bamboo.prometheanjira.com/browse/RL-LSAD-431

4.启动项目的命令python runner.py 测试用例名字(这个是运行开发环境的用例)

5、测试目录相关说明
api-auto-test-script-portal
api_call      【接口信息】
config        【常量配置】
--production
---config
----cfg.ini    常量数据 接口测试的URL地址配置[dev]    [sandbox]     [staging]   [pro]   [prod]
----gbl.py     设置页面encoding默认utf-8，把ini文件里面的url赋值给常量DEV SANDBOX STAGING

data_struct    【数据提供】一些变量数据，一些随机生成数据的方法

runner         【运行驱动】
--runner.py    取当前文件的绝对路径 run当前的文件
--suites.json  配置要运行的接口测试用例名字，用到的要运行的testcase里面写的测试用例代码


test_reports   生成的测试报告
testcases      与前面api相关的接口调用，当前测试用例相关编写，包括code断言和返回值的简单业务断言
util           公共方法提取/http状态码宏定义/数据宏定义/数据类公共方法
--txt_opera  一些接口使用的公共类，如登录后把cookie、token等一些数据写到txt文件当中，后续方法需要使用的时候再读取出来
              可以使用相对路径把读取AuthorizationToken数据存放到指定的位置









