from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
    
    # Pull all property-card elements within the section
    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.XPATH, '//div[@data-testid="property-card"]')

    # Extract and print the titles from the deal boxes
    def pull_titles(self):
        titles = []
        for deal_box in self.deal_boxes:
            title = deal_box.find_element(By.XPATH, './/*[@data-testid="title"]').get_attribute('innerHTML').strip()
            titles.append(title)
        return titles
    
    def pull_prices(self):
        prices = []
        for deal_box in self.deal_boxes:
            price = deal_box.find_element(By.XPATH, './/*[@data-testid="price-and-discounted-price"]').get_attribute('innerHTML').strip()
            prices.append(price)
        return prices