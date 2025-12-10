# # os模块是与操作系统交互
# ## 导入模块
# ## 获取当前工作目录
# os.getcwd()
# ## 改变当前脚本工作目录
# os.chdir("dirname")
# ## 返回当前目录
# os.curdir
# ## 获取当前目录的父目录字符串名
# os.pardir
# ## 一个dictionary包含环境变量的映射关系
# os.environ
# ## 显示当前使用的平台
# os.name
# ## 显示当前平台下路径分隔符
# os.sep
# ## 显示当前平台下使用的行终止符
# os.linesep
# ## 删除一个文件
# os.remove("filename")
# ## 重命名一个文件
# os.rename("oldname","newname")
# ## 返回指定目录下的所有文件和目录名
# os.listdir('dirname')
# ## 可生成多层递归目录
# os.makedirs('dirname/dirname')
# ## 删除单级目录
# os.rmdir('dirname')
# ## 得到用户登录名称
# os.getlogin()
# ## 得到环境变量配置
# os.getenv('key')
# ## 设置环境变量
# os.putenv('key')
# ## 用于运行shell命令，打开的是一个新的shell，运行命令，当命令结束，关闭shell

# ## os.path编写平台无关的程序
# ## 获取绝对路径
# os.path.abspath()
# ## 用于分开一个目录名称中的目录部分和文件名称部分
# os.path.split()
# ## 连接目录与文件名
# os.path.join(path,name)
# ## 返回文件名
# os.path.basename(path)
# ## 返回文件路径
# os.path.dirname(path)
# ## 创建文件的时间戳
# os.path.getctime("/root/1.txt")
# ## 判断文件是否存在
# os.path.exists(os.getcwd())
# ## 判断是否是文件名/目录/符号链接/文件系统安装点/同一文件/，1/0
# os.path.isfile(os.getcwd())
# os.path.isdir('c:\py')
# os.path.islink('/homw/111.sql')
# os.path.ismount(os.getcwd())
# os.path.samefile(os.getcwd,'/home')
# ## 给定目录下下的所有文件和目录都遍历一下
# os.path.walk('/home/huaging',test_fun,"a.c")
# os.walk(top,topdown=True,onerror=True)