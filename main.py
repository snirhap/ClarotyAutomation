from selenium import webdriver
from google_searcher import GoogleSearcher
from claroty_careers_searcher import ClarotyCareerSearcher

if __name__ == '__main__':

    chrome_browser = webdriver.Chrome()
    google_searcher = GoogleSearcher(chrome_browser)
    google_search_results = google_searcher.search('Claroty')

    print('Number of results: {}\n'.format(google_search_results.get_number_of_results()))

    first_result_link = google_search_results.get_result_link_by_position(1)  # 1 = first result

    if first_result_link in ['https://www.claroty.com/', 'http://www.claroty.com/']:
        print('https://www.claroty.com/ is the first result link\n')
    else:
        print('https://www.claroty.com/ is not the first result link, {} is the first result link\n'
              .format(first_result_link))

    claroty_searcher = ClarotyCareerSearcher(chrome_browser)
    number_of_openings = claroty_searcher.get_number_of_openings()
    print('Current Number of Openings: {}\n'.format(number_of_openings))

    chrome_browser.quit()
