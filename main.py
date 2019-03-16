from selenium import webdriver
from google_searcher import GoogleSearcher
from claroty_careers_searcher import ClarotyCareerSearcher

if __name__ == '__main__':
    # browser handler
    chrome_browser = webdriver.Chrome()

    # google search
    google_searcher = GoogleSearcher(chrome_browser)
    google_searcher.search('Claroty')

    print('Number of results: {}\n'.format(google_searcher.get_number_of_results()))

    if google_searcher.get_first_result_link() in ['https://www.claroty.com/']:
        print('https://www.claroty.com/ is the first result link\n')
    else:
        print('Other site is the first result link\n')

    # claroty career search
    claroty_searcher = ClarotyCareerSearcher(chrome_browser)
    print('Current Number of Openings: {}\n'.format(claroty_searcher.get_number_of_openings()))

    chrome_browser.quit()
