import os
import sys

def sprzedaj():
    print('sprzedane')


def kup():
    print('kupione')


kapital = 200.0
waluta = 0.0
przelicznikK = []
przelicznikS = []

priceSell=0
priceBuy=0

cenaKupna = 0
cenaSprzedazy=0

#if (cenaSprzedazy>=(cenaKupna+0.02) or cenaSprzedazy<=(cenaKupna-0.04)):
#    sprzedaj()

import requests

def get_pln_btc_prices():
  # Set the currency pair and base URL for the Binance API
  symbol = "BTCPLN"
  base_url = "https://api.binance.com"

  # Make a GET request to the Binance API to get the current order book
  endpoint = f"/api/v3/depth?symbol={symbol}&limit=1"
  response = requests.get(base_url + endpoint)

  if response.status_code == 200:
    # Parse the response data
    data = response.json()
    buy_price = float(data['bids'][0][0])
    sell_price = float(data['asks'][0][0])
    return (buy_price, sell_price)
  else:
    return None




prices = get_pln_btc_prices()
priceBuy = prices[0]
priceSell = prices[1]
print(priceSell, priceBuy)

def BuyCurr():
    global waluta, cenaKupna, priceBuy, przelicznikK
    prices = get_pln_btc_prices()
    priceBuy = prices[0]
    waluta = float(kapital) / float(priceBuy)
    cenaKupna = priceBuy
    przelicznikK.append(priceBuy)

def SellCurr():
    global kapital, cenaSprzedazy, priceBuy, przelicznikS
    prices = get_pln_btc_prices()
    priceSell = prices[1]
    kapital = float(waluta) * float(priceSell)
    cenaSprzedazy = priceSell
    przelicznikS.append(priceSell)

while True:
    prices = get_pln_btc_prices()
    priceBuy = prices[0]
    priceSell = prices[1]
    BuyCurr()
    print("Otwarcie kupiono! akutalny kapital: "+str(kapital)+" Aktualna waluta: "+str(waluta))
    print("Twój wolumen: "+str(waluta)+"    Cena kupna:"+str(priceBuy)+"    Cena sprzedaży:"+str(priceSell))

    if (priceSell >= (cenaKupna+0.03)):
        SellCurr()
        print("Sprzedano! akutalny kapital: "+str(kapital)+" Aktualna waluta: "+str(waluta))
        BuyCurr()
    elif(priceSell <= (cenaKupna-0.05)):
        BuyCurr()
        print("Sprzedano! akutalny kapital: "+str(kapital)+" Aktualna waluta: "+str(waluta))
        SellCurr()
        
