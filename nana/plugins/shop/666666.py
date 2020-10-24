from conf import settings
import os
import random

account_total_coins = 99999999
account = 'Yuuki'
total = []
#111111
with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f1, \
open(settings.SHOPPING_CARS_TMP, mode='w', encoding='utf-8') as f2,  \
open(settings.MAIDAODE_LIST_TMP, mode='a', encoding='utf-8') as f3:    
    for line in f1:
        user, commodity, price, nums = line.strip().split('|')
        print(user)
        if user == 'Yuuki':
            f3.write(f"{user}|{commodity}|{price}|{nums}\n")
            total.append(int(price) * int(nums))
        else:
            f2.write(line)
os.remove(settings.SHOPPING_CARS)
os.rename(settings.SHOPPING_CARS_TMP, settings.SHOPPING_CARS)
money = sum(total)
if account_total_coins < money:
    with open(settings.MAIDAODE_LIST_TMP, mode='r', encoding='utf-8') as f3 , \
    open(settings.SHOPPING_CARS, mode='a', encoding='utf-8') as f1:
        for line in f3:
            f1.write(line)
    os.remove(settings.MAIDAODE_LIST_TMP)
    retext='余额不足'
    print(retext)

else:
    with open(settings.MAIDAODE_LIST_TMP, mode='r', encoding='utf-8') as f3 , \
    open(settings.MAIDAODE_LIST, mode='a', encoding='utf-8') as f4:
        for line in f3:
            f4.write(line)
    os.remove(settings.MAIDAODE_LIST_TMP)
    total_coins = account_total_coins - int(money)
    retext='购买成功'+'\n'+'总价 '+str(money)+'金币'
    print(retext)
