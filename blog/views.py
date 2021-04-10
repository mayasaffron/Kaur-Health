from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BlogPostForm, CommentForm
from django.template.defaultfilters import slugify


class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/all_blogs.html'

    def get_queryset(self):
        author_val = self.request.GET.get('author', '')
        if author_val:
            author_object = User.objects.get(username=author_val)
            new_context = BlogPost.objects.filter(
                author=author_object,
            )
        else:
            new_context = BlogPost.objects.all()
        return new_context

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['author'] = self.request.GET.get('author')
        return context


def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post_comment = blog
            new_comment.save()
            messages.success(request, 'Thank you! Your \
                             comment has been added.')
            return redirect(reverse('blog_detail', kwargs={'slug': blog.slug}))

        else:
            messages.error(request, 'Comment cannot be added, please \
                           recheck the form')
            return redirect(reverse('blog_detail', kwargs={'slug': blog.slug}))
    context = {
        'object': blog,
        'form': form,
        'on_blog_detail_page': True,
    }
    return render(request, 'blog/blog_detail.html', context)


def add_blog_post(request):
    '''A view to allow users to add blogs'''
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you can only add a \
                        blog if youre logged in!')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_slug = slugify(form.cleaned_data['title'])
            qs_exists = BlogPost.objects.filter(
                    slug=new_slug).exists()
            if qs_exists:
                messages.error(request, 'A blog with this title, already exists!\
                                Change it slightly please.')
                return redirect(reverse('add_blog_post'))
            new_blog.slug = new_slug
            new_blog.save()
            messages.success(request, 'Thank you! Your blog has been added.')
            return redirect(reverse('blog_detail',
                                    kwargs={'slug': new_blog.slug}))
        else:
            messages.error(request, 'Blog cannot be added, please \
                            recheck the form.')
            return redirect(reverse('add_blog_post'))
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)


def update_blog(request, slug):
    '''A view to allow users to edit blogs'''

    blog = get_object_or_404(BlogPost, slug=slug)
    print(blog)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_detail', args=[blog.slug]))
        else:
            messages.error(request, 'Failed to update, please \
                            recheck the form.')
    else:
        form = BlogPostForm(instance=blog)
        messages.info(request, f'You are editing "{blog.title}" .')

    template = 'blog/update_blog_post.html'
    context = {
        'form': form,
        'blog': blog,
        'on_blog_page': True,
    }

    return render(request, template, context)


def delete_blog(request, pk):
    '''A view to allow super users to delete products'''
    blog = get_object_or_404(BlogPost, pk=pk)
    blog.delete()
    messages.success(request, f' "{blog.title}" has been deleted')
    return redirect(reverse('blog'))
