import requests
import logging
from fastapi import HTTPException, status
from bs4 import BeautifulSoup
from Scrap_News.sub_scrap import scrap_news_page
from tools.change_date import change_date_to_miladi
from crud_news import is_news_exist, save_news

BASE_URL = "https://snn.ir"
def scrap_news():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            main_div = soup.find('div', class_='col-xs-36 col-sm-23 col-md-21 main_col')
            section_news = main_div.find('section', class_='akhbar_vizhe')
            list_news = section_news.find_all('article', class_='akhbar_list_item')
            for news in list_news:
                news_url = BASE_URL + news.find('a', class_='akhbar_list_image')['href']
                news_details = scrap_news_page(news_url)
                image_url = BASE_URL + (news.find('a', class_='akhbar_list_image')).find('img')['src']
                title = news.find('a', class_='akhbar_list_title').text
                news_lead = news.find('div', class_='akhbar_list_lead').text
                news_id = news_details['id']
                news_category = news_details['category']
                published_date = change_date_to_miladi(news.find('a', class_='akhbar_list_title')['title'])
                # Check this news is existing in databases or not
                counter = 0
                if not is_news_exist(news_id):
                    news_jadid = {'news_url': news_url, 'image_url': image_url, 'title': title, 'news_lead': news_lead,
                                  'news_id': news_id, 'news_category': news_category, 'published_date': published_date}
                    save_news(news_jadid)
                    counter += 1
                return counter
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        logging.error("We Couldn't Connect To Website")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="We Couldn't Connect To Website")