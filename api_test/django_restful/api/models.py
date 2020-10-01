from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    groups = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=100)

    # 美化字段的显示，方便查看。
    def __str__(self):
        return self.name
