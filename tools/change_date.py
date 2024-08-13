from persiantools.jdatetime import JalaliDateTime


def change_date_to_miladi(news_date: str):
    time_news = news_date.split()[0]
    time_news_hour, time_news_min = map(int, time_news.split(':'))
    date_news = news_date.split()[2]
    date_news_year, date_news_month, date_news_day = map(int, date_news.split('/'))
    new_date = JalaliDateTime(date_news_year, date_news_month, date_news_day, time_news_hour, time_news_min).to_gregorian()
    return new_date
