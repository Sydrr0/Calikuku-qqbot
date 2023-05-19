from bs4 import BeautifulSoup
import requests, time, datetime


# a1印花集
def get_data_a1yhj():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time + now_time
    response = requests.get(url='https://buff.163.com/goods/835780#tab=selling')
    page_url = response.text
    with open("./cache/price_buff_hjw.html", "w", encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/price_buff_hjw.html", "r", encoding="utf-8")
    data_getten = BeautifulSoup(op, "lxml")
    mini_price = data_getten.find_all("span", class_="custom-currency")

    # 输出名称
    first_title = (str(data_getten.find("title").get_text))[45:-26]
    # 获取并输出价格
    now_price = mini_price[1].get("data-price")
    last = ('%s\n----------------------------\n%s: ¥%s'
            % (nowa_time, first_title, now_price))
    return last


# 黄金网
def get_data_hjw():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time + now_time
    response = requests.get(url='https://buff.163.com/goods/774695?from=market#tab=selling')
    page_url = response.text
    with open("./cache/price_buff_hjw.html", "w", encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/price_buff_hjw.html", "r", encoding="utf-8")
    data_getten = BeautifulSoup(op, "lxml")
    mini_price = data_getten.find_all("span", class_="custom-currency")

    # 输出名称
    first_title = (str(data_getten.find("title").get_text))[45:-26]
    # 获取并输出价格
    now_price = mini_price[2].get("data-price")
    last = ('%s\n----------------------------\n%s: ¥%s'
            % (nowa_time, first_title, now_price))
    return last


# 石林
def get_data_sl():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time + now_time
    response = requests.get(url='https://buff.163.com/goods/835615?from=market#tab=selling')
    page_url = response.text
    with open("./cache/price_buff_sl.html", "w", encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/price_buff_sl.html", "r", encoding="utf-8")
    data_getten = BeautifulSoup(op, "lxml")
    mini_price = data_getten.find_all("span", class_="custom-currency")

    # 输出名称
    first_title = (str(data_getten.find("title").get_text))[45:-26]
    # 获取并输出价格
    now_price = mini_price[2].get("data-price")
    last = ('%s\n----------------------------\n%s: ¥%s'
            % (nowa_time, first_title, now_price))
    return last


# usp印花集
def get_data_uspyhj():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time + now_time
    response = requests.get(url='https://buff.163.com/goods/900565#tab=selling')
    page_url = response.text
    with open("./cache/price_buff_sl.html", "w", encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/price_buff_sl.html", "r", encoding="utf-8")
    data_getten = BeautifulSoup(op, "lxml")
    mini_price = data_getten.find_all("span", class_="custom-currency")
    # 输出名称
    first_title = (str(data_getten.find("title").get_text))[45:-26]
    # 获取并输出价格
    now_price = mini_price[1].get("data-price")
    last = ('%s\n----------------------------\n%s: ¥%s'
            % (nowa_time, first_title, now_price))
    return last


def get_data_zhanhen():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    now_time = str(localtime[10:19])
    today_time = str(datetime.date.today())
    nowa_time = today_time + now_time
    response = requests.get(url='https://buff.163.com/goods/835504?from=market#tab=selling')
    page_url = response.text
    with open("./cache/price_buff_hjw.html", "w", encoding="utf-8") as op:
        op.write(page_url)
        op = open("./cache/price_buff_hjw.html", "r", encoding="utf-8")
    data_getten = BeautifulSoup(op, "lxml")
    mini_price = data_getten.find_all("span", class_="custom-currency")

    # 输出名称
    first_title = (str(data_getten.find("title").get_text))[45:-26]

    # 获取并输出价格
    now_price = mini_price[2].get("data-price")
    last = ('%s\n----------------------------\n%s: ¥%s'
            % (nowa_time, first_title, now_price))
    return last
