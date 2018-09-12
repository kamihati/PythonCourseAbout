# coding=utf8

def sort_list_with_dict(student_list):
    return sorted(student_list, key=lambda x: x['score'], reverse=True)

def score_list_with_dict_2(student_list):
    return sorted(student_list, key=lambda x: x['detail']['score'], reverse=True)


if __name__ == "__main__":
    # 字典内无子字典
    student_1 = dict(name='杜舞雩', score=33)
    student_2 = dict(name='祸风行', score=44)
    student_3 = dict(name='一剑风徽', score=22)
    student_list = [student_1, student_2, student_3]

    result = sort_list_with_dict(student_list)
    print(result)

    # 字典内有子字典
    student_1 = dict(name='绮罗生', detail=dict(age=18, score=33))
    student_2 = dict(name='意琦行', detail=dict(age=22, score=44))
    student_3 = dict(name='最光阴', detail=dict(age=21, score=22))
    student_list = [student_1, student_2, student_3]
    result = score_list_with_dict_2(student_list)
    print(result)
