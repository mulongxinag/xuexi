# 数据库图形管理工具
"""
## 常见数据库图形管理工具
1.navicat系列    navicat for sqlite
优点navicatForMysql用户多 表多的时候界面方便，缺点一是付费而二是体验一般。
2.datagrip    ,jetbrains出品，优点一个软件链接多个数据库；操作习惯跟pycharm类似；pycharm pro集成。缺点用户少；驱动不好下。

"""


"""
(了解）datagrip操作方法 （pycharm集成database工具为例子）：
1.pycharm左下角图标调出工具栏，打开pycharm右侧Database工具。
2.点加号-DataSource数据源-sqlite 。
3.弹出的对话框选择 drivers-sqlite（Xerial)
4.点击download sqlite-jdbc[latest]
5.如果网速不好的话 下载sqlite-jdbc-3.20.1.jar。对话框+号-custom jars 从本地安装
6.驱动安装成功后点击apply应用
7.点击对话框 project data source，开始配置连接数据库的实例
8.File路径点击...图标，选择要连接的.db文件。 
9.点test connection, successful为成功
10.点击OK退出。看到连接的数据库实例下有表。


（了解）
JDBC:Java操作数据库的驱动包。因为pycharm、datagr是用Java开发的。
"""
