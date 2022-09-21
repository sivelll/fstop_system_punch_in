import datetime
import random
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# ,chrome_options=options
s = Service('C:\chromedriver.exe')
driver = webdriver.Chrome(service=s)

fstop_username = ''
fstop_password = ''

system_username = ''
system_password = ''

def eHour():
    driver.get("http://wk.fstop.com.tw:8000/eh/login")
    username = driver.find_element(By.ID, 'username')
    username.send_keys(fstop_username)
    time.sleep(0.5)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(fstop_password)
    login_btn = driver.find_element(By.ID, 'loginSubmit')
    login_btn.click()
    print('完成 eHour 登入')

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

    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    time.sleep(2)
    only_click = driver.find_element(By.NAME, 'blueFrame:blueFrame_body:submitButtonTop')
    only_click.click()

    print('完成 eHour 打卡 ， 即將前往 System EIP 打卡')


def system_login():
    driver.get("https://eip.systex.com/UOF/Login.aspx?ReturnUrl=%2fUOF")
    id = driver.find_element(By.ID, 'txtAccount')
    id.send_keys(system_username)
    pwd = driver.find_element(By.ID, 'txtPwd')
    pwd.send_keys(system_password)
    btn = driver.find_element(By.XPATH, '//*[@id="btnSubmit"]')
    btn.click()
    print('完成 System EIP 登入')

    # try:
    #     # alert = driver.switch_to.alert
    #     # if alert:
    #     #     alert.accept()
    #     #     print("alert accepted")
    #     # driver.get('https://bms.systex.com/bms2/service/app.login?userid=2200565&menuid=193&hash=df32e577e5f365f03baa4a5c53911d844bc33054')
    #     driver.refresh()
    #     time.sleep(5)
    #     arrive = driver.find_element(By.ID,
    #                                  'ctl00_ContentPlaceHolder1_RadDock6d688bcd6342410e9d935e715e08173e_C_widget_btnCHECKIN')
    #     arrive.click()
    # except NoSuchElementException as e:
    #     print(e)
    #     driver.refresh()
    #     time.sleep(7)
    #     arrive = driver.find_element(By.ID,
    #                                  'ctl00_ContentPlaceHolder1_RadDock6d688bcd6342410e9d935e715e08173e_C_widget_btnCHECKIN')
    #     arrive.click()
    # # driver.close()
    # except traceback:
    #     traceback.print_exception()
    time.sleep(3)
    driver.switch_to.frame('Frame1')
    arrive = driver.find_element(By.XPATH,
                                  '//*[@id="ctl00_ContentPlaceHolder1_RadDock6d688bcd6342410e9d935e715e08173e_C_widget_btnCHECKIN"]')
    arrive.click()
    print('即將跳轉打卡分頁')
    # driver.switch_to_default_content()

    time.sleep(4)

def system_punch():
    driver.switch_to.window(driver.window_handles[1])
    hour = Select(driver.find_element(By.ID, 'startHH'))

    mins = random.randint(30, 40)
    print(mins)

    hour.select_by_value('8')
    min_choice = Select(driver.find_element(By.ID, 'startMM'))
    min_choice.select_by_value(str(mins))
    # mins=60
    # if mins == 60:
    #     hour.select_by_value('9')
    #     min_choice.select_by_value('00')
    # else:
    #     min_choice.select_by_value(str(mins))

    location = Select(driver.find_element(By.ID, 'locationFirst'))
    # today = datetime.datetime.now().isoweekday()
    location.select_by_value('工作地點')
    location_sec = Select(driver.find_element(By.ID, 'locationSecond'))
    # if today == 5:
    location_sec.select_by_value('北區_鼎盛(松江)')
    # else:
    #     location_sec.select_by_value('北區_恆逸復北12、14、16F')

    temp = random.randint(0, 9)
    temp_today = driver.find_element(By.ID, 'temp')
    temp_today.send_keys(f'36.{temp}')

    # driver.find_element(By.ID,'button_save').click()

    time.sleep(3)
    print('已填寫 EIP 打卡資訊 ， 確認無誤請按完成！！')
    # driver.quit()
    # os.system('exit')


if __name__ == '__main__':
    eHour()
    system_login()
    system_punch()
