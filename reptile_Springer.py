import os
import time

from chrome_driver import get_driver

start_url = 'https://link.springer.com/article/10.1007/s00778-022-00737-1#article-info'

browser = get_driver()


def spider():
    # 导出搜索的全部记录选项
    browser.get(start_url)
    container = browser.find_element_by_id('article-info-content')
    sub_container = container.find_elements_by_class_name('c-bibliographic-information')[0]
    list_item = sub_container.find_elements_by_tag_name('div')[1]
    ul = list_item.find_elements_by_class_name('c-article-subject-list')[0]
    print(ul.text)

    time.sleep(120)


if __name__ == "__main__":
    try:
        spider()
    finally:
        time.sleep(3)
        browser.quit()
