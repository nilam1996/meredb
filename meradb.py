import json
def load(fileName='hello.db'):
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

class MeraDB():

    fileName = ""
    jObject = {}

    def __init__(self, fileName):
        self.fileName = fileName

    def load_file(self):
        print "Loading Database from ", self.fileName, " !"
        content = open(self.fileName).read()
        if content=="":
            self.dump()
        else:
            self.jObject = json.loads(content)
        print "DB loaded successfully!"
        return self.jObject

    def dump(self):
        print "Dumping database to ", self.fileName, " !"
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()

        print "DB dumped successfully!"
        return "OK"