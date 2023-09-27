numbers = [100, 2, 3, 4, 5]

#max([1, 2, 3, 4, 5])
max_num = max(numbers)

# print(max_num)

import random

random_number = random.randint(1, 100)

# print(random_number)

##########

menus = ['김밥', '라면', '만두']
random_number = random.randint(0, 2)
#print(menus[random_number])

menu = random.choice(menus)
#print(menu)

######

numbers = range(1, 46)
lucky_number = random.sample(numbers, 6)
# print(sorted(lucky_number))

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

#pip install requests
import requests

res = requests.get(URL)

requests.get(URL)

#print(res.text)

data= res.json()

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)
lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)
print(set(lucky_number) & set(lotto_number))