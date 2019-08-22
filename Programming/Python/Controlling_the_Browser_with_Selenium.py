from selenium import webdriver
'''Intracting with the Browser and webpages using Selenium Module. More on : https://selenium-python.readthedocs.io/'''

#Creating the instance of Firefox WebDriver:
browser = webdriver.Firefox()

#########
#Example 1:

# #finding element from the webpage:
browser.get('https://amazon.com') # navigate to a page given by the URL
element = browser.find_element_by_css_selector('#nav-xshop > a:nth-child(2)')
element.click()

# # finding element from the search bar:
browser.back()
searchElement= browser.find_element_by_css_selector('#twotabsearchtextbox')
searchElement.send_keys('coffee')
searchElement.submit()

#########
#Example 2:

#Reading the content of the webpage:
website = browser.get('https://houdaaynaou.com')
about= browser.find_element_by_css_selector('.nav-container > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
about.click()
read_text = browser.find_element_by_css_selector('body > main:nth-child(2) > p:nth-child(4)')
print(read_text.text)


#########
#Example 3:

#Reading html:
website = browser.get('https://selenium-python.readthedocs.io')
webHtml= browser.find_element_by_css_selector('html')
print(webHtml.text)



