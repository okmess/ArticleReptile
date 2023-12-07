import urllib.request

url = 'https://dblp.uni-trier.de/db/journals/joc/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
}
if __name__ == "__main__":
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    print(content)
