__author__ = 'ammo'

import vincent
import random

list_data = []
for i in range(1,10):
    a = random.random()*100
    list_data.append(a)

bar = vincent.Bar(list_data)
# bar.to_json('www/bar.json', html_out=True, html_path='www/bar.html')
cats = ['c1','c2','c3']
index = range(10,20,30)

line = vincent.Line(test[['line1','line2','line3']])
line.axis_titles(x='Date', y='Price')
line.legend(title='Test Amir')

bar.to_json('www/bar.json')

