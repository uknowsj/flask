import pymongo
import pandas as pd


ip_address = 'localhost'
connection = pymongo.MongoClient('mongodb://%s' %(ip_address))
#connection  = pymongo.MongoClient('mongodb://%s:%s@%s' %(username,password,ip_address))
py_db = connection.py_db
py_collection = py_db.py_collection #make collection, 데이터 업로드 후 생성됨

#py_collection.insert_one({'name':'john'})
from gridfs import GridFS

# db = pymongo.MongoClient().gridfs_example #gridfs_example db 생성
# fs = GridFS(db) #gridFs 객체 생성
# file_id = fs.put("hello world",encoding="utf-8") #create new file in GridFS and return the value of the file documents _id key
# a=fs.get(file_id).read()
# a=a.decode("utf-8")
# print(a)


test = connection.test
fs = test.fs.files
cursor_fs = GridFS(test)
sample= fs.find_one({"filename":"sample.txt"})
#print("sample",sample)
sample_id = sample["_id"]

import io
o = cursor_fs.get_version("sample.txt").read()
odata = cursor_fs.get_version("sample2.txt").read()
print("o : ",o)
print("odata : ",odata)


o = o.decode("utf-8") #필수!
ofile = io.StringIO(o)
df2 = pd.read_csv(ofile,sep="\n",names=['data'])
print("df2 : ",df2)
ofile.close()

res = cursor_fs.get(sample_id).read()
#print(type(res))

res=res.decode("utf-8")


strfile = io.StringIO(res)
df = pd.read_csv(strfile,sep='\n',names = ['data'])
print("\n\n\n\n")
#print(df)
strfile.close()

