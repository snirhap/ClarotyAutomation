from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from google_results import GoogleResults


class GoogleSearcher:
    def __init__(self):
        self.browser_handler = webdriver.Chrome()

    def search(self, search_string):
        self.browser_handler.get("https://www.google.com")
        search_bar = self.browser_handler.find_element_by_xpath("//input[@name='q']")
        search_bar.send_keys(search_string)
        search_bar.send_keys(Keys.ENTER)

        return GoogleResults(self.browser_handler)

    def close(self):
        self.browser_handler.quit()
