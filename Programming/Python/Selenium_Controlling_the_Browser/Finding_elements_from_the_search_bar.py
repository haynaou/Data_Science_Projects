from selenium import webdriver
'''Intracting with the Browser and webpages using Selenium Module. More on : https://selenium-python.readthedocs.io/'''


browser = webdriver.Firefox()                                                   #Creating the instance of Firefox WebDriver
browser.get('https://amazon.com')                                               # navigate to a page given by the URL
searchElement = browser.find_element_by_css_selector('#twotabsearchtextbox')    #Search bar css find_element_by_css_selector
searchElement.send_keys('coffee')                                               #Word to search
searchElement.submit()                                                          #Submitting the research