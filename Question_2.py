from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()  # You can replace this with the path to your WebDriver executable

# Navigate to the URL
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

# Click Customer Login
customer_login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Customer Login')]")
customer_login_button.click()

# Choose Your Name as Hermoine Granger and Login
select_customer_dropdown = driver.find_element(By.XPATH, "//select[@id='userSelect']")
select_customer_dropdown.click()
hermoine_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Hermoine Granger')]")
hermoine_option.click()

login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_button.click()

# Choose "1003" in the drop down
account_dropdown = driver.find_element(By.XPATH, "//select[@id='accountSelect']")
account_dropdown.click()
account_option = driver.find_element(By.XPATH, "//option[@value='1003']")
account_option.click()

# Define transaction data
transactions = [
    (50000, "Credit"),
    (3000, "Debit"),
    (2000, "Debit"),
    (5000, "Credit"),
    (10000, "Debit"),
    (15000, "Debit"),
    (1500, "Credit")
]

# Iterate through transactions
for amount, transaction_type in transactions:
    amount_input = driver.find_element(By.XPATH, "//input[@placeholder='amount']")
    transaction_type_select = driver.find_element(By.XPATH, "//select[@id='type']")
    submit_button = driver.find_element(By.XPath,"//button[@type='submit']")

    amount_input.clear()
    amount_input.send_keys(str(amount))
    
    transaction_type_select.click()
    transaction_type_option = driver.find_element(By.XPATH, f"//option[contains(text(), '{transaction_type}')]")
    transaction_type_option.click()
    
    submit_button.click()

    # Wait for balance to update
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Balance:']")))
    balance_text = driver.find_element(By.XPATH, "//strong[text()='Balance:']/following-sibling::span").text
    print(f"Transaction: {transaction_type} {amount} - Updated Balance: {balance_text}")


    # Wait for 5 seconds
    time.sleep(20)

# Close the browser
driver.quit()
