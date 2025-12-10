# # + 直接字符串外+变量
# name = 'zheng'
# print('my name is '+name)
# # % 直接字符串外%(变量)
# name = 'zhang'
# age = 25
# print('my name is %s'%(name)+' my age is %d'%(age))
# # format()函数
# name = input('请输入你的名字：')
# data = input('请输入发送内容：')
# dest_ip = input('请输入ip：')
# dest_port = 2425
# chat_socket.sendto('1:123456:发送者的名称:{my_name}:32:{my_data}'.format(my_name=name,my_data=data).encode('gbk'),(dest_ip,dest_port))