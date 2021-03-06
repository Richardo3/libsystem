from django.db import models

# Create your models here.
class BookInfo(models.Model):
    branking = models.SmallIntegerField(verbose_name='排名')
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bauthor = models.CharField(max_length=20, verbose_name='作者')
    btype = models.CharField(max_length=20, verbose_name='分类')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 指定数据库中的表名
    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle


class AuthorsInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    aname = models.CharField(max_length=20, verbose_name='作者名称')
    agender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    acomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    abook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_authors'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.aname
