print('----- 欢迎进入通讯录程序 ------')
print('-----  1:查询联系人资料  ------')
print('-----  2:插入联系人资料  ------')
print('-----  3:删除联系人资料  ------')
print('-----  4:退出通讯录程序  ------')
address_list = dict()
while 1:
    temp = int(input('请输入相关指令代码:'))
    if temp == 1:
        name = input('请输入联系人姓名:')
        if name in address_list:
            print(name + ':' + address_list[name])
        else:
            print('您输入的名字不在通讯录中')
    if temp == 2:
        name = input('请输入联系人姓名:')
        if name in address_list:
            print('您输入的姓名在通讯录中已存在'+ name+':'+address_list[name])
            if input('是否修改用户资料(YES/NO):')==YES:
                address_list[name] = input('请输入用户联系电话:')
        else:
            address_list[name] = input('请输入用户联系电话:')
    if temp == 3:
        del(address_list[name])
    if temp == 4:
        print('----感谢您使用通讯录程序----')
        break
