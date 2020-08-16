from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
# Create your models here.

class Category(models.Model):
    '''
    django docs
    https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
    '''
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'classification'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('title',max_length=70)
    
    body = models.TextField('context')
    
    created_time = models.DateTimeField('create time', default=timezone.now)
    modified_time = models.DateTimeField(auto_now=True)
    
    excerpt = models.CharField('abstruct',max_length=200,blank=True)
    
    category = models.ForeignKey(Category,verbose_name='classification',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name='tag', blank=True)
    
    author = models.ForeignKey(User,verbose_name='author',on_delete=models.CASCADE,default=1)
    
    
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)