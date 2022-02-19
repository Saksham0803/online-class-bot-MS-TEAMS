import pyautogui
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import os.path
from os import path
import sqlite3
import schedule
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# driver = webdriver.Chrome(chrome_options=opt,service_log_path='NUL')
driver = None
URL = "https://teams.microsoft.com"

# put your teams credentials here
CREDS = {'email': '', 'passwd': ''}


def login():
    global driver
    # login required
    print("logging in")
    time.sleep(20)
    pyautogui.press("")              #enter ms teams id in "" 1 letter at a time
    pyautogui.press("")              #eg-
    pyautogui.press("")              # pyautogui.press("s")
    pyautogui.press("")              #  pyautogui.press("a")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("")           #enter password in the same manner
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("enter")
    time.sleep(90)
    teams_joinbtn= driver.find_element_by_xpath('//*[@id="app-bar-2a84919f-59d8-4441-a975-2a8c2643b741"]')
    teams_joinbtn.click()
    time.sleep(20)
    #a = pyautogui.moveTo(44, 198, 5)
    #b = pyautogui.click(44, 198)
    #print(a)
    #print(b)
    #time.sleep(50)
    #c = pyautogui.moveTo(1286, 243, 5)
    #d = pyautogui.click(1286, 243)
    #print(c,d)
    #time.sleep(10)
    #e = pyautogui.moveTo(1220, 290, 5)
    #f = pyautogui.click(1220, 290)
    #print(e,f)


    '''emailField = driver.find_element('//*[@id="i0116"]')
    emailField.click()
    emailField.send_keys(CREDS['email'])
    driver.find_element('//*[@id="idSIButton9"]').click()  # Next button
    time.sleep(5)
    passwordField = driver.find_element('//*[@id="i0118"]')
    passwordField.click()
    passwordField.send_keys(CREDS['passwd'])
    driver.find_element('//*[@id="idSIButton9"]').click()  # Sign in button
    time.sleep(5)
    driver.find_element('//*[@id="idSIButton9"]').click()  # remember login
    time.sleep(5)'''


# return driver


def createDB():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE timetable(class text, start_time text, end_time text, day text)''')
    conn.commit()
    conn.close()
    print("Created timetable Database")


def validate_input(regex, inp):
    if not re.match(regex, inp):
        return False
    return True


def validate_day(inp):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    if inp.lower() in days:
        return True
    else:
        return False


def add_timetable():
    if (not (path.exists("timetable.db"))):
        createDB()
    op = int(input("1. Add class\n2. Done adding\nEnter option : "))
    while (op == 1):
        name = input("Enter class name : ")
        start_time = input("Enter class start time in 24 hour format: (HH:MM) ")
        while not (validate_input("\d\d:\d\d", start_time)):
            print("Invalid input, try again")
            start_time = input("Enter class start time in 24 hour format: (HH:MM) ")

        end_time = input("Enter class end time in 24 hour format: (HH:MM) ")
        while not (validate_input("\d\d:\d\d", end_time)):
            print("Invalid input, try again")
            end_time = input("Enter class end time in 24 hour format: (HH:MM) ")

        day = input("Enter day (Monday/Tuesday/Wednesday..etc) : ")
        while not (validate_day(day.strip())):
            print("Invalid input, try again")
            end_time = input("Enter day (Monday/Tuesday/Wednesday..etc) : ")

        conn = sqlite3.connect('timetable.db')
        c = conn.cursor()

        # Insert a row of data
        c.execute("INSERT INTO timetable VALUES ('%s','%s','%s','%s')" % (name, start_time, end_time, day))

        conn.commit()
        conn.close()

        print("Class added to database\n")

        op = int(input("1. Add class\n2. Done adding\nEnter option : "))


def view_timetable():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM timetable'):
        print(row)
    conn.close()


def joinclass(class_name, start_time, end_time, day):
    global driver
    print("starting")
    time.sleep(20)
    o1_classes = driver.find_element_by_xpath(
        '//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[2]/div/ng-include/div/div')
    o1_classes.click()
    '''if day.lower() == 'monday':
                o1_prac = driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[3]/div/ng-include/div/div')
                o1_prac.click()
                print('its monday')'''
    print("its not monday")
    time.sleep(20)
    try_time = int(start_time.split(":")[1]) + 15
    try_time = start_time.split(":")[0] + ":" + str(try_time)
    print("wait")
    time.sleep(5)

    classes_available = driver.find_elements_by_class_name("name-channel-type")

    for i in classes_available:
        if class_name.lower() in i.get_attribute('innerHTML').lower():
            print("JOINING CLASS ", class_name)
            i.click()
            break
        '''if day.lower() == 'monday':
            o1_prac = driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[3]/div/ng-include/div/div')
            o1_prac.click()
            print('its monday')
        else:
            o1_classes = driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[2]/div/ng-include/div/div')
            o1_classes.click()
            print("its not monday")
            time.sleep(20)'''
        if class_name.lower() == 'comm skills':
            comm_skills = driver.find_element_by_xpath('//*[@id="channel-19:6594a6f74e874c07b789f7cb32a780db@thread.tacv2"]/a/div[1]/span')
            comm_skills.click()
        elif class_name.lower() == 'phy':
            phy = driver.find_element_by_xpath('//*[@id="channel-19:964ca57e903d452c9a65a0f3a9975adb@thread.tacv2"]/a/div[1]/span')
            phy.click()
        elif class_name.lower() == 'maths':
            maths = driver.find_element_by_xpath('//*[@id="channel-19:c72f6d35df5d426fa410afa40c873f82@thread.tacv2"]/a/div[1]/span')
            maths.click()
        elif class_name.lower() == 'eng graphics':
            eng_graphics = driver.find_element_by_xpath('//*[@id="channel-19:283e22f7579142949bfb37d32841efcb@thread.tacv2"]/a/div[1]/span')
            eng_graphics.click()
        elif class_name.lower() == 'evn studies':
            evn_studies = driver.find_element_by_xpath('//*[@id="channel-19:a3cb2421f6d34bb09f9f1e949b055181@thread.tacv2"]/a/div[1]/span')
            evn_studies.click()
        elif class_name.lower() == 'C':
            C = driver.find_element_by_xpath('//*[@id="channel-19:80101bccf4074a488b3caffe32b66e46@thread.tacv2"]/a/div[1]/span')
            C.click()
        elif class_name.lower() == 'manu process':
            manu_process = driver.find_element_by_xpath('//*[@id="channel-19:aa4289becbdb4464bbdda00d9f1c8746@thread.tacv2"]/a/div[1]/span')
            manu_process.click()
        elif class_name.lower() == 'C lab':
            C_lab = driver.find_element_by_xpath('// *[ @ id = "channel-19:ab24ef61ad3c4cbb8718271b605e28f7@thread.tacv2"] / a / div[1] / span')
            C_lab.click()


    time.sleep(4)

    try:
        joinbtn = driver.find_element_by_class_name("ts-calling-join-button")
        joinbtn.click()
        '''#m1639328481436 > calling-join-button > button
        #AAMkAGJhZmZhNDAwLWQzNzgtNGJiYS05MDFmLTc3Nzc2MWJkNzlhMwFRAAgI2eEn9jDAAEYAAAAAhOyTP0GgWEWG7rz_ThoP4QcAgCPNRzLU8UOAH7ODC5rxvQAAAAABDQAAgCPNRzLU8UOAH7ODC5rxvQAAAsf8ewAAEA\=\= > div.root-74.node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__cardBody--1kiA0 > button
        <span ng-if="!ctrl.roundButton" translate-once="calling_jumpIn" aria-label="Join">Join</span>
        MP_xpath=//*[@id="id__102"]
        prog._xpath=//*[@id="id__108"]
        evs=//*[@id="id__114"]
        joinbtn = driver.find_element_by_xpath("//*[@id='AAMkAGJhZmZhNDAwLWQzNzgtNGJiYS05MDFmLTc3Nzc2MWJkNzlhMwFRAAgI2d7MdvOAAEYAAAAAhOyTP0GgWEWG7rz_ThoP4QcAgCPNRzLU8UOAH7ODC5rxvQAAAAABDQAAgCPNRzLU8UOAH7ODC5rxvQAAEHrKDgAAEA==']/div[2]/button")
        joinbtn.click()
        joinbtn1 = driver.find_elemnent_by_xpath('//*[@id="AAMkAGJhZmZhNDAwLWQzNzgtNGJiYS05MDFmLTc3Nzc2MWJkNzlhMwFRAAgI2d_VoV1AAEYAAAAAhOyTP0GgWEWG7rz_ThoP4QcAgCPNRzLU8UOAH7ODC5rxvQAAAAABDQAAgCPNRzLU8UOAH7ODC5rxvQAADMWacAAAEA=="]/div[2]/button')
        joinbtn1.click()
        joinbtn2 = driver.find_element_by_xpath('//*[@id="id__158"]')
        joinbtn2.click()'''
    except:
        # join button not found
        # refresh every minute until found
        k = 1
        while (k <= 15):
            print("Join button not found, trying again")
            time.sleep(60)
            joinclass(class_name, start_time, end_time, day)
            # schedule.every(1).minutes.do(joinclass,class_name,start_time,end_time)
            k += 1
        print("Seems like there is no class today.")

    time.sleep(4)
    webcam = driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    if (webcam.get_attribute('title') == 'Turn camera off'):
        webcam.click()
    time.sleep(1)

    microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
    if (microphone.get_attribute('title') == 'Mute microphone'):
        microphone.click()

    time.sleep(1)
    joinnowbtn = driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()

    # now schedule leaving class
    tmp = "%H:%M"

    class_running_time = datetime.strptime(end_time, tmp) - datetime.strptime(start_time, tmp)

    time.sleep(class_running_time.seconds)

    driver.find_element_by_class_name("ts-calling-screen").click()

    driver.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[3]').click()  # come back to homepage
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="hangup-button"]').click()
    print("Class left")


def start_browser():
    global driver


    driver = webdriver.Chrome(options=opt, service_log_path='NUL')

    driver.get(URL)

    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    login()


def sched():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    start_browser()
    for row in c.execute('SELECT * FROM timetable'):
        # schedule all classes
        name = row[0]
        start_time = row[1]
        end_time = row[2]
        day = row[3]

        if day.lower() == "monday":
            schedule.every().monday.at(start_time).do(joinclass, name, start_time, end_time, day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
            joinclass(name, start_time, end_time, day)
        if day.lower() == "tuesday":
            schedule.every().tuesday.at(start_time).do(joinclass, name, start_time, end_time , day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
            joinclass(name, start_time, end_time, day)
        if day.lower() == "wednesday":
            schedule.every().wednesday.at(start_time).do(joinclass, name, start_time, end_time,day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
            joinclass(name, start_time, end_time, day)
        if day.lower() == "thursday":
            schedule.every().thursday.at(start_time).do(joinclass, name, start_time, end_time,day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
            joinclass(name, start_time, end_time, day)
        if day.lower() == "friday":
            schedule.every().friday.at(start_time).do(joinclass, name, start_time, end_time, day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
            joinclass(name, start_time, end_time, day)
        if day.lower() == "saturday":
            schedule.every().saturday.at(start_time).do(joinclass, name, start_time, end_time, day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))
        if day.lower() == "sunday":
            schedule.every().sunday.at(start_time).do(joinclass, name, start_time, end_time, day)
            print("Scheduled class '%s' on %s at %s" % (name, day, start_time))

    # Start browser
    #start_browser()
    '''for row in c.execute('SELECT * FROM timetable'):
        # schedule all classes
        name = row[0]
        start_time = row[1]
        end_time = row[2]
        day = row[3]
        joinclass(name, start_time, end_time)'''
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        #print("trying")
        time.sleep(1)


if __name__ == "__main__":
    # joinclass("Maths","15:13","15:15","sunday")
    op = int(input(("1. Modify Timetable\n2. View Timetable\n3. Start Bot\nEnter option : ")))

    if (op == 1):
        add_timetable()
    if (op == 2):
        view_timetable()
    if (op == 3):
        sched()