import json,os,random

def load(fileName='hello.db',autoDump = "False"):
    meraDB = MeraDB(fileName,autoDump)
    meraDB.load_file()
    return meraDB

class MeraDB():

    fileName = ""
    jObject = {}
    # how to print auto dump (without dupm funaction use how can set value)
    boolean = False

    def __init__(self, fileName,boolean):
        self.fileName = fileName
        self.boolean = boolean

    def load_file(self):
        print ("Loading Database from ", self.fileName, " !")
        if os.path.exists(self.fileName):
            #Cheacking for is there file exists or not
            data = open(self.fileName,"r").read()

        #If the file is exists then red either go to else and write data in fileName
            if(data == ""):
                print("nothing")  
            else:
                self.jObject = json.loads(data)
        #if there is no file then for making file
        else:
            file = open(self.fileName,'w')    
            self.jObject = json.loads(data)
          
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
        if(self.boolean == True):
            self.dump()
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
    def count_key(self,key):
        print len(self.jObject)
        return len(self.jObject)
    def del_db(self):
        self.jObject = {}
        return True
    def random_insert(self,number):
        for i in range (number):
            key=random.randint(0,100)
            value=random.randint(0,100)
            self.jObject[key]=value
        
        
         
          
    
        





        

