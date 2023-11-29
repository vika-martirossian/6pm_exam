import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_shop_now_page(self):
        self.homepage.click_on_shop_now_link()

    def verify_filtering_by_price(self):
        self.sidebar.filter_by_certain_price()


