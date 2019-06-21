# import meradb
# db=meradb.load("nilu.db")
# db.set("name","nilam")
#db.set("class",150)
# db.set("address","bangalore")
# db.get("name")
# db.get("nilam")
# db.get("class")
# db.get_all()
# db.rem("address")
# db.exists("name")
# db.count_key("key")
# # db.del_db()
# db.random_insert(10)
# db.set("news","india today")
# # db.dump()

# import meradb
# db1 = meradb.load('nilam.db')
# db1.set('key1', 'value1')
# db1.get('key1')True
# db1.set('key2', 'value2')
# db1.get('key2')
import meradb
a=meradb.load("nav.db")
a.set("hi","hello")
a.get("hi")
a.random_insert(10)


b = meradb.load("gurukul.db")
b.set("key","value")