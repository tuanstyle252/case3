from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from pageObjects.LoginPage import Loginpage
import time
import datetime
import pytest
from selenium.webdriver.common.by import By
from basetest import BaseTest


class Testaction(BaseTest):

    def test_action9(self):
        self.lp = Loginpage(self.driver, self.logger)
        # self.lp.clickGmail()
        time.sleep(2)
        self.lp.setUsername(self.credentials)
        time.sleep(1)
        # self.lp.clicknextuser()
        time.sleep(2)
        self.lp.setPassword(self.credentials)
        time.sleep(2)
        # self.lp.clicknextpass()
        self.lp.clicknextuser()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='instant-search']").send_keys("Yak")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='hotel-select-container']/div[3]/table/tbody/tr/td[2]/a").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='rev-navbar-menu']/nav/div[1]/div[5]").click()

        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()

        #get element field input
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").send_keys("automation")
        time.sleep(3)

        #get element send
        self.driver.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()

        #get element value input email
        get_email = self.driver.find_element(By.XPATH, "//*[@id='rtest-to']")
        act = get_email.get_attribute("value")
        error = act + " is not a valid email"

        #get message error
        message = self.driver.find_element(By.CLASS_NAME, "invalid-feedback")
        act_message = message.text

        #check error
        try:
            assert act_message == error
            self.logger.info(f'Passed when validate for error message {act_message} ')
        except Exception as ex:
            self.logger.error(f'Failed when validate for error message {act_message} ' + str(ex))