from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\Salim\\Documents\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome Browser")
    
    elif browser == 'edge':
        driver = webdriver.Edge("C:\\Users\\Salim\\Documents\\edgedriver_win64\\msedgedriver.exe")
        print("Launching Edge Browser")
    
    else:
        driver = webdriver.Chrome("C:\\Users\\Salim\\Documents\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome Browser")
        
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
        