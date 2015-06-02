__author__ = 'ammo'

import vincent
import random

list_data = []
for i in range(1,10):
    a = random.random()*100
    list_data.append(a)

bar = vincent.Bar(list_data)
# bar.to_json('www/bar.json', html_out=True, html_path='www/bar.html')
bar.to_json('www/bar.json')

