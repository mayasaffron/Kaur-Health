from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.contrib import messages
from .forms import BlogPostForm


class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/all_blogs.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


def add_blog_post(request):
    '''A view to allow users to add blogs'''
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry you can only add a blog if youre logged in!')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Thank you! your blog has been added')
            return redirect(reverse('blog_detail', args=[new_blog.pk]))
        else:
            messages.error(request, 'Blog cannot be added, please recheck the form')
            return redirect(reverse('add_blog_post'))
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def update_blog(request, pk):
    '''A view to allow users to edit blogs'''

    blog = get_object_or_404(BlogPost, pk=pk)
    print(blog)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_detail', args=[blog.pk]))
        else:
            messages.error(request, 'Failed to update, please recheck the form')
    else:
        form = BlogPostForm(instance=blog)
        messages.info(request, f'You are editing "{blog.title}" ')

    template = 'blog/update_blog_post.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


def delete_blog(request, pk):
    '''A view to allow super users to delete products'''
    blog = get_object_or_404(BlogPost, pk=pk)
    blog.delete()
    messages.success(request, f' "{blog.title}" has been deleted')
    return redirect(reverse('blog'))
