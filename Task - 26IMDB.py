from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class IMDbSearch:
    def __init__(self, driver_path, options):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(500, 500);")

    def expand_menu(self):
        try:
            expand_field_locator = (By.XPATH,
                                    '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')
            expand_field = self.wait.until(EC.element_to_be_clickable(expand_field_locator))
            expand_field.click()
            print("Menu option expanded successfully.")
        except Exception as e:
            print(f"Exception occurred while expanding menu: {e}")

    def enter_name(self, name):
        try:
            name_field_locator = (By.NAME, 'name-text-input')
            name_field = self.wait.until(EC.element_to_be_clickable(name_field_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", name_field)
            name_field.clear()
            name_field.send_keys(name)
            print("Name entered successfully.")
        except Exception as e:
            print(f"Exception occurred while entering name: {e}")

    def enter_credit(self, credit):
        try:
            credit_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
            actions = ActionChains(self.driver)
            actions.send_keys_to_element(credit_button, credit)
            actions.pause(2)
            actions.send_keys(Keys.DOWN)
            actions.pause(1)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            print("Credit entered successfully.")
        except Exception as e:
            print(f"Exception occurred while entering credit: {e}")

    def perform_search(self):
        try:
            search_locator = (By.XPATH,
                              "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button")
            search_locator_button = self.wait.until(EC.element_to_be_clickable(search_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", search_locator_button)
            search_locator_button.click()
            print("Search performed successfully.")
        except Exception as e:
            print(f"Exception occurred while performing search: {e}")

    def wait_for_results(self):
        try:
            results_locator = (By.XPATH,
                               "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul")
            results = self.wait.until(EC.presence_of_all_elements_located(results_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", results[0])
            print("Results are in view.")
        except Exception as e:
            print(f"Exception occurred while waiting for results: {e}")



    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    driver_path = r"\"C:\Users\jayasurya"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    imdb_search = IMDbSearch(driver_path, chrome_options)
    imdb_search.open_page("https://www.imdb.com/search/name/")
    imdb_search.expand_menu()
    imdb_search.enter_name("Brad")
    imdb_search.enter_credit("Pitt")
    imdb_search.perform_search()
    imdb_search.wait_for_results()
    imdb_search.close_browser()