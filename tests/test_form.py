from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, wait):

    driver.get("https://opensource-demo.orangehrmlive.com")

    wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()


def test_add_employee():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,10)

    login(driver, wait)

    # Go to PIM
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='PIM']"))).click()

    # Add Employee
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Add Employee']"))).click()

    # Fill Form
    driver.find_element(By.NAME,"firstName").send_keys("Test")
    driver.find_element(By.NAME,"lastName").send_keys("User")

    # Save
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    # Verify
    success = wait.until(
        EC.presence_of_element_located((By.XPATH,"//h6[text()='Personal Details']"))
    )

    assert success.is_displayed()

    driver.quit()
