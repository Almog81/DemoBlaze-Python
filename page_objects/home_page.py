
class HomePage():
    url = "https://www.demoblaze.com/"

    def __init__(self ,driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get(self.url)