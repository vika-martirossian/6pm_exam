from POM.tests.base_test import BaseTest


class TestSideBar(BaseTest):
    def test_filtering_by_price(self):
        self.navigate_to_shop_now_page()
        self.verify_filtering_by_price()
