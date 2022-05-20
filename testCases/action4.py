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

    def test_action4(self):
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
        time.sleep(4)
        self.driver.find_element(By.LINK_TEXT, "https://guest-feedback-test.revinate.com/gf/66347/tickets?assigneeIds%5B0%5D=292811&status%5B0%5D=open&ticket_num=&sortBy%5Bid%5D=ts_updated&sortBy%5Bdesc%5D=true").click()
        time.sleep(2)
        self.driver.refresh()
        self.logger.info(f'Passed when validate should refresh page')
        self.driver.close()