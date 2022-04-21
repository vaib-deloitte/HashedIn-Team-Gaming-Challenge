#importing webdriver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
def test_game():
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.maximize_window()
#opening url
    driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("Atul")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Atul@12345")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='signin']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[contains(text(),'Manage Books')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//div[contains(text(),'List Books')]").click()
    time.sleep(5)
    #for view pdf
   # driver.find_element(By.XPATH,"//a[contains(text(),'View PDF')]").click()
    #time.sleep(20)
    #for download pdf
    #driver.find_element(By.XPATH,"//a[contains(text(),'Download PDF')]").click()
    #time.sleep(20)
    #for update book
    #check  update books button
    driver.find_element(By.XPATH,"//button[contains(text(),'Update Book')]").click()
    time.sleep(20)
    #for choose file
    driver.find_element(By.XPATH,"//input[@id='myFile']").send_keys("C:/Users/vkrishana/Documents/file.docx")
    time.sleep(10)
    #for choose file for update
    driver.find_element(By.XPATH,"//button[contains(text(),'Update Now')]").click()
    time.sleep(20)