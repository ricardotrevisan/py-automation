import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time


load_dotenv()
PROXY = os.environ.get('PROXY');
print(PROXY)

userAgentsList =["Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
                 "Roku4640X/DVP-7.70 (297.70E04154A)",
                 "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"]

opt = Options()
opt.add_argument("user-agent=" + userAgentsList[0])

#---
answer = input("Connect using a Proxy? y|N")
if answer == "y" or answer == "Y":
    opt.add_argument("--proxy-server=http://%s" % PROXY)
#---

url = "https://www.ferendum.com/pt/PID528439PSD27285573" #testing purposes only
browser = webdriver.Chrome(executable_path="../resources/chromedriver.exe", options=opt)
browser.get(url)

nameFld = browser.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div[3]/div/div/form/div/table/tbody[1]/tr[1]/td[3]/input')
nameFld.click()
time.sleep(2) #unnecessary
nameFld.send_keys(('Donnar'))

option = browser.find_element_by_xpath('/html/body/spamtrap/main/div[3]/div[3]/div/div/form/div/table/tbody[1]/tr[3]/td[3]/input')
time.sleep(2) #unnecessary
option.click()

buttom = browser.find_element_by_xpath(('/html/body/spamtrap/main/div[3]/div[3]/div/div/form/div/table/tbody[2]/tr[1]/td[3]/input'))
buttom.click()
