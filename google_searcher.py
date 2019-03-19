from selenium.webdriver.common.keys import Keys
import re


class GoogleSearcher:
    def __init__(self, browser_handler):
        """
            expect to get an instance of Selenium web driver (e.g. Chrome, Firefox, etc.)
        """
        self.results_list = []
        self.browser_handler = browser_handler

    def search(self, search_string):
        """
            open a desired browser and execute a search according to the search string input
        """
        self.browser_handler.get("https://www.google.com")
        search_bar = self.browser_handler.find_element_by_xpath("//input[@name='q']")  # get the search bar element
        search_bar.send_keys(search_string)  # type in the search bar
        search_bar.send_keys(Keys.ENTER)  # generates an Enter key pressing

    def get_number_of_results(self):
        """
            returns the number of results to the search string in Google
        """
        try:
            stats = self.browser_handler.find_element_by_xpath("//div[@id='resultStats']").text
            return int(''.join(elem for elem in re.findall(r'\d*', re.sub(r'\(.*?\)', '', stats)) if elem.isdigit()))
        except:
            raise Exception('No search was executed')

    def get_result_link_by_position(self, position=1):
        """
            Returns the URL that appears in the position provided
            Default is the first result in Google
            position = 1 will return the first result in Google search
        """
        try:
            all_results = self.browser_handler.find_elements_by_xpath("//div[@id='search']//div[@class='g']")

            for result in all_results:
                url = result.find_element_by_tag_name('a').find_element_by_tag_name('cite').find_element_by_tag_name('span').text
                self.results_list.append(url)

            return self.results_list[position-1]

        except IndexError:
            raise Exception('Position provided is invalid')
        except:
            raise Exception('No search was executed')
