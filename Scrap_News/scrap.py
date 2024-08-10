import requests
from bs4 import BeautifulSoup
from Scrap_News.sub_scrap import scrap_news_page

BASE_URL = "https://snn.ir"
response = requests.get(BASE_URL)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    main_div = soup.find('div', class_='col-xs-36 col-sm-23 col-md-21 main_col')
    section_news = main_div.find('section', class_='akhbar_vizhe')
    list_news = section_news.find_all('article', class_='akhbar_list_item')
    for news in list_news:
        news_url = BASE_URL + news.find('a', class_='akhbar_list_image')['href']
        news_details = scrap_news_page(news_url)
        image_url = BASE_URL + (news.find('a', class_='akhbar_list_image')).find('img')['src']
        title = news.find('a', class_='akhbar_list_title').text
        published_date = news.find('a', class_='akhbar_list_title')['title']
        news_lead = news.find('div', class_='akhbar_list_lead').text
        news_id = news_details['id']
        news_service = news_details['service']
        # We need add Methode or Commands to save data into database instead of print Items
        print(news_url)
        print(image_url)
        print(title)
        print(published_date)
        print(news_lead)
else:
    raise Exception('We Couldn\'t Connect To Website')