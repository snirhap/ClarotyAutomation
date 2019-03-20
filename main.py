from google_searcher import GoogleSearcher
from claroty_careers_searcher import ClarotyCareerSearcher


if __name__ == '__main__':
    google_searcher = GoogleSearcher()
    google_search_results = google_searcher.search('Claroty')

    print('Number of results: {}\n'.format(google_search_results.get_number_of_results()))

    result_link = google_search_results.get_result_links()

    if result_link[0] in ['https://www.claroty.com/', 'http://www.claroty.com/']:
        print('https://www.claroty.com/ is the first result link\n')
    else:
        print('https://www.claroty.com/ is not the first result link, {} is the first result link\n'
              .format(result_link))

    claroty_searcher = ClarotyCareerSearcher()
    claroty_results = claroty_searcher.search()
    print('Current Number of Openings: {}\n'.format(claroty_results.get_number_of_openings()))

    google_searcher.close()
    claroty_searcher.close()
