
# 字符串处理工具

# 例如：将字符串'云南铜业(000878)'处理为返回'云南铜业'和'000878'
def getStockName(stockStr):
    stockStrArr = stockStr.split('(')
    # print('%s,%s'%(stockStrArr[0],stockStrArr[1]))
    return stockStrArr[0]

def getStockCode(stockStr):
    stockStrArr = stockStr.split('(')
    stockCodeStr = stockStrArr[1]
    stockCodeArr = stockCodeStr.split(')')
    return stockCodeArr[0]

# print(getStockCode('云南铜业(000878)'))

