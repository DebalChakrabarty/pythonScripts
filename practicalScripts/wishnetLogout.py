from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'/home/dchakrabarty/geckodriver')
driver.get('http://192.168.183.201:9082/WISHN/Login.jsp')
elem=driver.find_element_by_css_selector('#search-form > a:nth-child(2)')
elem.click()



driver.switch_to.alert.accept()
