import meradb
db=meradb.load("tab.db")
# db.set("name","nilam")
#db.set("class",150)
# db.set("address","bangalore")
db.get("name")
db.get("nilam")
db.get("class")
db.get_all()
db.rem("address")
db.exists("name")
db.dump()