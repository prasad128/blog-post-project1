from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    
    def get_publish_date(self):
        self.publish_date = timezone.now()
        self.save()

    def get_approve_comment(self):
        return self.comments.filter(approve_comment=True)
 
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk':self.pk})
     
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default= timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:list')

    def __str__(self):
        return self.text