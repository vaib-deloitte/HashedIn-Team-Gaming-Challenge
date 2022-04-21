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
    driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("parvesharma")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("12345@django")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='signin']").click()
    time.sleep(5)
    #check for manage book button and its clickable or not
    driver.find_element(By.XPATH,"//div[contains(text(),'Manage Books')]").click()
    time.sleep(10)
    #check for Add book button
    driver.find_element(By.XPATH,"//div[contains(text(),'Add Book')]").click()
    time.sleep(10)
    element = driver.find_element(By.XPATH, "//h3[contains(text(),'Hi, parvesharma')]")
    assert element.text == "Hi, parvesharma"
    print(" Valid Massage")
    #Add book title
    driver.find_element(By.XPATH,"//input[@name='title']").send_keys("RocketStem")
    time.sleep(10)
    #check for choose pdf for cover
    driver.find_element(By.XPATH,"//input[@id='cover']").send_keys("C:/Users/vkrishana/Documents/co.jpg")
    time.sleep(20)
    #check for choose pdf for file
    driver.find_element(By.XPATH,"//input[@id='file']").send_keys("C:/Users/vkrishana/Documents/file.docx")
    time.sleep(10)
    # driver.find_element(By.XPATH,'//select[@name="interest_id"]').click()
    #check for drop down and click on it
    time.sleep(5)
    x=Select(driver.find_element(By.NAME,'interest_id'))
    time.sleep(10)
    #for selection of intrest
    x.select_by_visible_text("Future Technology")
    time.sleep(10)
    #check for the submit button
    driver.find_element(By.XPATH,"//button[contains(text(),'Submit')]").click()
    time.sleep(10)