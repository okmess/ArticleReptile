import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

# 浏览器驱动
path = 'chromedriver.exe'


def get_driver():
    # 隐藏浏览器界面
    chrome_option = Options()
    # chrome_option.add_argument('--headless')
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_experimental_option('prefs', {'profile.default_content_settings.popups': 0,
                                                    'download.default_directory': os.getcwd()})
    # # # 防止检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_option, options=option)
    return browser
