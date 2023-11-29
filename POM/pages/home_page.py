from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers


class HomePage(Helpers):
    shop_now_link = (By.XPATH, "(//*[@class='xj-z'])[2]")

    def click_on_shop_now_link(self):
        self.find_and_click(self.shop_now_link)
