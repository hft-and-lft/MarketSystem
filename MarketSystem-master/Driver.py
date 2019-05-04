import Market
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from pandas.io import sql
import xlsxwriter
import datetime

def saveMes(market,prices):
    writer = pd.ExcelWriter("F:\南京大学(备份)\创新项目\MarketSystem\MarketRecords.xlsx", engine='xlsxwriter')
    #市场结构信息表：前两期基本面及市场价格；时间周期
    df1 = pd.DataFrame({'Time': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], 'LFT-Num': [market.LFTnum],
                        'HFT-Num': [market.HFTnum], 'Round': [time], 'Chart-Num': [market.Chartnum], 'Fund-Num': [market.Fundnum]})
    df1.to_excel(writer, sheet_name='MarketMessage')
    #交易者参数配置表：低频交易者数量；图表交易者数量；基本面交易者数量；高频交易者数量；低频交易者参数设置；高频交易者参数设置;财富
    # df21 = pd.DataFrame(market.LowLatencyFactor.T, columns=['LatencyFactor'])
    # df22 = pd.DataFrame(market.ChartEpsilon.T, columns=['ChartEps'])
    # df23 = pd.DataFrame(market.FundamentalEpsilon.T, columns=['FundEps'])
    # df24 = pd.DataFrame(market.PriceEps.T, columns=['PriceEps'])
    # df2 = pd.concat([df21, df22, df23, df24], axis=1)
    # df2.to_excel(writer, sheet_name="LowTradersMessage")
    # df31 = pd.DataFrame(market.threshold.T, columns=['Threshold'])
    # df32 = pd.DataFrame(market.priceDis.T, columns=['PriceDis'])
    # df3 = pd.concat([df31, df32], axis=1)
    # df3.to_excel(writer, sheet_name='HighTradersMessage')
    df4 = pd.DataFrame(columns=['Type', 'InitStock','Stock', 'InitCash','Cash', 'LatencyFactor', 'Eps', 'PriceEps'])
    for i in range(0,len(market.ChartTraders)):
        temp = market.ChartTraders['low' + str(i)]
        df4.loc[i] = [temp.traderType,temp.initstock,temp.stock,temp.initcash,temp.cash,temp.latencyFactor,temp.epsilon,temp.priceEps]
    for i in range(market.Chartnum,market.LFTnum):
        temp = market.FundTraders['low' + str(i)]
        df4.loc[i] = [temp.traderType,temp.initstock,temp.stock,temp.initcash,temp.cash,temp.latencyFactor,temp.epsilon,temp.priceEps]
    df4.to_excel(writer,sheet_name='LowAgent')
    df5 = pd.DataFrame(columns = ['InitStock','stock','InitCash', 'cash','threshold', 'priceDis'])
    for i in range(0,market.HFTnum):
        temp = market.HTraders['high' + str(i)]
        df5.loc[i] = [temp.initstock,temp.stock,temp.initcash,temp.cash,temp.threshold,temp.priceDis]
    df5.to_excel(writer,sheet_name='HighAgent')
    #成交订单表：每轮成交的订单详情表
    market.deals.to_excel(writer,sheet_name='Deals')
    #价格表：价格
    pd.DataFrame(prices).to_excel(writer,sheet_name='Price')
    writer.save()
    return

if __name__ == '__main__':

# Part 1: Initialization
    # ToDo : input the parameter
    RecordList = {-2:[100,102,[]],-1:[101,102,[]]}
    time = 10
    #Hflag = input("本次实验是否加入高频参与者？（加入输入True, 否则输入False）")
    market = Market.Market(RecordList,100,5,{},{},{})   #initialize market :RecordList,LFTnum,HFTnum,Chart,Fund,HFT
    market.initTraders(market.ChartTraders,market.FundTraders,market.HTraders,time)  #initialize traders
    prices = []
# Part 1.1: Create the Database
    #database = sqlite3.connect('Market.db')
#     database.execute('''CREATE TABLE AskList
#     (PRICE REAL NOT NULL,
#     TIME REAL NOT NULL,
#     AGENTYPE CHAR(10) NOT NULL,
#     AGENTID CHAR(50) NOT NULL,
#     QUANTITY REAL NOT NULL);''')
#     database.execute('''CREATE TABLE BidList
#     (PRICE REAL NOT NULL,
#     TIME REAL NOT NULL,
#     AGENTYPE CHAR(10) NOT NULL,
#     AGENTID CHAR(50) NOT NULL,
#     QUANTITY REAL NOT NULL);''')
#     database.execute('''CREATE TABLE Deals
#     (TIME TEXT NULL,
#     ASKTYEP CHAR(50) NOT NULL,
#     BIDTPE CHAR(50) NOT NULL,
#     PRICE REAL NOT NULL,
#     QUANTITY REAL NOT NULL);''')
# Part 2: Rounds of trade
    for t in range(0,time):
        # gen orders,现在加入高频还要靠手动调整代码
        market.preOrders()
        # gen market price
        market.genMarketQuotes()
        #market.AskList.to_sql('AskList',con=database,if_exists='append',index=False)
        #market.BidList.to_sql('BidList', con=database, if_exists='append', index=False)
        # temp_round = 'Round' + str(market.time)
        # market.AskList.to_excel(writer,sheet_name = temp_round )
        # market.BidList.to_excel(writer,sheet_name = temp_round,startcol = 8)
        deals = market.genMarketDeals()
        #market.deals.append(deals)
        prices.append(market.genMarketPrice(deals))
        # TODO:装换成Dataframe还有问题
        # new_deals = []
        # for deal in deals:
        #     new_deals.append([deal.sellerName,deal.buyerName,deal.quantity,deal.price,deal.time])
        # new_deals = pd.DataFrame(new_deals, columns=["AskId", "BidId", "Quantity", "Price","Time"])
        # new_deals.to_sql('Deals',con=database,if_exists='append',index=False)
        market.time = t + 1
        print(market.time)
    #print(market.RecordList)
    print("Chartnum is ",market.Chartnum)
    plt.plot(range(0,time),prices)
    plt.xlabel('Time')
    plt.ylabel('Market Price')
    plt.show()
    # market.writer.close()
#Part 2 : 参数信息写入文件
    saveMes(market,prices)


#==============================================================================
#     for t in range(0,1200):
#
#     print(LowLatencyFactor[0][1])                           #调用方法
#     ChartEpsilon = np.random.normal(0,0.05,[1,10000])
#     FundamentalEpsilon = np.random.normal(0,0.01,[1,10000]) #生成相关的随机数
#==============================================================================
