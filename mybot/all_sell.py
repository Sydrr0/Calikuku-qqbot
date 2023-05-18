import requests,time,datetime,os
from lxml import etree


def all_sell_data():
        #保存本地html文件
    save_path = "./cache"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    else:
        pass
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time+now_time
    url_csgo = "https://www.csgoob.com/"
    response = requests.get(url = url_csgo)
    page_url = response.text
    with open("./cache/csgoob_homepage.html","w",encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/csgoob_homepage.html","r",encoding="utf-8")
    #选取有效数据,定期更改！！！
    tree = etree.parse('./cache/csgoob_homepage.html')
    #价格变化
    all_price ='￥'+ tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[2]/text()')[1]
    price_changing_symbol = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[3]/text()')[0]
    try:
        float(tree.xpath('/html/body/div/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[3]/text()')[1]) 
        price_changing_num = tree.xpath('/html/body/div/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[3]/text()')[1] + '%'
    except:
        price_changing_num = tree.xpath('/html/body/div/div[4]/div/div[1]/div/div[1]/div[4]/div[1]/div[3]/text()')[1]
    price_changing = str(price_changing_symbol + price_changing_num)
    
    #数量变化
    all_count = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[2]/div[2]/text()')[0] + ' 件'
    count_changing_symbol = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[2]/div[3]/text()')[0]
    try:
        float(tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[2]/div[3]/text()')[1])
        count_changing_num = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[2]/div[3]/text()')[1] + '%'
    except:
        count_changing_num = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[4]/div[2]/div[3]/text()')[1]
    count_changing = str(count_changing_symbol + count_changing_num)
    
    result = ('%s\n总底价: %s\n底价变化: %s\n总数量: %s\n数量变化: %s'%(nowa_time,all_price,price_changing
                                ,all_count,count_changing))
    return (result)