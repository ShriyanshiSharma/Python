from tkinter import *
import requests
import json

pyth = Tk()
pyth.title("My Crypto")

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

def portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=11566edd-6537-4e3e-8c61-f2a7091d8037")
    api = json.loads(api_request.content)
   
    coins = [
    {
        "symbol": "BTC",
        "amount_owed":2,
        "price_per_coin":20000.0
    },
    {
        "symbol": "ETH",
        "amount_owed":100,
        "price_per_coin":1000.0
    },
    {
        "symbol": "USDT",
        "amount_owed":50,
        "price_per_coin":0.4
    },
     {
        "symbol": "BNB",
        "amount_owed":51,
        "price_per_coin":200.0
    },
     {
        "symbol": "ADA",
        "amount_owed":14,
        "price_per_coin":0.7
    },
     {
        "symbol": "XRP",
        "amount_owed":100,
        "price_per_coin":0.1
    },
     {
        "symbol": "DOGE",
        "amount_owed":45,
        "price_per_coin":0.09
    },
    ]
    
    total_pl = 0
    coin_row = 1
    total_current_value = 0
    
    for i in range(0,10):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owed"] * coin["price_per_coin"]
                current_val = coin["amount_owed"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owed"]

                total_pl += total_pl_coin
                total_current_value +=  current_val

                name = Label(pyth, text=api["data"][i]["symbol"], bg="white", fg="Black", font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                price = Label(pyth, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="Black", font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                no_coin = Label(pyth, text=coin["amount_owed"], bg="white", fg="black", font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                no_coin.grid(row=coin_row, column=2, sticky=N+S+E+W)

                amount_paid = Label(pyth, text="${0:.2f}".format(total_paid), bg="white", fg="Black", font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

                current_val = Label(pyth, text="${0:.2f}".format(current_val), bg="white", fg=font_color(float("{0:.2f}".format(total_paid))), font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

                pl_coin = Label(pyth, text="${0:.2f}".format(pl_percoin), bg="white", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

                totalpl = Label(pyth, text="${0:.2f}".format(total_pl_coin), bg="white", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

                coin_row += 1

    total_cv = Label(pyth,text="${0:.2f}".format(total_current_value), bg="white", fg="Black", font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
    total_cv.grid(row=coin_row, column=4,sticky=N+S+E+W)

    total_pl = Label(pyth,text="${0:.2f}".format(total_pl), bg="white",  fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
    total_pl.grid(row=coin_row, column=6,sticky=N+S+E+W)
    
    api = ""

    update = Button(pyth,text="Update" ,bg="#142E54",  fg="white",command=portfolio, font="Lato 12", padx="2", pady="2",borderwidth=2, relief="groove")
    update.grid(row=coin_row+1,column=6,sticky=N+S+E+W)



name = Label(pyth, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pyth, text="Price",  bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coin = Label(pyth, text="Coins Owned", bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
no_coin.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pyth, text="Total Amount Paid",  bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pyth, text="Current Value",  bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pyth, text="P/L Per Coin",  bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pyth, text="Total P/L with Coin",  bg="#142E54", fg="white",font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

portfolio()

pyth.mainloop()
