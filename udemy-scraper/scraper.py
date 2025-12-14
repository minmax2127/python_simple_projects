# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# URL = "https://www.udemy.com/course/the-complete-machine-learning-course-from-zero-to-expert"



from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium Manager automatically handles the driver
driver = webdriver.Chrome() 

driver.get("http://www.python.org")
assert "Python" in driver.title

# Find an element using a locator and interact with it
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN) # type: ignore

# Close the browser session
driver.quit()