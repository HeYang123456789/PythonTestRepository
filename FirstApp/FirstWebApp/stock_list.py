import pymongo
# from mongoengine import *
from bs4 import BeautifulSoup
import requests
from FirstWebApp.string_tool import *

# 这个会有__main__.不识别的问题，默认'.'被识别的的是'__main__'
# from .string_tool import *

# 处理东方财富的股票list清单
# http://quote.eastmoney.com/stock_list.html
# 数据库的名称：eastmoney_data_tab
# 其中这里要处理的是股票list清单，表单名称： eastmoney_stock_list


# 获取本地端口，激活mongo客户端
client = pymongo.MongoClient('localhost',27017)
# 创建一个数据库
eastmoney_data_tab = client['eastmoney_data_tab']
# 创建一个表单
eastmoney_stock_list = eastmoney_data_tab['eastmoney_stock_list']
# 获取股票list清单的原始网页地址
start_getstocklist_url = 'http://quote.eastmoney.com/stock_list.html'

# 下面打印出来的类型：<class 'pymongo.collection.Collection'>
# print(type(eastmoney_stock_list))

def get_sotocklist(url):
    web_response = requests.get(url)
    # print(type(web_response)) # <class 'requests.models.Response'>
    wb_data = web_response.text.encode(web_response.encoding).decode('gbk')
    soup = BeautifulSoup(wb_data, 'lxml')
    # print(soup)
    # div.quotesearch > ul > li
    # #quotesearch > ul > li
    links = soup.select('#quotesearch > ul > li > a')

    for link in links:
        # print("%s:%s"%(link.get_text(),link.get('href')))
        # 老板电器(002508):http://quote.eastmoney.com/sz002508.html
        stock_code = getStockCode(link.get_text())
        stock_name = getStockName(link.get_text())
        data = {
            'stock_code':stock_code,
            'stock_name':stock_name,
            'stock_eastmoney_url':link.get('href')
        }
        # print(data)
        eastmoney_stock_list.insert_one(data)
    print('一共添加了几条数据：%d。添加完毕'%(eastmoney_stock_list.count()))
    # print(eastmoney_data_tab.last_status())

# 清空数据库的这个表
eastmoney_stock_list.drop()

# 执行获取股票清单
get_sotocklist(start_getstocklist_url)



