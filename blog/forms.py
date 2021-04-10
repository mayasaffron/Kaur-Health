from django import forms
from .models import BlogPost, Comment
from products_and_services.models import Category
from .widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = 'title', 'category', 'body', 'blog_image'

    blog_image = forms.ImageField(
                                 label='Image', required=False,
                                 widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name())for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'name', 'body'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

