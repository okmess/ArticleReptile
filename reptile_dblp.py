import time
import requests
import json
from dblp_url import ACM_url, IEEE_url, Springer_url, ACM_conference_url, IEEE_conference_url, Springer_conference_url, \
    IEEE_ACM_conference_url

from chrome_driver import get_driver


def spider(start_url):
    browser = get_driver()
    # 导出搜索的全部记录选项
    browser.get(start_url)
    container = browser.find_element_by_xpath('//div[@id="main"]/ul')
    url_list = container.find_elements_by_tag_name('a')
    articles = []
    for i in range(len(url_list)):
        year = ''
        if ': ' in url_list[i].text:
            year = url_list[i].text.split(': ')[1]
        elif ', ' in url_list[i].text:
            year = url_list[i].text.split(', ')[1]
        if '/' in year:
            year = year.split('/')[0]
        if int(year) > 2017:
            temp = spider2(year, url_list[i].get_attribute('href'))
            articles.extend(temp)
            if int(year) == 2018:
                break
    browser.quit()
    return articles


def spider2(year, url):
    browser1 = get_driver()
    browser1.get(url)
    try:
        browser1.find_element_by_xpath('//header[@id="headline"]/nav/ul/li[1]/div[@class="body"]/ul/li[2]/a')
    except:
        return
    json_url = browser1.find_element_by_xpath('//header[@id="headline"]/nav/ul/li[1]/div[@class="body"]/ul/li[2]/a')
    response = requests.get(json_url.get_attribute('href'))
    json_data = json.loads(response.text)
    total = int(json_data['result']['hits']['@total'])
    article_list = json_data['result']['hits']['hit']
    articles = []
    for i in range(total):
        if 'ee' in article_list[i]['info']:
            temp = {'title': article_list[i]['info']['title'], 'year': article_list[i]['info']['year'],
                    'url': article_list[i]['info']['ee']}
            articles.append(temp)
    browser1.quit()
    return articles


def journal(journal_type):
    url_list = []
    # 获取对应出版社所有的期刊dblp地址
    if journal_type == 'ACM':
        url_list = ACM_url
    elif journal_type == 'IEEE':
        url_list = IEEE_url
    elif journal_type == 'Springer':
        url_list = Springer_url
    articles = []
    # 遍历每个期刊，并访问每个期刊的地址获取对应所有论文的地址
    for i in range(len(url_list)):
        start_url = url_list[i]['url']
        journal_name = url_list[i]['journal']
        journal_shorter_form = url_list[i]['shorter_form']
        temp = spider(start_url)
        for j in range(len(temp)):
            temp[j]['journal_name'] = journal_name
            temp[j]['journal_shorter_form'] = journal_shorter_form
        articles.extend(temp)
    print(articles)
    return articles


if __name__ == "__main__":
    # with open('ACM_journal.json', 'w') as file1:
    #     json.dump(journal('ACM'), file1, indent=4)

    with open('IEEE_journal.json', 'w') as file2:
        json.dump(journal('IEEE'), file2, indent=4)

    # with open('Springer_journal.json', 'w') as file3:
    #     json.dump(journal('Springer'), file3, indent=4)
