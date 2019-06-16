import json,os
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
        print ("Loading Database from ", self.fileName, " !")
        if os.path.exists(self.fileName):
        #If the file is exists then red either go to else and write data in fileName

            file = open(self.fileName,'r')
        else:
            file = open(self.fileName,'w')    
        data = file.read()
        #if there is no data then dump whole data and if there is data then go to else parts and do loads data in jObject
        if data=="":
            self.dump()
        else:
            self.jObject = json.loads(data)
        print ("DB loaded successfully!")
        return self.jObject

    def dump(self):
        print ("Dumping database to ", self.fileName, " !")
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()

        print ("DB dumped successfully!")
        return "OK"
    def set(self,key,value):
        self.jObject[key]=value
        return True
    def get(self,key):
        try:
            print (self.jObject[key])
            return self.jObject[key]

        except: 
            print ("there is no key " + key)  
            return False
    def get_all(self):
        list=[]
        for key in  self.jObject:
            list.append(key)
        print (list)
        return list
    def rem(self,key):
        try:
            del self.jObject[key]
            return True
        except:
            print ("there is no key " + key)
            return False
    def exists(self,key):
        if key in self.jObject:
            print (True)
            return True
        else:
            print (False)
            return False

        

