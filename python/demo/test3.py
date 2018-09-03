# coding=utf8


list_command = ['查看菜单', '退出']
list_1 = ['开封菜', '越南菜', '陕西菜']


def view_list():
    for i in range(len(list_1)):
        print('%s:%s' % (i, list_1[i]))
    print("%s:%s" % (len(list_1), '返回'))
    command = int(input("请输入命令:"))
    
    if command < len(list_1):
        print("您点了：", list_1[command])
        input("输入任意键返回主菜单")
    view_init()


def view_init():
    for i in range(len(list_command)):
        print('%s:%s' % (i, list_command[i]))
    command = int(input("请输入命令序号:"))
    if command == 1:
        import sys
        input('press any key to exit')
        sys.exit(1)
    else:
        view_list()


if __name__ == "__main__":
    view_init()
