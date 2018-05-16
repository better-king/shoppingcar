import myfile.customer
import myfile.business


# 注册函数
def sign_up():
    userdata = open("userdata.txt",'a+')
    username = input("请设定您的用户名:")
    password = input("请设定您的密码:")
    userdata.writelines(username+','+password+',0\n')       # 这里的0就是用户余额
    userdata.close()
    print(username,password)
    print("恭喜你完成了注册!\n")
    return username


# 登录函数
def sign_in(name, password):
    userdata = []
    f = open("userdata.txt",'r')
    readlines = f.readlines()
    for userline in readlines:
        userdata = userline.split(",")
        username = userdata[0]
        userpassword = userdata[1]
        balance = int(userdata[2].strip("\n"))
        if name == username:
            if password == userpassword:              # 情况1：登录成功
                return [1,username,balance]
            elif password != userpassword:            # 情况2：密码输入错误
                return [2,0,0]
    else:                                             # 情况3：找不到该用户
        return [0,0,0]
    f.close()


while True:
    choice1 = input("您好，请选择：1、商家登录  2、客户登录  3、客户注册 4、退出程序: ")
    if choice1 == "1":
        b_password = '123456'
        word = input("请输入商家登录密码：")
        if word == '123456':
            myfile.business.business()
        else:
            print('密码错误')
    elif choice1 == "2":
        username = input("请输入用户名：")
        password = input("请输入密码：")
        flag = 2
        while flag != 1:
            flag, user, balance = sign_in(username, password)
            if flag == "2":
                print("密码错误，请重新输入")
            elif flag == '3':
                print("找不到该用户")
            else:
                myfile.customer.customer(user, balance)
    elif choice1 == "3":
        user = sign_up()
        balance = 0
        myfile.customer.customer(user, balance)
    elif choice1 == "4":
        exit()
    else:
        print("输入错误，请重新输入")
