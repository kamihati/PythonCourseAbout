from django.db import models

import os
from django.conf import settings



# 把此函数设置到FileField字段的upload_to字段中则自动传入当前实例和文件名
def get_portaint_path(instance, filename):
    # 文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class PollMan(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    # 被传到`MEDIA_ROOT/uploads/2018/11/3`目录，增加了一个时间划分
    file_one = models.FileField(upload_to='upload/%Y/%m/%d/')
    portaint = models.FileField(upload_to=get_portaint_path)

