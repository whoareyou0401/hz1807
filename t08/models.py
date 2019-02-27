from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="书名"
    )
    price = models.FloatField(
        "价格"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "书籍"
        verbose_name_plural="所有书籍"