import requests
from bs4 import BeautifulSoup

def scrap_news_page(url):
    sub_detail = dict()
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        news_content = soup.find('div', class_="col-xs-36 col-sm-23 col-md-21 main_col")
        news_service = news_content.find('a', class_='service_name').text
        news_id = int(((news_content.find('div', class_="news_nav news_id_c hidden-xs hidden-ms visible-sm visible-md visible-lg")).contents[2].split())[0])
        sub_detail['service'] = news_service
        sub_detail['id'] = news_id
        return sub_detail
    else:
        raise Exception('We Couldn\'t Connect To Website')