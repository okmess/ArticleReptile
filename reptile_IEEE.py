import json
import os
import time

from chrome_driver import get_driver

browser = get_driver()


def spider(start_url):
    # 导出搜索的全部记录选项
    browser.get(start_url)
    browser.execute_script("window.location.href+='/keywords#keywords'")
    # 获取keyword的容器位置
    container = browser.find_elements_by_class_name('stats-keywords-container')
    # 获取keywords列表
    list_item = container[1].find_elements_by_class_name('doc-keywords-list-item')
    # 获取具体的keywords值列表
    text = list_item[0].text.lstrip('IEEE Keywords\n').replace('\n,\n', '[]')
    print(text)
    return text


def ieee_spider():
    content = []
    with open('IEEE_journal.json', 'r') as file:
        content = file.read()
        content = json.loads(content)
        for data in content:
            keywords = spider(data['url'])
            data['keywords'] = keywords
            print(data)
            time.sleep(3)
    with open('IEEE_journal1.json', 'w') as file:
        json.dump(content, file, indent=4)


if __name__ == "__main__":
    ieee_spider()
    browser.quit()
