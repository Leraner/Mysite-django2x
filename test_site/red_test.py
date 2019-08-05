import pytest
from selenium import webdriver
from django.urls import resolve
from django.test import TestCase
from app.blogengine.home.views import home_visit


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_title(browser):

    browser.get('http://127.0.0.1:8000/home/')
    header_text = browser.find_element_by_tag_name('h1').text
    inputbox = browser.find_element_by_id('rrrrrr')
    inputbox.send_keys('Тест')

    assert header_text == 'Project'
    assert browser.title == 'Project'


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
