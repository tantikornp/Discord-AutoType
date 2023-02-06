import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os, shutil
import random
import selenium

driver = webdriver.Chrome()

driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 
username = ''
password = ''

# Copy the URL of channel where you wanna send messages and paste below
channelURL = "https://discord.com/channels/882366346707472455/916402999759368193"

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email
username_input = driver.find_element_by_name('email')
username_input.send_keys(username)

# Initialize and input password
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

# Initialize and login
login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
login_button.click()

print(">>Login Complete!")
time.sleep(10)

driver.get(channelURL)
print(">Opening The Server Link...")
time.sleep(5)

massage_list = ['เข้มแข็งไว้นะ', 'ร่าเริงหน่อยสิ', 'ใจเย็นๆ นะ',
                'อย่าเพิ่งท้อออออ',
                'ชิวววว',
                'อย่าคิดมากเลยน่าาา',
                'อย่ากังวลไปเลยย',
                'เป็นกำลังใจให้นะะ',
                'มันไม่ได้แย่ขนาดนั้นมั้งง',
                'ทำตัวให้สดชื่นหน่อยยยย',
                'ลืมมันไปปปปป' ,
                'ไม่ต้องเก็บมาใส่ใจ',
                'มองโลกในแง่ดีกันบ้าง',
                'เรื่องแบบนี้อาจเกิดกับใครก็ได้',
                'สู้เค้า ๆๆ',
                'สู้ต่อไปปปป',
                'ก้าวต่อไปปป',
                'อย่าหยุดดด', 'สู้ๆๆๆๆๆๆ',
                'สู้ดิเฮ้ยยยย',
                'อย่ายอมแพ้',
                'ไม่ต้องหมดกำลังใจจจ',
                'เดี๋ยวมันก็ดีเองงงงงงง',
                'เดี๋ยวเราก็ผ่านมันไปได้นะจ๊ะ',
                'เราทำด้ายยย', 'มาลุยกันยาวๆไปครับ']

#number of time you wanna change
x = 10
i = 0

# Msg Sending
while(i <= x):

    try:
        time.sleep(random.randint(125,250))

        x = random.randint(0,10)

        if x < 5:
            my_msg = massage_list[random.randint(0,25)]+massage_list[random.randint(0,25)]
            print(my_msg)
        else:
            my_msg = massage_list[random.randint(0,25)]
            print(my_msg)

        msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')
        msg_input.send_keys(my_msg)
        msg_input.send_keys(Keys.ENTER)

    except selenium.common.exceptions.NoSuchElementException:
        msg_input.send_keys(Keys.ENTER)
        time.sleep(2)

    i+=1
    print(">Numbers of Messages sent: "+str(i))

    time.sleep(2)

print("Its Done!")