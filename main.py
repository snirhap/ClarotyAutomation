from selenium import webdriver
from google_searcher import GoogleSearcher
from google_results import GoogleResults
from claroty_careers_searcher import ClarotyCareerSearcher

if __name__ == '__main__':
    # Browser handler
    chrome_browser = webdriver.Chrome()

    # Google search
    google_searcher = GoogleSearcher(chrome_browser)
    google_search_results_handler = google_searcher.search('Claroty')

    google_search_results = GoogleResults(google_search_results_handler)

    # Get the number of results in Google
    print('Number of results: {}\n'.format(google_search_results.get_number_of_results()))

    # Check if Calroty is the first result link in the result
    first_result_link = google_search_results.get_result_link_by_position()  # 1 = first result

    if first_result_link in ['https://www.claroty.com/', 'http://www.claroty.com/']:
        print('https://www.claroty.com/ is the first result link\n')
    else:
        print('https://www.claroty.com/ is not the first result link, {} is the first result link\n'.format(first_result_link))

    # Claroty career search
    # Check the number of openings in Claroty
    claroty_searcher = ClarotyCareerSearcher(chrome_browser)
    number_of_openings = claroty_searcher.get_number_of_openings()
    print('Current Number of Openings: {}\n'.format(number_of_openings))

    chrome_browser.quit()
