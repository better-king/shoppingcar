import copy

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


# 打印当前库存的商品信息
def showlist(goods_list):
    print('%-8s%-8s%-8s%-8s'%('序号','商品名','价格','余量'))
    for i in goods_list:                             # 这个循环列出商品信息
        num = goods_list.index(i)+1
        print('%-10d%-10s%-10d%-10d' % (num, i[0], int(i[1]), int(i[2])))


# 更新商品信息文件
def write_list(new_list):
    f = open('goods_list.txt', 'w')
    for i in new_list:
        newline = i[0]+','+i[1]+','+i[2]+'\n'
        f.writelines(newline)
    f.close()


def change():
    goods_list = get_list()
    change_list = copy.deepcopy(goods_list)
    while True:
        showlist(change_list)
        chioce1 = int(input('请选择：0、返回上一级  1、单个商品修改  2、批量修改'))
        if chioce1 == 0:
            break
        elif chioce1 == 1:
            c1 = int(input('请输入想修改的商品序号：'))
            c2 = 1
            while c2 != 0:
                c2 = int(input('请输入0完成修改，或者选择修改项目：1、商品名称  2、商品单价  3、余量 '))
                if c2 == 1:
                    change_list[c1-1][c2-1] = input('请输入新的商品名称：')
                elif c2 == 2:
                    change_list[c1 - 1][c2 - 1] = input('请输入新的商品单价：')
                elif c2 == 3:
                    change_list[c1 - 1][c2 - 1] = input('请输入新的商品余量：')
        elif chioce1 == 2:
            p1 = input('请输入想修改的商品序号，并在各序号之间用逗号隔开(请使用英文输入法的逗号)：')
            num = p1.split(',')
            p2 = 1
            while p2 != 0:
                p2 = int(input('请输入0完成修改，或者输入想批量修改的项：1、商品单价  2、商品余量'))
                if p2 == 1:
                    new1 = input('请输入新的商品单价：')
                    for i in num:
                        i = int(i)
                        change_list[i-1][p2] = new1
                if p2 == 2:
                    new2 = input('请输入新的商品余量：')
                    for i in num:
                        i = int(i)
                        change_list[i - 1][p2] = new2
        else: print('输入错误')
    if goods_list != change_list:
        print('/----------------------------------\***************\------------------------------------/')
        print('修改前：')
        showlist(goods_list)
        print('修改后：')
        showlist(change_list)
        chioce2 = input('是否保存此次修改？ 1、保存修改   2、不保存修改：')
        if chioce2 == '1':
            write_list(change_list)
            print('保存成功!')


def add_goods():
    goods_list = get_list()
    change_list = copy.deepcopy(goods_list)
    add_list = []
    while True:
        showlist(change_list)
        chioce1 = input('请选择：0、返回上一级  1、上架商品 ')
        if chioce1 == '0':
            break
        elif chioce1 == '1':
            c1 = input('请输入0取消上架商品，或者输入上架商品名称：')
            if c1 != '0':
                c2 = input('请输入0取消上架商品，或者输入上架商品单价：')
                if c2 != '0':
                    c3 = input('请输入0取消上架商品，或者输入上架商品余量：')
                    if c3 != '0':
                        new = [c1,c2,c3]
                        add_list.append(new)
                        change_list.append(new)
    if goods_list != change_list:
        print('/----------------------------------\***************\------------------------------------/')
        print('此次上架商品列表如下：')
        showlist(add_list)
        chioce2 = input('是否保存此次修改？ 1、保存修改   2、不保存修改：')
        if chioce2 == '1':
            write_list(change_list)
            print('保存成功!')


def del_goods():
    goods_list = get_list()
    change_list = copy.deepcopy(goods_list)
    del_list = []
    while True:
        showlist(change_list)
        chioce1 = input('请选择：0、返回上一级  1、下架商品 ')
        if chioce1 == '0':
            break
        elif chioce1 == '1':
            c1 = int(input('请输入想要下架的商品序号：'))
            print('即将下架此项商品：')
            print('商品名称：%s  商品单价：%s  商品余量：%s'%(change_list[c1-1][0],change_list[c1-1][1],change_list[c1-1][2]))
            c2 = input('请问是否确定：1、确定下架  2、取消下架')
            if c2 == '1':
                del_list.append(change_list[c1-1])
                del change_list[c1-1]
    if goods_list != change_list:
        print('/----------------------------------\***************\------------------------------------/')
        print('此次将下架以下商品：')
        showlist(del_list)
        chioce2 = input('是否保存此次修改？ 1、保存修改   2、不保存修改：')
        if chioce2 == '1':
            write_list(change_list)
            print('保存成功!')


def business():
    print('恭喜你登录成功')
    while True:
        print('/----------------------------------\欢迎光临XXX商城\------------------------------------/')
        chioce = input('请选择：0、退出程序 1、修改商品信息（包括余量与单价）  2、上架货物  3、下架货物：')
        if chioce == '1':
            change()
        elif chioce == '2':
            add_goods()
        elif chioce == '3':
            del_goods()
        elif chioce == '0':
            exit()
        else:
            print('输入错误，请重新输入')
