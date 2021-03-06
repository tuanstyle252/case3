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

    def test_action5(self):
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
        time.sleep(1)

        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(2)
        privacy = self.driver.find_element(By.LINK_TEXT, "Privacy Policy")
        privacy.click()
        table1 = self.driver.window_handles[1]
        self.driver.switch_to.window(table1)
        time.sleep(3)

        # switch to parent window
        time.sleep(2)
        act_title = self.driver.title
        time.sleep(2)
        try:
            act_title == "Privacy Policy - Revinate"
            self.logger.info(f'Passed when validate for navigate the user to the "privacy policy" page')
        except Exception as ex:
            self.logger.error(f'Failed when validate for navigate the user to the "privacy policy" page ' + str(ex))

        # close browser parent window
        time.sleep(3)
        self.driver.switch_to.window(table0)
