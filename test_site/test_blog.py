from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.blogengine.blog.models import Blog


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Blog.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    # def test_sting_represintation(self):
    #     post = Blog(title='A simple title')
    #     assert str(post) == post.body
    #
    # def test_post_content(self):
    #     assert f'{self.post.title}' == 'A good title'
    #     assert f'{self.post.author}' == 'testuser'
    #     assert f'{self.post.body}' == 'Nice body content'
    #
    # def test_post_list_view(self):
    #     response = self.client.get(reverse('home'))
    #     assert response.status_code == 200
    #     assert 'Nice body content' in response
    #     self.assertTemplateUsed(response, 'home.html')
    #
    # def test_post_detail_view(self):
    #     response = self.client.get('/post/ /')
    #     no_response = self.client.get('/post/100000/')
    #     assert response.status_code == 200
    #     assert no_response.status_code == 404
    #     assert 'Nice body content' in response
