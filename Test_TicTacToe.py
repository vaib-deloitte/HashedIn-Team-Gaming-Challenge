#importing webdriver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
def test_game():
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.maximize_window()
#opening url
    driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("Alex")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Alex@123")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='signin']").click()
#clicking the tictactoe game
    driver.find_element(By.XPATH,"//div[contains(text(),'Play Tic-Tac-Toe')]").click()
#check for the page and massage on the game page
    time.sleep(10)
#check for roomID
    driver.find_element(By.XPATH,"//input[@id='room']").send_keys("3")
    time.sleep(3)
#drop selection
   # driver.find_element(By.XPATH,"//select[@name='character_choice']").click()

#for starting game
    driver.find_element(By.XPATH,"//button[@class='btn primarybtn']").click()
    time.sleep(5)
    time.sleep(5)
    element = driver.find_element(By.XPATH, "//h3[contains(text(),'Hi, Alex')]")
    assert element.text == "Hi, Alex"
    print("valid massage ")
#click on empty block
    driver.find_element(By.XPATH,"//div[@id='game_board']//div[2]//div[2]").click()
#clicking without waiting for oponent
    time.sleep(5)
#driver.find_element(By.XPATH,"//div[@id='playingbox']//div[1]//div[3]").click()
    driver.find_element(By.XPATH,"//div[@id='playingbox']//div[1]//div[2]").click()

    time.sleep(20)
    driver.find_element(By.XPATH,"//div[3]//div[2]").click()
    time.sleep(20)
   #for verifying the goto dashborad button
    driver.find_element(By.XPATH,"//a[contains(text(),'Go To Dashboard')]").click()
    #time.sleep(20)
   #for verifying play again button
    #driver.find_element(By.XPATH,"//button[contains(text(),'Play Again')]").click()
    #time.sleep(10)

