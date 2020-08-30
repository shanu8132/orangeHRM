import pytest
import time
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig

class Test_001_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    def test_homePageTitle(self,setup):
        
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
    
    def test_login(self,setup):
        
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_url = self.driver.current_url
        
        if act_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
            self.lp.clickLogout()
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Screenshots\\"+"LoginFailed.png")
            self.driver.close()
            assert False
    
    