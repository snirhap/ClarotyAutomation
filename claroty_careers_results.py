class ClarotyCareersResults:

    def __init__(self, browser_handler):
        self.positions_list = []
        self.browser_handler = browser_handler

    def get_current_openings(self):
        openings = self.browser_handler.find_elements_by_xpath(
            "//div[@class='grid careerr']//div[@class='w-container']//div[@class='w-dyn-list']//div[@class='w-dyn-items']//div[@class='w-dyn-item']")

        for job in openings:
            if job.text != '':
                self.positions_list.append(job.text)

        return self.positions_list

    def get_number_of_openings(self):
        return len(self.get_current_openings())
