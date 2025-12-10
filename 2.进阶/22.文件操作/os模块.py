# os模块下常用操作文件的方法
# #TODO:remove(path)	                    删除指定的文件
# #TODO:rename(src,dest)	                重命名文件或目录
# #TODO:stat(path)	                    返回文件的所有属性
# #TODO:listdir(path)	                    返回path目录下的文件和目录列表
# os模块下关于目录操作的相关方法
# #TODO:mkdir(path)	                    创建目录
# #TODO:makedirs(path1/path2/path3/...)	创建多级目录
# #TODO:rmdir(path)	                    删除目录
# #TODO:removedirs(path1/path2...)	    删除多级目录
# #TODO:getcwd()	                        返回当前工作目录：current work dir
# #TODO:chdir(path)	                    把path设为当前工作目录
# #TODO:walk()	                        遍历目录树
# sep	                            当前操作系统所使用的路径分隔符
# os.path模块_常用方法
# #TODO:isabs(path)	                    判断path是否绝对路径
# #TODO:isdir(path)	                    判断path是否为目录
# #TODO:isfile(path)	                    判断path是否为文件
# #TODO:exists(path)	                    判断指定路径的文件是否存在
# #TODO:getsize(filename)	                返回文件的大小
# #TODO:abspath(path)	                    返回绝对路径
# #TODO:dirname(p)	                    返回目录的路径
# #TODO:getatime(filename)	            返回文件的最后访问时间
# #TODO:getmtime(filename)	            返回文件的最后修改时间
# #TODO:walk(top,func,arg)	            递归方式遍历目录
# #TODO:join(path,*paths)	                连接多个path
# #TODO:split(path)	                    对路径进行分割，以列表形式返回
# #TODO:splitext(path)	                从路径中分割文件的扩展名
import os

# path = os.getcwd()
path = "D:\Python"
for root, pathdir, files in os.walk(path, topdown=False):
    print(root+'\n', end='>>>')
    for j in files:
        dirs = root + '\\' + j
        print(dirs+'\n', end='>>>')

