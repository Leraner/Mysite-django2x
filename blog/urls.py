from django.urls import path
from .views import (BlogListViews,
                    BlogDetailView,
                    BlockCreateView,
                    BlogUpdateView,
                    BlogDeleteView,
                    )
from home.views import AboutPageView


urlpatterns = [
    path('', BlogListViews.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/new/', BlockCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
