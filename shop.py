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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
#
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".post-181 h3").click()
# title = driver.find_element_by_css_selector("h1.product_title")
# assert title.text == 'HTML5 Forms'
#
# driver.quit()


#################################################################################

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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
#
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".cat-item-19 a").click()
#
# items = driver.find_elements_by_css_selector(".products  li")
# assert len(items) == 3, "Items != 3"
#
# driver.quit()


#################################################################################

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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
# driver.find_element_by_id("menu-item-40").click()
#
# select = driver.find_element_by_css_selector('[name="orderby"]')
# selector = Select(select)
#
# assert selector.first_selected_option.text == 'Default sorting', 'Select != Default sorting'
#
# selector.select_by_value('price-desc')
#
# select = driver.find_element_by_css_selector('[name="orderby"]')
# selector = Select(select)
#
# assert selector.first_selected_option.text == 'Sort by price: high to low', 'Select != Sort by price: high to low'
#
# driver.quit()


#################################################################################

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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
# driver.find_element_by_id("menu-item-40").click()
#
# driver.find_element_by_css_selector(".post-169 h3").click()
#
# old_price = driver.find_element_by_css_selector('.price del .woocommerce-Price-amount').text
# assert old_price == '₹600.00', 'Old price != ₹600'
#
# new_price = driver.find_element_by_css_selector('.price ins .woocommerce-Price-amount').text
# assert new_price == '₹450.00', 'New price != ₹450.00'
#
# img = waiting.until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-main-image")))
# img.click()
# img_exit = waiting.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# img_exit.click()
#
# driver.quit()


#################################################################################

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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
# driver.find_element_by_id("menu-item-40").click()
#
# driver.find_element_by_css_selector(".post-182 .button").click()
#
# waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".wpmenucartli .amount"), "₹180.00"))
# cart_item = driver.find_element_by_css_selector(".wpmenucartli .cartcontents").text
# cart_amount = driver.find_element_by_css_selector(".wpmenucartli .amount").text
#
# assert cart_item == "1 Item", "cart item != 1"
# assert cart_amount == "₹180.00", "cart amount != ₹180.00"
#
# driver.find_element_by_css_selector(".wpmenucartli").click()
#
# waiting.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount")))
# waiting.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount")))
#
# driver.quit()


#################################################################################

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
# driver.find_element_by_id("username").send_keys("aaa@aa.aa")
# driver.find_element_by_id("password").send_keys("qwerty123455432112345qwerty")
# driver.find_element_by_css_selector('[name="login"]').click()
#
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:nth-child(6) a")
# assert logout.text == 'Logout'
# driver.find_element_by_id("menu-item-40").click()
#
# driver.find_element_by_css_selector(".post-182 .button").click()
# driver.find_element_by_css_selector(".post-165 .button").click()
# waiting.until(EC.element_to_be_clickable((By.CLASS_NAME, "wpmenucartli"))).click()
#
# driver.find_element_by_css_selector(".cart_item:nth-child(1) .remove").click()
# waiting.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-message a"))).click()
# waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart_item:nth-child(1) .product-name a"), "Mastering JavaScript"))
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
# quantity.clear()
# quantity.send_keys(3)
# driver.find_element_by_css_selector('[name="update_cart"]').click()
# assert quantity.get_attribute("value") == '3', "quantity != 3"
# time.sleep(2)
# driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# waiting.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-error")))
# assert driver.find_element_by_class_name("woocommerce-error").text == "Please enter a coupon code."
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
driver.find_element_by_id("menu-item-40").click()

driver.find_element_by_css_selector(".post-182 .button").click()
waiting.until(EC.element_to_be_clickable((By.CLASS_NAME, "wpmenucartli"))).click()

waiting.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
driver.find_element_by_id("billing_first_name").send_keys("Ivan")
driver.find_element_by_id("billing_last_name").send_keys("Ivanov")
driver.find_element_by_id("billing_phone").send_keys("89999999999")
driver.find_element_by_id("billing_address_1").send_keys("some street")
driver.find_element_by_id("billing_city").send_keys("some city")
driver.find_element_by_id("billing_postcode").send_keys("12345")

time.sleep(2)

driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()

waiting.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3) td"), "Check Payments"))

driver.quit()
