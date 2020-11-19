# pymongo
import pymongo
import pandas as pd
from gridfs import GridFS
# util
import io

#URI

import os

class MongoGridFS:
    def __init__(self,uri): 
        self.connection = pymongo.MongoClient(uri)
    def setDB(self, dbname):
        self.db = self.connection[dbname]
    def setGridFS(self):
        self.fs = GridFS(self.db)
    # def put(self, data, **kwargs):
    #     self.fs.put(data, **kwargs)
    def getfile(self):
        return self.db.fs.files.find()
    def get(self, filename):
        content = self.fs.get_version(filename).read()
        content = content.decode("utf-8") #필수!
        file = io.StringIO(content)
        df = pd.read_csv(file,sep="\n",names=['data'])
        file.close()
        return df

def getFileFromDB(filename):
    # 객체생성 접속
    o = MongoGridFS(os.environ["mongoURI"])
    # db connect
    o.setDB('test')
    # GridFS 객체 생성
    o.setGridFS()
    # hello.txt 파일등록
    # o.put('hello.txt', filename="hello.txt")
    # 가져오기
    # ob = o.getfile()
    # for i in ob:
    #     print(i)
    ret = o.get(filename)
    return ret
