from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

UPLOAD_URL = "http://127.0.0.1:8000/soal/"


@given("I logged in for upload file")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://127.0.0.1:8000/users/login/")
    context.browser.find_element(By.NAME, "email").send_keys("testuser2@gmail.com")
    context.browser.find_element(By.NAME, "password").send_keys("Password@123!!")
    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)


@given("I navigates to the question upload page")
def step_impl(context):
    context.browser.get(UPLOAD_URL)
    time.sleep(1)


@when("I selects a valid file in a supported format")
def step_impl(context):
    file_path = os.path.abspath("features/test_files/test_txt.txt")
    file_input = context.browser.find_element(By.ID, "file-input")
    file_input.send_keys(file_path)
    time.sleep(1)


@when("I selects a file with an unsupported format")
def step_impl(context):
    file_path = os.path.abspath("features/test_files/test_png.png")
    file_input = context.browser.find_element(By.ID, "file-input")
    file_input.send_keys(file_path)
    time.sleep(1)


@when("I uploads the file")
def step_impl(context):
    button = context.browser.find_element(By.ID, "classify-btn")
    button.click()
    time.sleep(2)

@then("the file preview should be displayed")
def step_impl(context):
    preview = context.browser.find_element(By.ID, "file-preview")
    assert preview.is_displayed()


@then("the classify button should be enabled")
def step_impl(context):
    btn = context.browser.find_element(By.ID, "classify-btn")
    assert btn.is_enabled()


@then("the system should confirm the file is ready to classify")
def step_impl(context):
    name = context.browser.find_element(By.ID, "file-name").text
    assert name != ""

@then("the system should reject the file")
def step_impl(context):
    preview = context.browser.find_element(By.ID, "file-preview")
    assert preview.is_displayed() is False


@then("the classify button should remain disabled")
def step_impl(context):
    btn = context.browser.find_element(By.ID, "classify-btn")
    assert btn.is_enabled() is False