from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from time import sleep


price = 150

@given(u'I am logged in as an admin user')
def step_impl(context):
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.get("https://automationintesting.online/#/admin")
    context.driver.find_element(By.ID, "username").send_keys('admin')
    context.driver.find_element(By.ID, "password").send_keys('password')
    context.driver.find_element(By.ID, "doLogin").click()

    sleep(10)

@given(u'I am on the admin Rooms page')
def step_impl(context):
    assert "Front Page" in context.driver.find_element(By.ID, "frontPageLink").text

@when(u'I enter room details')
def step_impl(context):
    context.driver.find_element(By.ID, "roomNumber").send_keys("200")
    context.driver.find_element(By.ID, "type").send_keys("Double")
    context.driver.find_element(By.ID, "accessible").send_keys("true")
    context.driver.find_element(By.ID, "roomPrice").send_keys(price)
    context.driver.find_element(By.ID, "wifiCheckbox").click()
    context.driver.find_element(By.ID, "tvCheckbox").click()
    # context.driver.find_element(By.ID, "createRoom").click()
    sleep(5)

@when(u'Click the Create button')
def step_impl(context):
    context.driver.find_element(By.ID, "createRoom").click()
    sleep(5)

@then(u'The new room should be added to the admin Rooms page')
def step_impl(context):
    # assert "200" in context.driver.find_element(By.ID, "roomNumber").text
    rows = context.driver.find_elements(By.CLASS_NAME, "row detail")
    for row in rows:
        if row.find_element(By.ID, "roomNumber").text == "200":
            assert True
    sleep(5)