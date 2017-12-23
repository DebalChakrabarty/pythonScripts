from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'/home/dchakrabarty/geckodriver')
driver.get('http://192.168.183.201:9082/WISHN/Login.jsp')
elem=driver.find_element_by_css_selector('input.input_field:nth-child(4)')
elem2=driver.find_element_by_css_selector('input.input_field:nth-child(6)')
elem.send_keys('Debal_inet')
elem2.send_keys('Counter123!')
elem.submit()
