import time
from selenium import webdriver

# Replace 'your_url' with the URL you want to visit
url = 'https://www.youtube.com/watch?v=wlUKHoPszEs'

# Create a Chrome browser instance
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get(url)

# Now you can interact with the webpage using Selenium commands
time.sleep(10)

# For example, print the page title
print(f'Page title: {driver.title}')



# Don't forget to close the browser when you're done
driver.quit()
