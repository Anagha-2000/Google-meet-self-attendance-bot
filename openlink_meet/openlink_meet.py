import webbrowser
import time
import threading
# importing webdriver from selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from pygame._sdl2 import get_num_audio_devices, get_audio_device_name #Get playback device names
from pygame import mixer #Playing sound


url = 'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.159644724.887115149.1602468384-1763864472.1602468384&flowName=GlifWebSignIn&flowEntry=ServiceLogin'




# Here Chrome will be used 
#driver = webdriver.Chrome("D://openlink_meet/chromedriver.exe")
chrome_options = Options()
#chrome_options.add_argument('use-fake-device-for-media-stream')
chrome_options.add_argument('use-fake-ui-for-media-stream')
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome("D://openlink_meet/chromedriver.exe",chrome_options=chrome_options)



# Opening the website 
driver.get(url) 

# geeting the button by class name 
SignIn = driver.find_element_by_id("identifierId") 

# clicking on the button 
SignIn.send_keys("Enter email id here")
SignIn.send_keys(Keys.ENTER)

driver.implicitly_wait(10)

EnterPass =driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
EnterPass.send_keys("Enter password here")
EnterPass.send_keys(Keys.ENTER)

JoinLink =driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]") 
JoinLink.click()

Enterlink =driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input")
Enterlink.send_keys("Enter your google meet link here")
Enterlink.send_keys(Keys.ENTER)

#Dismiss =driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div")
#Dismiss.click()

Mute = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]")
Mute.click()

CamOff = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div")
CamOff.click()

#driver.implicitly_wait(10)

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)

JoinNow =WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")))
JoinNow.click()

TurnOnCaptions = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[3]/div[2]/div/span/span/div/div[2]")
TurnOnCaptions.click()

Caption_tray = WebDriverWait(driver,30,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[5]")))
Captions = WebDriverWait(driver,30,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[5]/div/div[2]")))
count = 0
staleElement = True
while staleElement :

        try :

            Caption_tray = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[5]")
            Captions = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[5]/div/div[2]")
            if Captions.is_displayed() :
                    Caption_text= Captions.text
                    Caption_text.strip().lower()
                    print(Caption_text)
                    
                    
        except(StaleElementReferenceException):

                staleElement = True

        except(NoSuchElementException) :
                
                staleElement = True

        changed_numstudents = int(students.text)
        print(changed_numstudents)
        if changed_numstudents > Total_numStudents :
                Total_numStudents = changed_numstudents
        elif changed_numstudents < Total_numStudents :
        
                if changed_numstudents <= math.floor(0.2*Total_numStudents):  
                                EndCall=driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div/span")
                                EndCall.click()   
                                
        if count ==0 :

                 words = (“roll number 1”,“john” , “jon” , “jondoe” ,”jondo” , “jondove” , “johndoe” , “johndove” , “doe” , “dove”)
                 if any(name in Caption_text for name in words): 

                        UnMute = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[1]/div/div/div")
                        UnMute.click()
                        mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
                        mixer.music.load("Path to recorded audio file")
                        mixer.music.play()
                        time.sleep(4)
                        mixer.music.stop()
                        UnMute.click()
                        count+=1
        
        
            

            

