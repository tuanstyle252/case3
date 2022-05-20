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

    def test_action10(self):
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
        time.sleep(2)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(4)
        #click x
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='modal-header']/button"))).click()
        #check close modal
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        try:
            assert modal == True
            self.logger.info(f'Passed when validate for close modal ')
        except Exception as ex:
            self.logger.error(f'Failed when validate for close modal ' + str(ex))
        time.sleep(3)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()

        menu = self.driver.find_element(By.XPATH, "//*[@class='table tables-v2']/tbody/tr[1]/td[1]")
        click_ticket = self.driver.find_element(By.XPATH,"//*[@class='table tables-v2']/tbody/tr[1]/td[1]/div/label/div")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).click(click_ticket).perform()
        # check close modal
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        try:
            assert modal == True
            self.logger.info(f'Passed when validate for close modal ')
        except Exception as ex:
            self.logger.error(f'Failed when validate for close modal ' + str(ex))


