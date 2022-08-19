import datetime
# import os
import random
import test
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

fstop_username = ''
fstop_password = ''

system_username = ''
system_password = ''

def punch():
    global driver
    driver = webdriver.Chrome('C:\chromedriver.exe')

    driver.get("http://wk.fstop.com.tw:8000/eh/login")
    username = driver.find_element(By.ID, 'username')
    username.send_keys(fstop_username)
    time.sleep(0.5)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(fstop_password)
    login_btn = driver.find_element(By.ID, 'loginSubmit')
    login_btn.click()

    # week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    # today = week_list[datetime.datetime.now().weekday()] // 星期X
    # today = datetime.datetime.now() # 8/9
    # print(today)
    today = datetime.datetime.now().isoweekday()  # 2
    # print(today)

    value = driver.find_element(By.NAME, f'blueFrame:blueFrame_body:customers:3:rows:1:days:{today}:day:day')
    # print("====")
    # print(value.text)
    # try:
    if value == None:
        value.send_keys(8)
    else:
        value.clear()
        driver.refresh()
        value = driver.find_element(By.NAME, f'blueFrame:blueFrame_body:customers:3:rows:1:days:{today}:day:day')
        value.send_keys(8)

    #     else:
    #         value.clear()
    #         driver.refresh()
    #         time.sleep(2)
    #         value.send_keys(8)
    # except StaleElementReferenceException as e:
    #     print(e.msg)
    # else:
    #     value.send_keys(8)
    # finally:
    #     driver.quit()

    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    time.sleep(2)
    only_click = driver.find_element(By.NAME, 'blueFrame:blueFrame_body:submitButtonTop')
    only_click.click()

    print('========================')

    driver.get("https://eip.systex.com/athena/")
    id = driver.find_element(By.ID, 'userid_input')
    id.send_keys(system_username)
    pwd = driver.find_element(By.ID, 'password')
    pwd.send_keys(system_password)
    btn = driver.find_element(By.XPATH, '//*[@id="loginform"]/table[2]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/div/a[1]/img')
    btn.click()
    try:
        time.sleep(3)
        arrive = driver.find_element(By.LINK_TEXT,
                            '今日出勤登打')
        arrive.click()
    except NoSuchElementException as e:
        print(e)
        driver.refresh()
        time.sleep(7)
        arrive = driver.find_element(By.LINK_TEXT,
                                     '今日出勤登打')
        arrive.click()
    # driver.close()

    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])
    # try:
    hour = Select(driver.find_element(By.ID,'startHH'))
    # except NoSuchElementException as e:
        # print (e)

    # hour.click()
    hour.select_by_value('8')

    min_choice = Select(driver.find_element(By.ID,'startMM'))
    mins = random.randint(50,60)
    print(mins)
    # mins=60
    if mins == 60:
        hour.select_by_value('9')
        min_choice.select_by_value('00')
    else:
        min_choice.select_by_value(str(mins))

    location = Select(driver.find_element(By.ID,'locationFirst'))
    # today = datetime.datetime.now().isoweekday()
    location.select_by_value('工作地點')
    location_sec = Select(driver.find_element(By.ID,'locationSecond'))
    if today == 5:
        location_sec.select_by_value('北區_鼎盛(松江)')
    else:
        location_sec.select_by_value('北區_恆逸復北12、14、16F')

    temp = random.randint(0,9)
    temp_today = driver.find_element(By.ID,'temp')
    temp_today.send_keys(f'36.{temp}')

    # driver.find_element(By.ID,'button_save').click()


    time.sleep(3)
    # driver.quit()
    # os.system('exit')

punch()
