from binance import Client
from binance.enums import *
from time import sleep

def GetFloat(string):
    while True:
        try:
            quantity = float(input(string))
            return quantity
        except Exception as e:
            print(e)
        
def GetInt(string):
    while True:
        try:
            typeOrder = int(input(string))
            if typeOrder == 1 or typeOrder == 2:
                return typeOrder
        except Exception as e:
            print(e)
    
apiKey = input("Enter API Key: ")
privateKey = input("Enter Private Key: ")
symbol = input("Enter Symbol (EX: BTCUSDT): ").upper()
quantity = GetFloat("Enter quantity: ")
typeOrder = GetInt("Enter Type Order (1 for MARKER, 2 for LIMIT): ")
if typeOrder == 2:
    priceLimit = GetFloat("Enter Price Limit: ")

client = Client(apiKey, privateKey, testnet=False)

while True:
    try:
        if typeOrder == 1:
            result = client.create_order(
                symbol=symbol,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
        else:
            result = client.create_order(
                symbol=symbol,
                side=SIDE_BUY,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=priceLimit,
                timeInForce=TIME_IN_FORCE_GTC
            )
        print("Order created: ", str(result))
        break
    except Exception as e:
        print(e.message)
    sleep(0.5)