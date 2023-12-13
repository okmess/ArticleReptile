import json
import time

from chrome_driver import get_driver

browser = get_driver()


def spider(start_url):
    # 导出搜索的全部记录选项
    browser.get(start_url)
    try:
        browser.find_elements_by_class_name('article__index-terms')[0]
    except:
        return "null"

    container = browser.find_elements_by_class_name('article__index-terms')[0]
    try:
        container.find_elements_by_class_name('level-1')[0]
    except:
        return "null"
    list_item = container.find_elements_by_class_name('level-1')[0]
    text = list_item.text.replace('\n', '[]')
    return text


def acm_spider():
    content = []
    with open('ACM_journal_repeat.json', 'r') as file:
        content = file.read()
        content = json.loads(content)
        for data in content:
            keywords = spider(data['url'])
            data['keywords'] = keywords
            print(data)
            time.sleep(1)
    print(content)

    with open('ACM_journal_final_data1.json', 'w') as file:
        json.dump(content, file, indent=4)


if __name__ == "__main__":
    acm_spider()
    browser.quit()
