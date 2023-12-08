import json
import os
import time

from chrome_driver import get_driver
import multiprocessing




def spider(start_url,browser):
    # 导出搜索的全部记录选项
    browser.get(start_url)
    browser.execute_script("window.location.href+='/keywords#keywords'")
    try:
        browser.find_elements_by_class_name('stats-keywords-container')
    except:
        return "null"
    # 获取keyword的容器位置
    container = browser.find_elements_by_class_name('stats-keywords-container')

    try:
        container[1].find_elements_by_class_name('doc-keywords-list-item')
    except:
        return "null"
    # 获取keywords列表
    list_item = container[1].find_elements_by_class_name('doc-keywords-list-item')

    try:
        list_item[0].text.lstrip('IEEE Keywords\n').replace('\n,\n', '[]')
    except:
        return "null"
    # 获取具体的keywords值列表
    text = list_item[0].text.lstrip('IEEE Keywords\n').replace('\n,\n', '[]')
    return text


def ieee_spider(index):
    browser = get_driver()
    content = []
    print(index)
    try:
        with open(f'documents/batch_{index}.json', 'r') as file:
            content = file.read()
            content = json.loads(content)
            for data in content:
                keywords = spider(data['url'], browser)
                data['keywords'] = keywords
                print(data)
                time.sleep(1)
        with open(f'IEEEData/IEEE_journal{index}.json', 'w') as file:
            json.dump(content, file, indent=4)
    except:
        with open('error.txt', 'w') as file:
            file.write(str(index + 1))
    finally:
        browser.quit()


if __name__ == "__main__":
    processes = []
    for index in range(40, 43):
        p = multiprocessing.Process(target=ieee_spider,args=(index,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()

