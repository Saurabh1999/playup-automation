from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys
import getpass


print("\n" ,"******** ENTER PLAYUP CREDENTIAL ***************","\n")
print("email: ",end="")
user_username = input()

try:
    user_pass = getpass.getpass()
except Exception as error:
    print('ERROR', error)


challenge_list = []
print('Enter :')
print("1.Firefox")
print("2.Chrome")

sel = int(input())

if(sel == 1):

	print("Openning Firefox........................") 
	browser = webdriver.Firefox()

else:

	print("Openning Chrome........................") 
	browser = webdriver.Chrome()



browser.get('https://play.playup.com/lobby?modal=signin')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys(user_username)
password.send_keys(user_pass)

browser.find_element_by_xpath("//button[@type='submit']").click()  #SIGN IN
time.sleep(2)

browser.find_element_by_xpath("//button[@class='css-18vq0q3']").click() # Close Verification update dialog
time.sleep(2)
browser.find_element_by_xpath("//button[@class='css-15ir5jy']").click() # Close BBL SPARTAN dialog
time.sleep(3);

type_list = browser.find_elements_by_xpath("//li"); 
print(len(type_list))
for x in type_list:
	if(x.text == "FREE"):                
		print("success")
		x.click()      # CLick FOR FREE LEAGUES


time.sleep(3)
l = browser.find_elements_by_xpath("//a[@class='Tappable-inactive css-rhqy0g']"); # get all free challenge data
for x in l:
	challenge_list.append(x.get_attribute("href")) # get all free challenge link in challenge_list

print("Free Challenge count : ",len(challenge_list))

for challenge_link in challenge_list:
	print("going to --> ",challenge_link)
	browser.get(challenge_link)
	time.sleep(3)
	browser.find_element_by_xpath("//div[@class='css-1ya7mne Tappable-inactive']").click() # click on  \/ button 
																						   #           /\
	time.sleep(3)

	browser.find_element_by_xpath("//div[@class='css-1oswupl Tappable-inactive']").click() # click Autofill 
	time.sleep(2)


	browser.find_element_by_xpath("//button[@class='button-0-11 primary-0-13 block-0-12']").click() # Submit Lineup
	time.sleep(2)


	browser.find_element_by_xpath("//button[@class='css-8b0ko4']").click() # Confirm Lineup

	time.sleep(2)


