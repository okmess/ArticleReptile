import os
import time

from chrome_driver import get_driver

start_url = 'https://dl.acm.org/doi/10.1145/3581783.3613910#sec-terms'

browser = get_driver()


def spider():
    # 导出搜索的全部记录选项
    browser.get(start_url)
    container=browser.find_elements_by_class_name('article__index-terms')[0]
    list_item=container.find_elements_by_class_name('level-1')[0]
    print(list_item.text)

    time.sleep(120)


if __name__ == "__main__":
    try:
        spider()
    finally:
        time.sleep(3)
        browser.quit()
