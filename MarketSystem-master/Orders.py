# 历史记录
class Records:
    time = 0
    fundamentalPrice = 0
    marketPrice = 0
    deals = []
    totalVolume = 0
    finalPrice = 0
    averagePrice = 0


# ==============================================================================
#     def __init__(self):
#         if Time==0:
#             self.fundamentalPrice=fundamentalPrice
#             self.marketPrice=marketPrice
#         else:
#             self.fundamentalPrice
#
#     def computeTotalVolume(self):
#         self.totalVolume=0
#         for i in self.deals:
#             self.totalVolume+=self.volume
#         return self.totalVolume
#
#     def computeFinalPrice(self):
#         self.finalPrice=0
#         self.finalPrice=self.deals[-1].price
#
#     def computeAveragePrice(self):
#         totalPrice=0
#         for i in range(len(self.deals)):
#             totalPrice+=self.deals[i].price
#         self.averagePrice=totalPrice/len(self.deals)
#
#     def addDeal(self,deal):
#         self.deals.append(deal)
# ==============================================================================

# 订单
class Order:
    price = 100
    traderType = ''
    traderId = 0
    direction = 0  # 0-ask 1-bid
    quantity = 18
    # 高频与低频交易者的留存时间设定，市场每清算一次区间减一，高频的值较小
    suspendTime = 0
    time = 0

    def __init__(self, traderId, direction, price, quantity):
        self.traderId = traderId
        self.quantity = quantity
        self.direction = direction
        self.price = price


class Deal:
    dealId = 0
    sellerName = ''
    buyerNameme = ''
    quantity = ''
    price = 0
    time = 0

    def __init__(self, sellerName, buyerName, quantity, price,time):
        self.sellerName = sellerName
        self.buyerName = buyerName
        self.quantity = quantity
        self.price = price
        self.time = time