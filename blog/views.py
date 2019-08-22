from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Blog


class BlogListViews(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blog_data'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'danila'


class BlockCreateView(CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']