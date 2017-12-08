import pymongo

# 获取本地端口，激活mongo客户端
client = pymongo.MongoClient('localhost',27017)

# 创建一个数据库
mydata = client['mydata']

# 创建一个表单
sheet_tab_one = mydata['sheet_tab_one']

# 处理一个本地的txt文档，然后把文本内容全部读取，然后文本数据结构化，并存储每行的文字数，也存出起来
# /Users/HeYang/Desktop/长江电力分析报告.txt

# path = '/Users/HeYang/Desktop/长江电力分析报告.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         if len(line.split())>0 :
#             data = {
#                 'index':index,
#                 'line':line,
#                 'words':len(line.split())
#             }
#             print(data)
#             sheet_tab_one.insert_one(data)

# 表插入数据的方法insert_one，会不清除原有的数据，重复添加进去

# 展示数据库中的数据
# $lt $lte $gt $gte $ne，
# 依次等价于< <= > >= !=
# l表示less，g表示greater e表示equal n表示not
for item in sheet_tab_one.find({'index':{'$lt':5}}):
    print(item)




