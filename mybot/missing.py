import time
lista = ['一','二','三','四','五','六','七','八','九']
now_time = time.localtime()
day_num = int(now_time[7]) - 68
if day_num<=99:
    num_ge = day_num%10
    num_shi = day_num//10
    hanzi_ge = lista[num_ge-1]
    hanzi_shi = lista[num_shi-1] + '十'
    result = hanzi_shi + hanzi_ge
else:
    num_ge = day_num%10
    num_shi = (day_num-100)//10
    num_bai = day_num//100
    hanzi_ge = lista[num_ge-1]
    hanzi_shi = lista[num_shi-1] + '十'
    hanzi_bai = lista[num_bai-1] + '百'
    result = hanzi_bai + hanzi_shi + hanzi_ge