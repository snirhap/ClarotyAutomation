import re


class GoogleResults:
    def __init__(self, results_handler):
        self.results_list = []
        self.results_handler = results_handler

    def get_number_of_results(self):
        try:
            stats = self.results_handler.find_element_by_xpath("//div[@id='resultStats']").text
            return int(''.join(elem for elem in re.findall(r'\d*', re.sub(r'\(.*?\)', '', stats)) if elem.isdigit()))
        except:
            raise Exception('No search was executed')

    def get_result_links(self):
        try:
            all_results = self.results_handler.find_elements_by_xpath("//div[@id='search']//div[@class='g']")

            for result in all_results:
                url = result.find_element_by_tag_name('a').find_element_by_tag_name('cite').find_element_by_tag_name('span').text
                self.results_list.append(url)

            return self.results_list

        except TypeError:
            raise Exception('Missing position parameter')
        except IndexError:
            raise Exception('Position provided is invalid')
        except:
            raise Exception('No search was executed')

    def get_result_link_by_position(self, position):
        return self.get_result_links()[position-1]
