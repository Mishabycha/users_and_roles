from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Title")
    text = models.TextField(max_length=1000, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of update")

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Text")
    author = models.CharField(max_length=30, verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of update")

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")

