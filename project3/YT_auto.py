from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class YouTubePlayer:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def play(self, query):
        self.driver.get("https://www.youtube.com")
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys(query)
        search_box.submit()
        video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "video-title"))
        )
        video.click()
