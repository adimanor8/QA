#Import Sellenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from selenium.webdriver.support.ui import Select
import time
#Add the folder of the driver
driver=webdriver.Chrome("chromedriver.exe")
#Go to Heroku computers App page
driver.get("http://computer-database.herokuapp.com/computers")
#test 1...

#Press on Add new Computer Button
driver.find_element_by_id("add").click()


#error handling & Verify add computer name field appear
try:
    driver.find_element_by_id("name").is_displayed()
except NoSuchElementException:
    print("Error:The element Not exist")

#test2


#Insert Valid info on the fields
#getting today date
today=date.today()
#getting the date one month from now
oneMonthFromNow=str(today.year)+ "-"+str(today.month+1) + "-"+str(today.day)
#send the name of computer
driver.find_element_by_id("name").send_keys("Adi")
#send the date of today
driver.find_element_by_id("introduced").send_keys(str(date.today()))
#send the date one month from now
driver.find_element_by_id("discontinued").send_keys(oneMonthFromNow)
#select the drop-down
select=Select(driver.find_element_by_id("company"))
#Select "apple"
select.select_by_value('1')
#Press on cancel button
driver.find_element_by_xpath('//*[@id="main"]/form/div/a').click()

#Verify you are on main page&the computer not created

try:
    el = driver.find_element_by_xpath('//*[@id="main"]/div[1]')
    if el.is_displayed():
        raise Exception ("Error the computer created")
except:
    pass


#test3

#Press on Add new Computer Button
driver.find_element_by_id("add").click()
#send the name of computer
compName="Adi"+str(time.time())
driver.find_element_by_id("name").send_keys(compName)
#send the date of today
driver.find_element_by_id("introduced").send_keys(str(date.today()))
#send the date one month from now
driver.find_element_by_id("discontinued").send_keys(oneMonthFromNow)
#select the drop-down
select=Select(driver.find_element_by_id("company"))
#Select "apple"
select.select_by_value('1')
#press on "Create this computer"
driver.find_element_by_css_selector('input[value="Create this computer"]').click()
try:
    el = driver.find_element_by_xpath('//*[@id="main"]/div[1]').is_displayed()

except NoSuchElementException:
    print("Error:The element Not exist")


#test4

#send the new computer name&Press Filter by name button
driver.find_element_by_id("searchbox").send_keys(compName)
driver.find_element_by_id("searchsubmit").click()
#Verify you get the computer name
try:
    driver.find_element_by_xpath('//*[@id="main"]/table').is_displayed()
except NoSuchElementException:
    print("Error:The element Not exist")


#Test5

driver.find_element_by_id("searchbox").send_keys("SM@@")
driver.find_element_by_id("searchsubmit").click()
#verify Nothing to display message appear
try:
    driver.find_element_by_xpath('//*[@id="main"]/div[2]/em').is_displayed()
except NoSuchElementException:
    print("Error:The element Not exist")





#test6
driver.find_element_by_id("add").click()
driver.find_element_by_css_selector('input[value="Create this computer"]').click()
try:
    driver.find_element_by_css_selector('input[value="Create this computer"]').is_displayed()
except NoSuchElementException:
    print("Error:The element Not exist")
#test7

driver.find_element_by_id("name").send_keys("@@AA@@@")
driver.find_element_by_id("introduced").send_keys("AAA")
driver.find_element_by_id("discontinued").send_keys("BBB")
select=Select(driver.find_element_by_id("company"))
#Select "apple"
select.select_by_value('1')
driver.find_element_by_css_selector('input[value="Create this computer"]').click()
try:
    driver.find_element_by_css_selector('input[value="Create this computer"]').is_displayed()
except NoSuchElementException:
    print("Error:The element Not exist")












