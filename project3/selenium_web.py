from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # Import for element selection

class InfoScraper:  # More descriptive class name
    def __init__(self):  # Corrected the __init__ method
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        self.query = query
        self.driver.get(f"https://www.wikipedia.org/wiki/{query}")  # Direct search URL
        print("Data", query)
        # Implement search result scraping logic here
        # Example:
        try:
            # Use explicit waits for dynamic content (adjust selectors as needed)
            search_results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mw-content-text > p"))
            )
            print(search_results.text)  # Example of extracting text from results
        except Exception as e:
            print(f"Error getting info: {e}")

        # Close the browser after scraping (optional)
        self.driver.quit()

# if __name__ == "__main__":  # Corrected the main method check
#     assistant = InfoScraper()
#     assistant.get_info("Python")

