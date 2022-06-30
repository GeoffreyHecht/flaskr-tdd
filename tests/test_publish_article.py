from pytest_bdd import scenario, given, when, then
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pytest


@scenario('publish_article.feature', 'Publishing an article with a title and a text')
def test_publish():
    pass


@given("I'm a connected user")
def connect_user(browser):
    """ dasadsadsf """
    login = "admin"
    password = "admin"
    browser.visit('http://127.0.0.1:5000/login')
    browser.find_by_name('username').fill(login)
    browser.find_by_name('password').fill(password)
    browser.find_by_value('Login').click()

@given("I check the index page")

def go_to_index(browser):
    browser.visit('http://127.0.0.1:5000')

@when("I enter a title for my article")
def enter_title(browser):
    browser.find_by_name('title').fill('Check my new blog')
    
    
@when("I enter a text for my article")
def enter_text(browser):
    browser.find_by_name('text').fill('Yeah ! This is my first article')

@when("I press the share button")
def publish_article(browser):
    browser.find_by_value('Share').click()


@then("I should not see the error message")
def no_error_message(browser):
    with pytest.raises(ElementDoesNotExist):
        browser.find_by_css('.message.error').first


@then("the article should be published")
def article_is_published(browser):
    assert browser.is_text_present('Check my new blog')
    assert browser.is_text_present('New entry was successfully posted')