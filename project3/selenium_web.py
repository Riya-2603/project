from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InfoScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        self.driver.get(f"https://www.wikipedia.org/wiki/{query}")
        try:
            search_results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mw-content-text > p"))
            )
            print(search_results.text)
        except Exception as e:
            print(f"Error getting info: {e}")
        self.driver.quit()

