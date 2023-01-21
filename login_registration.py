# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
#
# from selenium.webdriver.support import expected_conditions as EC
#
# path_to_extension = r'C:\Users\dimon\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_1'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
#
# driver.maximize_window()
# driver.implicitly_wait(10)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
#
# waiting = WebDriverWait(driver, 20)
# driver.get("https://practice.automationtesting.in/")
#
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("reg_email").send_keys("aaa@aa.aa")
# driver.find_element_by_id("reg_password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="register"]').click()
#
# driver.quit()


#################################################################################


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

driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("aaa@aa.aa")
driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
driver.find_element_by_css_selector('[name="login"]').click()

logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
assert logout.text == 'Logout'

driver.quit()
