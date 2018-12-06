# coding=utf8



# 当前登录用户
login_user = None


def show_command(re_input=False):
    """
    显示命令列表
    :param re_input: 是否是重新输入命令。为 True则不显示命令列表
    :return:输入的命令正确时返回此值
    """
    cmd_list = []
    # 根据是否登录决定命令列表的内容
    if login_user is None:
        pass
    else:
        pass
    
    # 根据是否重新输入命令来决定是否显示命令列表
    if not re_input:
        for i in range(len(cmd_list)):
            print("%s:%s" % (i + 1, cmd_list[i]))
        
    cmd = input("请输入您要执行的命令：")
    
    # 命令的有效性校验
    if not cmd.isdigit():
        print("请输入正确的命令.")
        return show_command(True)
    else:
        cmd = int(cmd)
        if cmd < len(cmd_list) or cmd > len(cmd_list):
            print("请输入正确的命令..")
            return show_command(True)
        return cmd



