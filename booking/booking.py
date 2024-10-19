from types import TracebackType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from booking.booking_filters import BookingFilters
from booking.booking_report import BookingReport
import booking.constants as const
from prettytable import PrettyTable
from selenium import webdriver
import time

class Booking(webdriver.Chrome):
    def __init__(self, options: Options = None, service: Service = None, keep_alive: bool = True) -> None:
        super().__init__(options, service, keep_alive)
        self.implicitly_wait(15)
        self.maximize_window()
        self.titles = []
        self.prices = []
        
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def click(self, button):
        try:
            self.find_element(By.CSS_SELECTOR, f'button[{button}]').click()
            time.sleep(2)
        except:
            print("no se encontro confirmacion")
    
    def select_currency(self, currency):
        self.find_element(By.XPATH, f"//button[.//div[@class=' CurrencyPicker_currency' and text()='{currency}']]").click()
        time.sleep(2)
        
    def place_to_go(self, place_to_go):
        input_text = self.find_element(By.ID, ":rh:")
        input_text.send_keys(place_to_go)
        time.sleep(2)
        self.find_element(By.XPATH, "//li[@id='autocomplete-result-0']//div[@role='button']").click()
        
    def seach_button(self):
        self.find_element(By.XPATH, '//form[@role="region"]//button[@type="submit"]').click()
        time.sleep(2)
    
    def select_date(self, start_date, end_date):
        self.find_element(By.XPATH, f'//td//span[@data-date="{start_date}"]' ).click()
        self.find_element(By.XPATH, f'//td//span[@data-date="{end_date}"]' ).click()
        time.sleep(2)
    
    def filter(self,*star):
        filter = BookingFilters(driver=self)
        filter.apply_star_rating(*star)
        time.sleep(2)
    
    def report_result(self):
        try:
            hotel_boxes_section = self.find_element(By.XPATH, '//div[@data-results-container="1"]')
            report = BookingReport(hotel_boxes_section)
            self.titles = report.pull_titles()
            self.prices = report.pull_prices()
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def Print_table(self):
        table = PrettyTable(field_names=["Hotel Name","Hotel Price"])
        for title, price in zip(self.titles, self.prices):
            table.add_row([title, price])
        print(table)
    
    
    
    
    
    # the WebPage architecture dont allow do this exercise 
    #but i want to save the get value
    def select_adults(self, adults_number):
        self.find_element(By.XPATH, "//button[@aria-controls=':ri:']").click()
        #get value
        adults = self.find_element(By.XPATH, "//input[@id='group_adults']").get_attribute("value")
        time.sleep(1)
        