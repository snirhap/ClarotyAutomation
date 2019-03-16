from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


class Searcher:
    def __init__(self):
        self.browser_handler = webdriver.Chrome()
        self.results_list = []

    def search(self, search_string):
        self.browser_handler.get("https://www.google.com")
        search_bar = self.browser_handler.find_element_by_xpath("//input[@name='q']")  # get the search bar element
        search_bar.send_keys(search_string)  # type in the search bar
        search_bar.send_keys(Keys.ENTER)  # generates an Enter key pressing

    def get_number_of_results(self):
        stats = self.browser_handler.find_element_by_xpath("//div[@id='resultStats']").text
        return int(''.join(elem for elem in re.findall(r'\d*', re.sub(r'\(.*?\)', '', stats)) if elem.isdigit()))

    def get_first_result_link(self):
        try:
            all_results = self.browser_handler.find_elements_by_xpath("//div[@id='search']//div[@class='g']")

            for result in all_results:
                url = result.find_element_by_tag_name('a').find_element_by_tag_name('cite').find_element_by_tag_name('span').text
                self.results_list.append(url)

            return self.results_list[0]
        except:
            print('No search was excecuted')

    def close_browser(self):
        self.browser_handler.quit()


s = Searcher()
s.search('Claroty')
print(s.get_first_result_link())
print(s.get_number_of_results())
# s.close_browser()
