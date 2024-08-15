import mysql.connector
# Connect to MySQL
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="R00t1234", database="snn_scrap")
def initialize_db():
    db = Database()
    if db.conn.is_connected():
        cursor = db.conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS news (
            id int primary key auto_increment ,
            news_url text,
            image_url varchar(255) ,
            title varchar(255),
            news_lead text,
            news_id int ,
            news_category varchar(128),
            published_date datetime
        )
        """
        cursor.execute(query)
        db.conn.close()
