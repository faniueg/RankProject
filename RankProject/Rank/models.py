from django.db import models


class RankModels(models.Model):
    grade = models.IntegerField(null=True)  # 排名
    client = models.CharField(max_length=16, null=True)  # 客户端
    fraction = models.IntegerField(null=True)  # 分数
