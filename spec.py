from tinydb import TinyDB,Query

spec=open('spec.csv').read().split('\n')
db=TinyDB('db.json')
db.truncate()



for row in spec[1:]:
    m,c,p=spec[0].split(",")[1:]
    model,comp,price=row.split(',')[1:]
    db.insert({m:model,c:comp,p:price})
    
