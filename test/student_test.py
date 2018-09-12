# coding=utf8
import os
import sys
import json
import time
import arrow
test_result = []

# 正确答案
# 例子：第一大题每题2分。共5小题。正确答案依次为ABCDE
# 第二大题每题3分。共4小题。正确答案依次为BCDE
# answers = [[2, (A, B, C, D, E)], [3, (B, C, D, E)]]
answers = ['A', 'B', 'C', 'B', 'A', 'A', 'C', 'A', 'C', 'B', 'B', 'C', 'B', 'B', 'C', 'C', 'B',
           'C', 'C', 'B', 'B', 'B', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'C', 'A', 'B', 'B', 'A', 'A', 'B']

score = dict()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
F_PATH = os.path.join(BASE_DIR, 'score.json')# % arrow.Arrow.now().format("YYYYMMDDHHmmss"))


def save_test(name, answer):
    """
    保存成绩.写入到文件
    :param name:
    :param answer:
    :return:
    """
    if '\n' in answer:
        answer.remove("\n")
    if name in score:
        print("%s已存在。总分数为:%s" % (name, score[name]['total']))
        return False
    elif len(answer) != len(answers):
        print(answer)
        print(answers)
        print("%s的答题记录与题目数量不符.true:%s,false:%s。不予记录" % (name, len(answers), len(answer)))
        return False
    else:
        score[name] = dict(answer=answer)
        # 错误记录结构为[dict('index': 0, '')(题号,错误答案,正确答案)]
        score[name]['error'] = []
        # 总分数
        result = 0
        for i in range(len(answers)):
            if answers[i].upper() == answer[i].upper():
                result += 2
            else:
                score[name]['error'].append(i + 1)
                # score[name]['error'].append(dict(index=i, mistake=answer[i], currect=answers[i]))
        score[name]['total'] = result
        with open(F_PATH, 'w+', encoding='utf8') as f:
            f.write(json.dumps(score).encode("utf8").decode("unicode_escape"))
        return True


def read_data():
    with open(os.path.join(BASE_DIR, 'data.json'), 'r', encoding='utf8') as f:
        for line in f.readlines():
            print(line)
            name, answer = line.split(',')
            save_test(name, list(answer))
    print("文件读取完毕")


def show_cmd():
    print('1.添加学生成绩')
    print('2.查看学生成绩')
    print('3.退出')
    print("4.读取data.txt")
    return input('请输入功能前的序号:')
    

def show_score(name=None):
    """
    查看学生成绩
    :param name:
    :return:
    """
    if name:
        if name not in score:
            print("%s未录入成绩" % name)
        else:
            print("%s的成绩为: %s, 做错%s道题:%s" % (name, score[name]["total"], len(score[name]['error']), score[name]['error']))
    else:
        for k, v in score.items():
            print("%s的成绩为%s,做错%s道题:%s" % (k, v['total'], len(v['error']), v['error']))
        print('学生成绩输出完毕。共有学生(%s)人' % len(score))
    input("press any key to continue...")
    

def init_input(cmd=None):
    """
    命令处理程序
    :param cmd:
    :return:
    """
    
    if not cmd:
        cmd = int(show_cmd())
    if cmd not in (1, 2, 3, 4):
        print("命令有误。请重新输入")
    elif cmd == 3:
        # print("3秒后将退出程序")
        # for i in range(3):
        #    print(3 - i)
        #    time.sleep(1)
        sys.exit()
    elif cmd == 2:
        # 查看成绩
        show_score()
    elif cmd == 1:
        # 保存成绩
        arg = input("请输入学生姓名与成绩。使用半角逗号分隔。如：姓名,AABBCDEFGGS，答案数量需要与题量一致:")
        name, answer = arg.split(',')
        if save_test(name, list(answer)):
            print("保存成功。%s的分为%s" % (name, score[name]['total']))
    elif cmd == 4:
        read_data()
    
    init_input()
    

if __name__ == "__main__":
    print(F_PATH)
    init_input()
