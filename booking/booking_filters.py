from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BookingFilters:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        
    def apply_star_rating(self, *stars_values):
        # Loop through each star value provided in stars_values
        for star_value in stars_values:
            try:
                # Wait for the star filter box to be visible
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='filters-group' and @data-filters-group='class']"))
                )
            
                # Directly find the star rating element using a specific XPath
                star_xpath = f'//div[@data-filters-item="class:class={star_value}"]'
            
                # Wait until the star element is clickable
                star_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, star_xpath))
                )
            
                # Click the star rating filter
                star_element.click()
                print(f"Found and clicked star rating for: {star_value}")
            
            except TimeoutException:
                print(f"Timeout: Star rating for {star_value} not found.")
            except NoSuchElementException:
                print(f"Star rating for {star_value} not found.")