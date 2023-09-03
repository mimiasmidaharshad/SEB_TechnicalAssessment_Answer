from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# Navigate to the URL
url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
driver.get(url)

# Log in as Bank Manager
driver.find_element_by_xpath("//button[contains(text(), 'Bank Manager Login')]").click()
time.sleep(2)  # Wait for the animation

# Create customers
customer_data = [
    ("Christopher", "Connely", "L789C349"),
    ("Frank", "Christopher", "A897N450"),
    ("Christopher", "Minka", "M098Q585"),
    ("Connely", "Jackson", "L789C349"),
    ("Jackson", "Frank", "L789C349"),
    ("Minka", "Jackson", "A897N450"),
    ("Jackson", "Connely", "L789C349")
]

for first_name, last_name, postcode in customer_data:
    driver.find_element_by_xpath("//button[contains(text(), 'Add Customer')]").click()
    driver.find_element_by_xpath("//label[contains(text(), 'First Name')]/following-sibling::input").send_keys(first_name)
    driver.find_element_by_xpath("//label[contains(text(), 'Last Name')]/following-sibling::input").send_keys(last_name)
    driver.find_element_by_xpath("//label[contains(text(), 'Post Code')]/following-sibling::input").send_keys(postcode)
    driver.find_element_by_xpath("//button[contains(text(), 'Add Customer')]").click()
    time.sleep(1)

# Go to Customers Tab
driver.find_element_by_xpath("//button[contains(text(), 'Customers')]").click()
time.sleep(2)

# Verify customers in the table
customer_names = [f"{first_name} {last_name}" for first_name, last_name, _ in customer_data]
table_rows = driver.find_elements_by_xpath("//table[@class='table table-bordered']/tbody/tr")

for row in table_rows:
    name = row.find_element_by_xpath(".//td[1]").text
    assert name in customer_names, f"Customer {name} not found in the table"

# Delete specific customers
customers_to_delete = [
    ("Jackson", "Frank", "L789C349"),
    ("Christopher", "Connely", "L789C349")
]

for first_name, last_name, postcode in customers_to_delete:
    driver.find_element_by_xpath("//button[contains(text(), 'Customers')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Delete')]").click()
    driver.find_element_by_xpath("//label[contains(text(), 'First Name')]/following-sibling::input").send_keys(first_name)
    driver.find_element_by_xpath("//label[contains(text(), 'Last Name')]/following-sibling::input").send_keys(last_name)
    driver.find_element_by_xpath("//label[contains(text(), 'Post Code')]/following-sibling::input").send_keys(postcode)
    driver.find_element_by_xpath("//button[contains(text(), 'Delete')]").click()
    time.sleep(1)

# Close the browser
driver.quit()
