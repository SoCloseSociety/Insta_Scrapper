from builtins import print

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
import time
import argparse
from selenium.webdriver.common.proxy import Proxy, ProxyType
from numpy import random
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import pyautogui
from selenium.webdriver.support.ui import Select
import pyshorteners
from datetime import datetime
import os
import urllib.request
import requests
from termcolor import colored
from colorama import init
import threading
from random import randint
import json
import random


class Instagram():
    def __init__(self):
        print("rgrgr")
        self.aa = input("enter how many users you need in one iteration  :      ")
        list_user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0']
        ua = UserAgent()
        #userAgent = ua.random
        userAgent = random.choice(list_user_agents)
        print(userAgent)

        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        options = Options()
        options.add_argument("--lang=en")
        print(os. getcwd()+"\\temp\\profile")
        #options.user_data_dir = "/media/buddhi/New Volume/fiver/soclose/curent/InstaScrapper/temp/profile"  #os. getcwd()+"\\temp\\profile"
        #options.add_argument('--user-data-dir="/media/buddhi/New Volume/fiver/soclose/curent/InstaScrapper/temp/profile"')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument(f'user-agent={userAgent}')

        options.add_argument("--lang=fr")
        options.add_argument("--lang=fr-ca")
        options.add_argument("--lang=aus")




        self.driver = webdriver.Chrome(options=options,executable_path="chromedriver")# executable_path=os.getcwd()+"chromedriver"

        #driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        time.sleep(1)
        

    def script(self):
        self.driver.get("https://www.instagram.com/")
        start = input("press Y if you need to sart scrapping hit enter")
        crawlc = (int(self.aa)/6)
        for xx in range(int(crawlc+10)):
            randompause = random.randint(1,4)
            if randompause == 3:
                waittym = random.randint(15,60)
                print("while crawling it takes the rest dut to bot detection wait time  : "+str(waittym))
                time.sleep(waittym)
            else:
                print(str(randompause)+"  still scrowling")

            try:
                self. driver.execute_script('''var fDialog = document.querySelector('div[role="dialog"] .isgrP');fDialog.scrollTop = fDialog.scrollHeight''')
            except Exception :
                print("crowling issue")
            print("reaching up to that limit")
            time.sleep(random.randint(0,2))
        print("crawling finished")


        for x in range(int(self.aa)):

            try:
                uname = self.driver.find_element_by_xpath('(//div[@role="dialog"]/descendant::div/ul/div/li/div/div/div[2]/div/span/a)['+str(x)+']').text
                #time.sleep(random.randint(0,3))
                print("click on follow button    :   "+ str(x))
                print(uname)
                with open('users.txt', 'a+') as f:
                    f.write(uname)
                    f.write('\n')
                f.close()
            except Exception:
                self. driver.execute_script('''var fDialog = document.querySelector('div[role="dialog"] .isgrP');fDialog.scrollTop = fDialog.scrollHeight''')
                time.sleep(random.randint(0,2))
                continue
                print("exeption")




aaa = Instagram()

aaa.script()