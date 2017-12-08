import tushare as ts


print(type(ts.get_stock_basics()))
# print(ts.get_stock_basics())
stock_basics = ts.get_stock_basics()
# print(type(stock_basics[stock_basics.name == '贵州茅台']))
print(stock_basics[stock_basics.name == '贵州茅台'].index.tolist())
print(type(stock_basics[stock_basics.name == '贵州茅台'].name))
# print(stock_basics[stock_basics.name == '贵州茅台'].iloc[0,21])
# print(stock_basics[stock_basics.name == '贵州茅台'].columns.size)

# i=0
# while i<22 :
#     print(i)
#     print(stock_basics[stock_basics.name == '贵州茅台'].iloc[0,i])
#     i = i+1



# for isHasGuiZhouMaoTai in ts.get_stock_basics()['name'].isin(['贵州茅台']):
    # if isHasGuiZhouMaoTai != False:
    #     print('有贵州茅台')

# for item in ts.get_stock_basics():
#     print(item)
    # isHasGuiZhouMaoTai = item['name'].isin(['贵州茅台'])
    # if isHasGuiZhouMaoTai != False:
    #     print(item)



