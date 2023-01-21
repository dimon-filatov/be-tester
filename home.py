import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\dimon\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_1'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)

driver.maximize_window()
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

waiting = WebDriverWait(driver, 20)
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 900);")
driver.find_element_by_css_selector(".post-160 h3").click()
driver.find_element_by_class_name("reviews_tab").click()
driver.find_element_by_class_name("star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Ivan")
driver.find_element_by_id("email").send_keys("aaa@aa.aa")
driver.find_element_by_id("submit").click()

driver.quit()
