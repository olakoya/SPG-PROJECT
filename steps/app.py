from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from time import sleep


price = 150
@given(u'I am on the admin login page')
def step_impl(context):
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.get("https://automationintesting.online/#/admin")
    context.driver.implicitly_wait(10)
    sleep(5)
    
@when(u'I log in as an admin Username: "{username}" Password: "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "doLogin").click()
    sleep(5)

@then(u'I should be taken to the Rooms page')
def step_impl(context):
    
    assert "Front Page" in context.driver.find_element(By.ID, "frontPageLink").text
    # assert "Rooms" in self.driver.title

# @given(u'I am logged in as an admin user')
# def step_impl(context):
#     context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
#     context.driver.get("https://automationintesting.online/#/admin")
    
#     nav_link = context.driver.find_elements(By.CLASS_NAME, "nav-item")
#     for link in nav_link:
#         for a in link.find_elements(By.TAG_NAME, "a"):
#             if a.text == "Front Page":
#                 assert "Front Page" in a.text
#     sleep(10)

@when(u'I click the logout button')
def step_impl(context):
    nav_link = context.driver.find_elements(By.CLASS_NAME, "nav-item")
    for link in nav_link:
        for a in link.find_elements(By.TAG_NAME, "a"):
            if a.text == "Logout":
                a.click()
    # context.driver.find_element(By.CSS_SELECTOR, ".ml-auto > li:nth-child(3) > a:nth-child(1)").click()
    sleep(5)

@then(u'I should be taken to the admin login page')
def step_impl(context):
    login_header = context.driver.find_element(By.CSS_SELECTOR, ".col-sm-8 > h2:nth-child(1)").text
    assert "Log into your account" in login_header


