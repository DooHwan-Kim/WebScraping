
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options = chrome_options, executable_path="D:/Dropbox/WebScraping/WorkSpace/section3/webdriver/chrome/chromedriver")
# driver.set_window_size(1920,1280)

driver.get('https://google.com')

driver.save_screenshot("c:/website1.png")

driver.get('https://www.daum.net')

driver.save_screenshot("c:/website2.png")


driver.quit()
