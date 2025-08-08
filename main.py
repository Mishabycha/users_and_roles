import django_setup

from blog.models import Post, Comment

#Post.objects.create(
#    title="Test post",
#    text="Test text"
#)

post1 = Post.objects.get(id=1)

#Comment.objects.create(
#    text="Some text",
#    author="Some author",
#    post=post1
#)