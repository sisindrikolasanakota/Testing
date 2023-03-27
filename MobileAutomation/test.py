import subprocess

import time

#create a new contact
subprocess.run("adb shell am start -n com.android.contacts/com.android.contacts.activities.PeopleActivity")#contact launch
subprocess.run("adb shell input tap 900 1950")#clickonPlusbutton on contact to create the new name
subprocess.run("adb shell input text sisi",shell=True)#enterFirstName
time.sleep(2)
subprocess.run("adb shell input keyevent 4")#back
subprocess.run("adb shell input tap 700 1350")#[204,1282][912,1444]#clickonphone text
subprocess.run("adb shell input text 9100359527") # enter phone number
time.sleep(2)
subprocess.run("adb shell input tap 950 250")#[888,156][1080,300]#save the contact
subprocess.run("adb shell input keyevent 4")#back
subprocess.run("adb shell input keyevent 4")#back to come home page
time.sleep(2)

#edit the contact
subprocess.run("adb shell am start -n com.android.contacts/com.android.contacts.activities.PeopleActivity")
time.sleep(2)
subprocess.run("adb shell input text a",shell=True)
subprocess.run("adb shell input tap 550 750")#[0,669][1080,837] select sisi name
subprocess.run("adb shell input tap 900 250")#[816,156][960,300] select edit button
time.sleep(2)
subprocess.run("adb shell input tap 550 1100")#[204,1025][912,1187] select the cursor after sisi
subprocess.run("adb shell input text ndri",shell=True) #name edit (enter name add)(ndri)
subprocess.run("adb shell input tap 950 250")#[888,156][1080,300]#save
subprocess.run("adb shell input keyevent 4")#back
subprocess.run("adb shell input keyevent 4")#back
time.sleep(2)

#delete the contact
subprocess.run("adb shell am start -n com.android.contacts/com.android.contacts.activities.PeopleActivity")
time.sleep(2)
subprocess.run("adb shell input tap 550 750")#[0,669][1080,837] select sisindri name
subprocess.run("adb shell input tap 1000 225")#[960,156][1080,300] select 3 dots
subprocess.run("adb shell input tap 750 370")#[528,339][1020,404] delete
subprocess.run("adb shell input tap 700 1225")#[567,1124][787,1268] select delete again
subprocess.run("adb shell input keyevent 4")#back