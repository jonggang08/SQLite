from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import sqlite3

#create connection
conn = sqlite3.connect('cputest.db')
c = conn.cursor()

#c.execute('''CREATE TABLE crypto(name TEXT, price INT, change TEXT, MarketCap TEXT)''')

url = "https://finance.yahoo.com/cryptocurrencies"

def extract(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table",{"class":"W(100%)"})
    coins = table.find_all("tr",{"class":"simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor)"})
    crypto=[]
    for coin in coins:
        name = coin.find("td",{"aria-label":"Name"}).text
        price = coin.find("td",{"aria-label":"Price (Intraday)"}).text
        change = coin.find("td",{"aria-label":"Change"}).text
        MarketCap = coin.find("td",{"aria-label":"Market Cap"}).text    
        c.execute('''INSERT INTO crypto VALUES(?,?,?,?)''',(name, price, change, MarketCap))
        dict = {"Name":name, "Price":price, "Change": change, "MarketCap":MarketCap}
        crypto.append(dict)
    return crypto

data = extract(url)

df = pd.DataFrame(data)
#df.to_csv("Crypto.csv")

conn.commit()
print('complete.')

#select all from table
c.execute('''SELECT * FROM crypto''')
results = c.fetchall()
print(results)

conn.close()