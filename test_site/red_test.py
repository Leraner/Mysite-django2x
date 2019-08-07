import os

from django.urls import resolve
from django.test import TestCase
from django.test import SimpleTestCase
from app.blogengine.posts.models import Post
from django.urls import reverse


# def test_title(browser):
#
#     browser.get('http://127.0.0.1:8000')
#     header_text = browser.find_element_by_tag_name('h1').text
#
#     assert header_text == 'Project'
#     assert browser.title == 'Project'


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        assert expected_object_name == 'just a test'


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        assert resp.status_code == 200

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        assert resp.status_code == 200

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        assert resp.status_code == 200
        self.assertTemplateUsed(resp, 'home.html')


# class SimpleTests(SimpleTestCase):
#
#     def test_home_page_status_code(self):
#         response = self.client.get('')
#         assert response.status_code == 200
#
#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         assert response.status_code == 200


# def test_home_visit():
#     found = resolve('/home/')
#     assert found.func == home_visit
#
#
# class HomePageTest(TestCase):
#
#     def test_uses_home_template(self):
#         response = self.client.get('/home/')
#         self.assertTemplateNotUsed(response, 'home/home.html')
