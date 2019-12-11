import json
import boto3
import random

kinesis = boto3.client('kinesis')

def getOrderData(orderId, ticker):
    data = {}
    data['RecordType'] = "Order"
    data['Oid'] = orderId
    data['Oticker'] = ticker
    data['Oprice'] = random.randint(500, 10000)
    data['Otype'] = "Sell"
    return data

def getTradeData(orderId, tradeId, ticker, tradePrice):
    data = {}
    data['RecordType'] = "Trade"
    data['Tid'] = tradeId
    data['Toid'] = orderId
    data['Tticker'] = ticker
    data['Tprice'] = tradePrice
    return data

x = 1
while True:
    #rnd = random.random()
    rnd = random.randint(1,3)
    if rnd == 1:
        ticker = "AAAA"
    elif rnd == 2:
        ticker = "BBBB"
    else:
        ticker = "CCCC"
    data = json.dumps(getOrderData(x, ticker))
    kinesis.put_record(StreamName="OrdersAndTradesStream", Data=data, PartitionKey="partitionkey")
    print(data)
    tId = 1
    for y in range (0, random.randint(0,6)):
        tradeId = tId
        tradePrice = random.randint(0, 3000)
        data2 = json.dumps(getTradeData(x, tradeId, ticker, tradePrice));
        kinesis.put_record(StreamName="OrdersAndTradesStream", Data=data2, PartitionKey="partitionkey")
        print(data2)
        tId+=1
        
    x+=1