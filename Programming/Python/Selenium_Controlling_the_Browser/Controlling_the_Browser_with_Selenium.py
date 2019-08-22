from selenium import webdriver
'''Intracting with the Browser and webpages using Selenium Module. More on : https://selenium-python.readthedocs.io/'''


browser = webdriver.Firefox()                                                   #Creating the instance of Firefox WebDriver:
browser.get('https://amazon.com')                                               #Navigate to a page given by the URL
element = browser.find_element_by_css_selector('#nav-xshop > a:nth-child(2)')   #CSS selector of clickable element
element.click()                                                                 #clicking





