from selenium import webdriver
from claroty_careers_results import ClarotyCareersResults


class ClarotyCareerSearcher:
    def __init__(self):

        self.browser_handler = webdriver.Chrome()

    def search(self):
        self.browser_handler.get("https://www.claroty.com/careers/")

        return ClarotyCareersResults(self.browser_handler)

    def close(self):
        self.browser_handler.quit()
