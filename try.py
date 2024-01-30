from selenium import webdriver
import time as t

# Set up the WebDriver (you may need to download the appropriate driver for your browser)
# Example: ChromeDriver - https://sites.google.com/chromium.org/driver/
# driver = webdriver.Chrome()  # Update the path to the location of your chromedriver executable
driver2 = webdriver.Chrome()
# Open the website
mail = "xx@xx.xx"
print(mail)
driver2.get('https://devfolio.co/signup?from=https%3A%2F%2Fproductathon-ai.devfolio.co%2F')
t.sleep(10)
inputs = driver2.find_element("tag name",'input')
inputs.send_keys(mail)
buttons = driver2.find_elements("tag name",'button')
print(buttons)
for button in buttons:
    if button.text == "Continue":
        button.click()
        break
t.sleep(10)

