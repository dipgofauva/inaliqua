from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.example.com = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
submit_button = driver.find_element_by_id("submit")

actions = ActionChains(driver)
actions.move_to_element(username_field).click().send_keys("username").perform()
actions.move_to_element(password_field).click().send_keys("password").perform()
actions.move_to_element(submit_button).click().perform()
