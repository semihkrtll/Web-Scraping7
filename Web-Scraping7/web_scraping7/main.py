import requests
from bs4 import BeautifulSoup
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="",      
    database="crypto_db"  
)

cursor = db_connection.cursor()


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://finans.mynet.com/kripto-para/"
sayfa = requests.get(url, headers=headers)
icerik = BeautifulSoup(sayfa.content, "html.parser")

adi = icerik.find_all("div", {"class": "flex align-items-center kripto-first-td-m"})


for i in adi:
    crypto_name = i.text.strip()

   
    cursor.execute("INSERT INTO crypto_names (crypto_name) VALUES (%s)", (crypto_name,))


db_connection.commit()


cursor.close()
db_connection.close()
