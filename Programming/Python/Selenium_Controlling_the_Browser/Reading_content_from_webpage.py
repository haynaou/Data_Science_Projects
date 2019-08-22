from selenium import webdriver

browser = webdriver.Firefox()

#Reading content from a webpage:
website = browser.get('https://houdaaynaou.com')                                                                       #navigate to a page given by the URL
about = browser.find_element_by_css_selector('.nav-container > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')    #navigate to 'about' section of the page
about.click()                                                                                                          #clicking
read_text = browser.find_element_by_css_selector('body > main:nth-child(2) > p:nth-child(4)')                          #CSS selector of the selected text
print(read_text.text)                                                                                                  #printing text




#Reading html:
website = browser.get('https://selenium-python.readthedocs.io')    #launching new page
webHtml = browser.find_element_by_css_selector('html')             #selecting web html
print(webHtml.text)                                                #printing text


