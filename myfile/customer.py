# 从商品文件中读出商品列表，并做初步处理
def get_list():
    f = open('goods_list.txt','r')
    lines = f.readlines()
    f.close()
    for i in lines:
        line = i.split(",")
        line[2] = line[-1].strip("\n")
        lines[lines.index(i)] = line
    return lines


# 把商品文件更新
def write_list(good_list):
    f = open('goods_list.txt','w')
    for i in good_list:
        f.writelines(i[0]+','+i[1]+','+str(i[2])+'\n')
    f.close()


# 把用户余额更新
def write_user(username,balance):
    f0 = open('userdata.txt', 'r')
    lines = f0.readlines()
    f0.close()
    f1 = open('userdata.txt', 'w')
    n = 0  # 索引变量
    for line in lines:  # 查找出对应的用户名在lines列表中的索引
        userline = line.split(",")
        if username == userline[0]:
            n = lines.index(line)
            break
    name = userline[0]
    password = userline[1]
    u_balance = balance
    new = name + "," + password + "," + str(u_balance) + "\n"
    lines[n] = new  # 把该元素更新
    for i in lines:
        f1.writelines(i)  # 把lines列表重新写入userdata.txt文件中
    f1.close()


# 购物函数
def shopping(goods_list,shopping_list,balance):          # 参数：商品列表、购物车列表、余额
    if len(goods_list) == 0:
        goods_list = get_list()                          # 从文件读出商品列表
    while True:
        print('%-8s%-8s%-8s%-8s'%('序号','商品名','价格','余量'))
        for i in goods_list:                             # 这个循环列出商品信息
            num = goods_list.index(i)+1
            print('%-10d%-10s%-10d%-10d' % (num, i[0], int(i[1]), int(i[2])))
        goods = int(input('请输入0退出购物，输入-1查看当前购物车，或输入欲购买的商品序号：'))
        if goods != 0 and goods != -1:
            if goods <= num:                              # 判断是否超过商品列表最大序号
                number = int(input('请输入0取消购买，或者输入欲购买的商品数量：'))
                if number != 0 :
                    if number > int(goods_list[goods-1][2]):     # 判断购买数量是否超过商品余量,若超过则按最大余量
                        number = int(goods_list[goods-1][2])
                    if balance > int(goods_list[goods-1][1]) * number:   # 判断余额是否足够
                        buy = [goods_list[goods-1][0],number]
                        shopping_list.append(buy)
                        goods_list[goods - 1][2] = int(goods_list[goods-1][2]) - number
                        balance = balance - int(goods_list[goods-1][1]) * number
                    else :
                        print("余额不足，无法加入购物车")
            else:
                print('输入错误，请重新输入')
        elif goods == -1:
            if len(shopping_list):
                for i in shopping_list:
                    print(i[0] + ',' + '数量：' + str(i[1]) + '\n')
            else: print('当前购物车为空')
        else: break
    return (goods_list,shopping_list,balance)


# 充值函数
def recharge(user,balance):
    money = int(input("请输入充值金额："))
    if money >= 0:
        balance += money
    print("恭喜你充值成功，现在余额为："+ str(balance))
    write_user(user,balance)
    return balance


# 客户接口
def customer(user, balance):
    print('欢迎' + user + ',' + '您的当前余额为：' + str(balance))
    shopping_list = []
    goods_list = []
    while True:
        print('/----------------------------------\欢迎光临XXX商城\------------------------------------/')
        c_choice1 = input('请选择：1、购物  2、充值  3、退出：')
        if c_choice1 == '1':
            goods_list,shopping_list,balance = shopping(goods_list,shopping_list,balance)
        elif c_choice1 == '2':
            balance = recharge(user,balance)
        elif c_choice1 == '3':
            if len(shopping_list):                   #判断购物车是否有东西
                print('当前购物车：\n')
                for i in shopping_list:
                    print(i[0] + ',' + '数量：' + str(i[1]) + '\n')
                flag = input("购物车不为空，请问是否结账退出：1、结账 2、不结账直接退出：")
                if flag == '1':
                    print("恭喜您，已购买商品：")
                    for i in shopping_list:
                        print(i[0] + ',' + '数量：' + str(i[1])+'\n')
                    print('当前余额：'+ str(balance))
                    write_list(goods_list)               # 变更文件
                    write_user(user,balance)
                    exit()
            else:
                exit()
        else :
            print("输入错误，请重新输入")
