import requests
import datetime
import pubfunc

legal = pubfunc.legal_date_time()
if legal == 0:
    print("休市时间！")
    exit(0)
else:
    print(str(datetime.datetime.now()) + " 开始...")

config_file_dir = '/home/yanjc/sbin/stock/list.txt'
config_file = open(config_file_dir)

content = ''

while 1:
    line = config_file.readline()
    if not line:
        break
    list = line.split(",", 1)
    req_str = 'http://hq.sinajs.cn/list=' + list[0]
    r = requests.get(req_str)
    res = r.text
    result = res.split('=')[1]                            # 截取等号之后的数据部分
    
    name = result.split(',')[0].replace('"', '')          # 股票名称
    start_price = float(result.split(',')[1])             # 今日开盘价
    yesterday_price = float(result.split(',')[2])         # 昨日收盘价
    now_price = float(result.split(',')[3])               # 当前价格
    rate = (now_price-yesterday_price)/start_price * 100      # 涨跌幅度
    
    content = content + "{0}  {1:.2f}  {2:.2f}  {3:.2f}%".format(name, start_price, now_price, rate) + '\n'

config_file.close()

content = content.strip('\n')

json_data = {
    "msgtype": "text",
    "text": {
        "content": content,  # 发送内容
    }
}

wechat_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62dfeb6d-59bc-4819-a773-f72a7347a30a'
requests.post(url=wechat_url, json=json_data)

print(str(datetime.datetime.now()) + " 结束...")
