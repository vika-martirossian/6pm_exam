from selenium.webdriver.common.by import By

from POM.lib.assertions import assert_that
from POM.lib.helpers import Helpers


class SideBar(Helpers):
    price_search_field = (By.ID, "Price")
    search_result = (By.XPATH, "//*[@id='searchFilters']/div[1]/div[2]/section[4]/div[2]/ul/li/a/span[1]")
    search_result_tag = (By.XPATH, "//*[@aria-label='Remove $35.00 and Under filter']")

    def filter_by_certain_price(self):
        self.find_and_send_keys(self.price_search_field, "35")

    def select_search_result(self, search_tag_expected_text="$35.00 and Under"):
        self.select_item(self.search_result)
        search_tag_actual_text = self.find(self.search_result_tag, get_text=True)
        assert_that(search_tag_actual_text, search_tag_expected_text)
