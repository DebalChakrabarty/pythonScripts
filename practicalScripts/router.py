from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'/home/dchakrabarty/geckodriver')
driver.get("http://admin:admin@192.168.0.1")

