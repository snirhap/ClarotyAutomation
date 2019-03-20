from selenium.webdriver.common.keys import Keys
from google_results import GoogleResults


class GoogleSearcher:
    def __init__(self, search_handler):
        self.search_handler = search_handler

    def search(self, search_string):
        self.search_handler.get("https://www.google.com")
        search_bar = self.search_handler.find_element_by_xpath("//input[@name='q']")
        search_bar.send_keys(search_string)
        search_bar.send_keys(Keys.ENTER)

        return GoogleResults(self.search_handler)
