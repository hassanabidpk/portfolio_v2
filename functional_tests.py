from selenium import webdriver

browser = webdriver.Chrome('/Users/hassanabid/Documents/hassan/open_source/hassan_portfolio/chromedriver')
browser.get('http://localhost:8000')

assert 'Hassan' in browser.title
