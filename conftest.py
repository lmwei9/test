import pytest
from selenium import webdriver
from day09.tool.web_key import WebKey
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver1():
    driver12 = webdriver.Chrome()

    yield driver12

    driver12.quit()

def drever2():
    pass
