import re
from urllib.request import urlopen
from collections import defaultdict

names = defaultdict(int)
URL = 'http://shannon.usu.edu.ru/ftp/python/hw2/home.html'
page = urlopen(URL)
text = page.read().decode('cp1251')
start = text.find("Студенты мат-меха")
text = text[start+len("Студенты мат-меха"):]
full_names = re.findall(r'>[a-яА-ЯёЁ]+ [a-яА-ЯёЁ]+', text)

for f in full_names:
    names[f.split(' ')[1]] += 1

sorted_names = dict(sorted(names.items(), key=lambda x: x[1], reverse=True))

print("Женщины:")
for v in sorted_names:
    if v[-1:] in "уеоиаяюаы" and not (v in "ИльяНикитаАлехандроЛёва") or v == "Любовь":
        print(f'{v}: {names[v]}')

print("\nМужчины")
for v in sorted_names:
    if not (re.match('[уеиоэюая]', v) and not (v in "ИльяНикитаАлехандроЛёва") or v == "Любовь"):
     print(f'{v}: {names[v]}')
