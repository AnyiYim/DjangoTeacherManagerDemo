from django.db import models

# Create your models here.


class Classes(models.Model):
    # 班级表
    title = models.CharField(max_length=32)
    a = models.ManyToManyField('Teachers')
    objects = models.Manager()   # 不知道为什么加这个就有objects


class Teachers(models.Model):
    # 老师表
    name = models.CharField(max_length=32)
    objects = models.Manager()


class Students(models.Model):
    # 学生表
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)
    objects = models.Manager()
