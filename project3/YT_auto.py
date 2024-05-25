# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By  # Import for element selection
#
#
# class music:  # More descriptive class name
#     def __init__(self):  # Corrected the __init__ method
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     def play(self, query):
#         self.query = query
#         self.driver.get("https://www.youtube.com/results?search_query=" + query)
#         video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
#         video.click()
#
# assist= music()
# assist.play('dynamite by bts')

#         # Search for the query
#         search_box = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "search_query"))
#         )
#         search_box.send_keys(query)
#         search_box.submit()
#
#         try:
#             # Wait for search results to load
#             video_elements = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_all_elements_located((By.ID, "video-title"))
#             )
#
#             # Print titles and links of the first few video results
#             for video in video_elements[:5]:  # Adjust the number to get more results
#                 title = video.get_attribute("title")
#                 link = video.get_attribute("href")
#                 print(f"Title: {title}\nLink: {link}\n")
#         except Exception as e:
#             print(f"Error getting info: {e}")
#
#         # Close the browser after scraping (optional)
#         self.driver.quit()
#
#
# if __name__ == "__main__":  # Corrected the main method check
#     assistant = YouTubeScraper()
#     assistant.get_info("Python programming")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class YouTubePlayer:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com")

        # Search for the query
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys(query)
        search_box.submit()

        try:
            # Wait for search results to load and click the first video
            video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail'))
            )
            video.click()

            # Wait for the video to start playing
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'html5-video-player'))
            )
            print("Playing video:", query)

            # Get video duration in seconds
            duration_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ytp-time-duration'))
            )
            duration_text = duration_element.text
            duration_parts = duration_text.split(":")
            if len(duration_parts) == 2:
                duration = int(duration_parts[0]) * 60 + int(duration_parts[1])
            elif len(duration_parts) == 3:
                duration = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])
            else:
                duration = 0
            print(f"Video duration: {duration} seconds")

            # Wait for the duration of the video
            time.sleep(duration + 5)  # Adding a buffer of 5 seconds

        except Exception as e:
            print(f"Error playing video: {e}")

        # Close the browser after the video finishes
        self.driver.quit()

# if __name__ == "__main__":
#     assistant = YouTubePlayer()
#     assistant.play("dynamite by bts")
