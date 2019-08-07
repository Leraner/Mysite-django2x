from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListViews(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blog_data'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'danila'
