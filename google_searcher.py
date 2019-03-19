from selenium.webdriver.common.keys import Keys
from google_results import GoogleResults


class GoogleSearcher:
    def __init__(self, search_handler):
        """
            expect to get an instance of Selenium web driver (e.g. Chrome, Firefox, etc.)
        """

        self.search_handler = search_handler

    def search(self, search_string):
        """
            open a desired browser and execute a search according to the search string input
            returns a search handler that contains all data from the search query results
        """
        self.search_handler.get("https://www.google.com")
        search_bar = self.search_handler.find_element_by_xpath("//input[@name='q']")  # get the search bar element
        search_bar.send_keys(search_string)  # type in the search bar
        search_bar.send_keys(Keys.ENTER)  # generates an Enter key pressing

        return GoogleResults(self.search_handler)

