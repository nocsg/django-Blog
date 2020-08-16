from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email')
    url = models.URLField('url',blank=True)
    text = models.TextField('context')
    created_time = models.DateTimeField('created_time',default=timezone.now)
    post = models.ForeignKey('blog.Post',verbose_name='article',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return '{}: {}'.format(self.name,self.text[:20])