import os
import time

from chrome_driver import get_driver

start_url = 'https://ieeexplore.ieee.org/document/9425000/keywords#keywords'

browser = get_driver()


def spider():
    # 导出搜索的全部记录选项
    browser.get(start_url)
    # 获取keyword的容器位置
    container = browser.find_elements_by_class_name('stats-keywords-container')
    # 获取keywords列表
    list_item = container[1].find_elements_by_class_name('doc-keywords-list-item')
    # 获取具体的keywords值列表
    li_list = list_item[0].find_elements_by_tag_name('li')
    for i in range(len(li_list)):
        print(li_list[i].text.split("\n,")[0])
    time.sleep(120)


if __name__ == "__main__":
    try:
        spider()
    finally:
        time.sleep(3)
        browser.quit()
