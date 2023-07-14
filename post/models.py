from django.db import models
from django.conf import settings

# Create your models here.
class CounselPost(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    hashtag_choices = [('취업고민', '취업고민'), ('진로고민', '진로고민'), ('연애고민', '연애고민'), ('인간관계', '인간관계'), ('번아웃', '번아웃'),('다이어트', '다이어트')]
    hashtag = models.CharField(max_length=128, choices = hashtag_choices)
    date = models.DateField(auto_now_add=True)
    post_like = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='post_image')
    author = models.ForeignKey('account.CustomUser', null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     null=True, 
    #     default='null'
    # )
    like_users = models.ManyToManyField(
        'account.CustomUser',
        related_name='like_counselposts', 
    )

    def __str__(self):
        return self.title


class CounselComment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey('post.CounselPost', null=True, blank=True, on_delete=models.CASCADE, related_name='post_comment')
    comment_like = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('account.CustomUser', null=True, on_delete=models.CASCADE)
    comment_like = models.IntegerField(default=0)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE, 
    #     null=True, 
    #     default='null'
    # )
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name='like_counselcomments'
    # )

    def __str__(self):
        return self.comment

class CounselRecomment(models.Model):
    recomment = models.TextField()
    comment = models.ForeignKey('post.CounselComment', null=True, blank=True, on_delete=models.CASCADE, related_name='recomment')
    recomment_like = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('account.CustomUser', null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     null=True, 
    #     default='null'
    # )
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name='like_counselrecomments'
    # )

    def __str__(self):
        return str(self.pk)

class JarPost(models.Model):
    content = models.TextField()
    jar_like = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='post_image')
    author = models.ForeignKey('account.CustomUser', null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     null=True, 
    #     default='null'
    # )
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name='like_jarposts'
    # )
    # like_users = models.ManyToManyField(
    #     ,
    #     related_name='like_jarposts'
    # )
    def __str__(self):
        return str(self.pk)