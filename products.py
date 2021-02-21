from tinydb import TinyDB,Query
from pprint import pprint

db=TinyDB('db.json')
file=open('pro.csv').read().split('\n')
db.truncate()

for item in file[1:]:
    categ,comp=item.split(',')[1:]
    # print(categ,comp)
    db.insert({"category":categ,"company":comp})