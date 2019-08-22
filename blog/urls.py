from django.urls import path
from .views import BlogListViews, BlogDetailView, BlockCreateView
from home.views import AboutPageView


urlpatterns = [
    path('', BlogListViews.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/new/', BlockCreateView.as_view(), name='post_new')
]