from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE,verbose_name=_('author'))
    title = models.CharField(max_length=100,verbose_name=_('title'))#To let django knows that this _... should be translate it
    tags = TaggableManager()
    image = models.ImageField(_('image'),upload_to='post/%Y/%m/%d/')
    created_at = models.DateTimeField(_('created at'),default=timezone.now)#_('created at') automatically is a verbose name without writing verbose name
    description = models.TextField(_('description'),max_length=15000)
    category = models.ForeignKey('Category',related_name='post_category',verbose_name=_('category'),on_delete=models.CASCADE)
    slug = models.SlugField(_('url'),null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):  
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'slug': self.slug})
    



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog:post_by_tags', args=[str(self.slug)])



