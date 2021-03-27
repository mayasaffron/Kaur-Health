from django.db import models
from django.contrib.auth.models import User
from products_and_services.models import Category
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=254, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,
                                 blank=True, on_delete=models.SET_NULL)
    body = models.TextField()
    blog_image = models.ImageField(null=False, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post_comment = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    name = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.post_comment.title, self.name)
