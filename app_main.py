import eel
from class_crypto import CryptoAPI


@eel.expose
def get_currency():
    tickers = crypto_api.get_tickers()
    return tickers

@eel.expose
def get_avg_price(ticker, amount, date):
    price_by_date = crypto_api.get_price_by_date(ticker, date)
    avg_price = round(price_by_date * float(amount), 3)
    return avg_price

@eel.expose
def submit_order(ticker, amount, date, total):
    global all_orders
    id = crypto_api.order_id_assignment()
    dic = {"id": id, "ticker": ticker, "amount": amount, "data": date, "total": total}
    all_orders.append(dic)
    return id


crypto_api = CryptoAPI()
eel.init('web')
eel.start('login.html', size=(1200, 600), port=0)



