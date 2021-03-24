from django.db import models
from django.contrib.auth.models import User
from products_and_services.models import Category


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,
                                 blank=True, on_delete=models.SET_NULL)
    body = models.TextField()
    blog_image = models.ImageField(null=False, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)
