from bs4 import BeautifulSoup
import requests

# 原始最开始主页的网页地址
start_url = 'http://data.eastmoney.com'

def get_channel_urls(url):
    wb = requests.get(url)
    # print(wb_data_o.encoding)
    wb_data = wb.text.encode(wb.encoding).decode('gbk')
    soup = BeautifulSoup(wb_data,'lxml')
    links = soup.select('div.vnav > div.navbody > ul > li > ul > li > a')
    for link in links:
        print("%s:%s"%(link.get_text(),link.get('href')))

get_channel_urls(start_url)

'''
大盘资金流:http://data.eastmoney.com/zjlx/dpzjlx.html
个股资金流:http://data.eastmoney.com/zjlx/detail.html
主力排名:http://data.eastmoney.com/zjlx/list.html
板块资金:http://data.eastmoney.com/bkzj/
行业资金流:http://data.eastmoney.com/bkzj/hy.html
概念资金流:http://data.eastmoney.com/bkzj/gn.html
地域资金流:http://data.eastmoney.com/bkzj/dy.html
资金流监测:http://data.eastmoney.com/bkzj/jlr.html
沪深港通资金流:http://data.eastmoney.com/hsgt/index.html
沪深港通成交榜:http://data.eastmoney.com/hsgt/top10.html
沪深港通持股:http://data.eastmoney.com/hsgtcg/
龙虎榜单:http://data.eastmoney.com/stock/lhb.html
融资融券:http://data.eastmoney.com/rzrq/
转融通:http://data.eastmoney.com/zrt/
公司题材:http://data.eastmoney.com/gstc/
千股千评:http://data.eastmoney.com/stockcomment/
停复牌信息:http://data.eastmoney.com/tfpxx/
选股器:http://data.eastmoney.com/xuangu/
大宗交易:http://data.eastmoney.com/dzjy/default.html
分红送配:http://data.eastmoney.com/yjfp/
机构调研:http://data.eastmoney.com/jgdy/
股东分析:http://data.eastmoney.com/gdfx/
股东户数:http://data.eastmoney.com/gdhs/
股东增减持:http://data.eastmoney.com/executive/gdzjc.html
高管持股:http://data.eastmoney.com/executive/
股东大会:http://data.eastmoney.com/gddh/
财经日历:http://data.eastmoney.com/cjrl/default.html
股市日历:http://data.eastmoney.com/gsrl/default.html
分析师指数:http://data.eastmoney.com/invest/invest/default.html
限售解禁:http://data.eastmoney.com/dxf/default.html
AB股比价:http://quote.eastmoney.com/center/list.html#absh_0_4
AH股比价:http://quote.eastmoney.com/center/list.html#ah_1
交易结算资金:http://data.eastmoney.com/cjsj/bankTransfer.html
股票账户:http://data.eastmoney.com/cjsj/yzgptjnew.html
股票统计:http://data.eastmoney.com/cjsj/gpjytj.html
券商业绩月报:http://data.eastmoney.com/other/qsjy.html
新股申购:http://data.eastmoney.com/xg/xg/default.html
新股日历:http://data.eastmoney.com/xg/xg/calendar.html
新股上会:http://data.eastmoney.com/xg/gh/default.html
首发申报信息:http://data.eastmoney.com/xg/xg/sbqy.html
新股解析:http://data.eastmoney.com/xg/xg/chart/zql.html
增发:http://data.eastmoney.com/other/gkzf.html
配股:http://data.eastmoney.com/zrz/pg.html
可转债:http://data.eastmoney.com/kzz/default.html
个股研报:http://data.eastmoney.com/report/
行业研报:http://data.eastmoney.com/report/hyyb.html
盈利预测:http://data.eastmoney.com/report/ylyc.html
策略报告:http://data.eastmoney.com/report/clbg.html
券商晨会:http://data.eastmoney.com/report/qsch.html
宏观研究:http://data.eastmoney.com/report/hgyj.html
最新业绩报表:http://data.eastmoney.com/bbsj/
分红送配:http://data.eastmoney.com/yjfp/
2017三季报:http://data.eastmoney.com/bbsj/201709/yjbb.html
2017三季报快报:http://data.eastmoney.com/bbsj/201709/yjkb.html
2017三季报预告:http://data.eastmoney.com/bbsj/201709/yjyg.html
2017三季报预披露:http://data.eastmoney.com/bbsj/201709/yysj.html
2017中报:http://data.eastmoney.com/bbsj/201706/yjbb.html
2017中报快报:http://data.eastmoney.com/bbsj/201706/yjkb/13.html
2017中报预告:http://data.eastmoney.com/bbsj/201706/yjyg.html
2017中报预披露:http://data.eastmoney.com/bbsj/201706/yysj.html
2017一季报:http://data.eastmoney.com/bbsj/201703/yjbb.html
2016年报:http://data.eastmoney.com/bbsj/201612/yjbb.html
期货龙虎榜:http://data.eastmoney.com/futures/sh/data.html
期货库存:http://data.eastmoney.com/ifdata/kcsj.html
COMEX库存:http://data.eastmoney.com/pmetal/comex/by.html
CFTC持仓:http://data.eastmoney.com/pmetal/cftc/baiyin.html
ETF持仓:http://data.eastmoney.com/pmetal/etf/by.html
现货与股票:http://data.eastmoney.com/ifdata/xhgp.html
期货价差矩阵:http://data.eastmoney.com/ifdata/jcjz.html
可交割国债:http://data.eastmoney.com/tf/tf.html
期权龙虎榜单:http://data.eastmoney.com/other/qqlhb.html
期权价值分析:http://data.eastmoney.com/other/valueAnal.html
期权风险分析:http://data.eastmoney.com/other/riskanal.html
期权折溢价:http://data.eastmoney.com/other/premium.html
美国经济数据:http://data.eastmoney.com/cjsj/foreign_0_0.html
德国经济数据:http://data.eastmoney.com/cjsj/foreign_1_0.html
瑞士经济数据:http://data.eastmoney.com/cjsj/foreign_2_0.html
日本经济数据:http://data.eastmoney.com/cjsj/foreign_3_0.html
英国经济数据:http://data.eastmoney.com/cjsj/foreign_4_0.html
澳大利亚经济数据:http://data.eastmoney.com/cjsj/foreign_5_0.html
加拿大经济数据:http://data.eastmoney.com/cjsj/foreign_7_0.html
欧元区经济数据:http://data.eastmoney.com/cjsj/foreign_6_0.html
香港经济数据:http://data.eastmoney.com/cjsj/foreign_8_0.html
行业指数:http://data.eastmoney.com/cjsj/hyzs.html
全球主要国家利率:http://data.eastmoney.com/cjsj/globalRate.html
基金排行:http://fund.eastmoney.com/data/fundranking.html
净值估算:http://fund.eastmoney.com/fundguzhi.html
基金评级:http://fund.eastmoney.com/data/fundrating.html
封基折价:http://fund.eastmoney.com/fbsjj_dwjz.html
新发基金:http://fund.eastmoney.com/data/xinfund.html
基金定投:http://fund.eastmoney.com/dingtou/syph_yndt.html
基金导购:http://fund.eastmoney.com/data/funddaogou.html
基金分红:http://fund.eastmoney.com/data/fundfenhong.html
基金公司:http://fund.eastmoney.com/company/default.html
私募基金:http://simu.eastmoney.com/data/smranklist.aspx
保险产品库:http://data.eastmoney.com/money/insurance.html
'''