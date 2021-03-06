from django.db import models


# Create your models here.
class ClassBlog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # 자동으로 추가
    updated_at = models.DateTimeField(auto_now=True)  # 자동으로 추가
    body = models.TextField()

    def __str__(self):
        return self.title
