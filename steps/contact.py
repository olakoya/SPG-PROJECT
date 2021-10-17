from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from time import sleep
import steps.app as app

name = 'Shady Meadows B&B!'

@given(u'I am on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.get('https://automationintesting.online/#/')
    sleep(10)

@when(u'I populate the contact form at the bottom of the page')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys(name)
    context.driver.find_element(By.ID, "email").send_keys('fake@fakeemail.com')
    context.driver.find_element(By.ID, "phone").send_keys('012345678901')
    context.driver.find_element(By.ID, "subject").send_keys('farmhouse')
    context.driver.find_element(By.ID, "description").send_keys('This is a test message')

@when(u'Click the submit button')
def step_impl(context):
    context.driver.find_element(By.ID, "submitContact").click()
    sleep(5)

@then(u'The text "Thanks for getting in touch <name>!" should be displayed')
def step_impl(context):
    elem = context.driver.find_elements(By.ID, "col-sm-5")
    for i in elem:
        if name in i.find_element(By.TAG_NAME, "h1"):
            print(i.text)
            assert i.text == 'Thanks for getting in touch ' + name + '!'

@given(u'I have submitted the contact form')
def step_impl(context):
    elem = context.driver.find_elements(By.ID, "col-sm-5")
    for i in elem:
        if  name in i.find_element(By.TAG_NAME, "h1").text:
            # sleep(5)
            print(i.text)
    # step_impl(context)
    # step_impl(context)
        assert 'as soon as possible' in i.text

# @when(u'I log in as an admin user')
# def step_impl(context):
#     context.driver.find_element(By.ID, "username").send_keys(username)
#     context.driver.find_element(By.ID, "password").send_keys(password)
#     context.driver.find_element(By.ID, "doLogin").click()
#     sleep(5)


@Given(u'I navigate to the admin messages page')
def step_impl(context):
    navs = context.driver.find_elements(By.ID, "nav-link")
    for nav in navs:
        if nav.find_element(By.TAG_NAME, "a").href == '#/admin/messages':
            nav.click()
        # context.driver.find_element(By.CLASS_NAME, "fa fa-inbox").click()
        sleep(5)

@then(u'I should see the details of the message I submitted')
def step_impl(context):
    messages = context.driver.find_elements(By.CLASS_NAME, 'messages')
    for message in messages:
        assert name in message.text

