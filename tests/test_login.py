from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()
    
    try:
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com")
        
        wait = WebDriverWait(driver, 10)
        
        # Username
        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")
        
        # Password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")
        
        # Login Button
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()
        
        # Verify Dashboard
        dashboard = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
        
        assert dashboard.is_displayed()
    
    finally:
        # ✅ This ALWAYS runs - pass or fail!
        driver.quit()