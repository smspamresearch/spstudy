from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Set up the Selenium driver
driver = webdriver.Chrome()

# Navigate to the Google Messages web login page
driver.get("https://messages.google.com/web")

# Wait for the user to log in
input("Press Enter after logging in")

try:
    # Search for the recipient's name or phone number
    driver.find_element(By.XPATH, "/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a").click()
    print("debugging point 1...ok")

    # Search for the recipient's name or phone number
    driver.find_element(By.XPATH, "/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a").click()
    search_box = driver.find_element(By.XPATH, "/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/mat-chip-listbox/div/input")
    print("searchBox")
    time.sleep(10)
    search_box.send_keys("CONTACT NAME OR NUMBER")
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contacts-list/div/mw-contact-row/div/div/div[1]/mw-bold-matching-text/b").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea").send_keys("SMS TEXT HERE.........")
    time.sleep(5)

    print("debugging point 2...ok")

    send = driver.find_element(By.XPATH, "/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-message-send-button/div/mw-message-send-button/button")
    time.sleep(2)
    print("debugging point 3...ok")
    send.click()
       # Wait for the message to be sent
    time.sleep(10)

    # Close the browser window
    driver.quit()

except Exception as e:
    print(f"An exception occurred {e}")
    pass


