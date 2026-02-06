from selenium import webdriver

def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.quit()
