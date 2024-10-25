import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


email = os.getenv('ASTRO_EMAIL')
password = os.getenv('ASTRO_PASSWORD')

# Set up Chrome options
chrome_options = Options()

# Optional: Run Chrome in headless mode (no browser window)
chrome_options.add_argument('--headless')

# Specify the path to chromedriver
service = Service('/usr/local/bin/chromedriver')  # Update the path if necessary

# Create the driver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the login page
    driver.get('https://www.astro.com/cgi/awd.cgi')

    # Wait until the email field is present
    wait = WebDriverWait(driver, 1)
    email_field = wait.until(EC.presence_of_element_located((By.NAME, 'mail')))
    password_field = driver.find_element(By.NAME, 'pwrd')



    # Enter the credentials
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Submit the form by clicking the login button
    login_button = driver.find_element(By.NAME, 'submit')
    login_button.click()

    # Wait for the login process to complete
    # For example, wait until the "My Astro" link is present
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'My Astro')))

    # Now navigate to the general horoscope page
    driver.get('https://www.astro.com/cgi/hk.cgi?lang=e')

    # Wait until the general horoscope text is present
    general_horoscope_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hktext')))
    general_horoscope_text = general_horoscope_element.text

    print("\nYour General Daily Horoscope:")
    print(general_horoscope_text)

    # Now navigate to the love horoscope page
    driver.get('https://www.astro.com/cgi/hk.cgi?lang=e&inlove=1')

    # Wait until the love horoscope text is present
    love_horoscope_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hktext')))
    love_horoscope_text = love_horoscope_element.text

    print("\nYour Love Horoscope:")
    print(love_horoscope_text)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()