from utilities.common_ops import *
from page_objects.home_page import HomePage


def test_o1(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()