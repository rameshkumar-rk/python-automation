from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html") 
messagefield=driver.find_element_by_xpath('//*[@id="user-message"]')
messagefield.send_keys('hello world')
showmessagebutton=driver.find_element_by_xpath('//*[@id="get-input"]/button')
showmessagebutton.click()