from selenium.webdriver.common.by import By
import time

# _email_locator = "//*[@id='identifierId']"
# _gmail = "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]/div[2]"
# _password_locator = "//*[@id='password']/div[1]/div/div[1]/input"
# _next_username_btn_locator = "//*[@id='identifierNext']/div/button/span"
# _next_password_btn_locator = "//*[@id='passwordNext']/div/button"
#
_email_locator = "//*[@id='username']"
_password_locator = "//*[@id='password']"
_sign_in_btn_locator = "/html/body/div[3]/div/div[1]/form/input"


class Loginpage:

    driver = None
    logger = None

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    # def setUsername(self, credentials):
    #     self.driver.find_element(By.XPATH, _email_locator).send_keys(credentials.email)
    #     time.sleep(1)
    #
    # def setPassword(self, credentials):
    #     self.driver.find_element(By.XPATH, _password_locator).send_keys(credentials.password)
    #     time.sleep(1)
    #
    # def clicknextuser(self):
    #     click_next_user = self.driver.find_element(By.XPATH, _next_username_btn_locator)
    #     click_next_user.click()
    #     time.sleep(1)
    #
    # def clickGmail(self):
    #     click_gmail = self.driver.find_element(By.XPATH, _gmail)
    #     click_gmail.click()
    #     time.sleep(1)
    #
    # def clicknextpass(self):
    #     self.driver.find_element(By.XPATH, _next_password_btn_locator).click()

    def setUsername(self, credentials):
        self.driver.find_element(By.XPATH, _email_locator).send_keys(credentials.email)
        time.sleep(1)

    def setPassword(self, credentials):
        self.driver.find_element(By.XPATH, _password_locator).send_keys(credentials.password)
        time.sleep(1)

    def clicknextuser(self):
        click_next_user = self.driver.find_element(By.XPATH, _sign_in_btn_locator)
        click_next_user.click()
        time.sleep(1)