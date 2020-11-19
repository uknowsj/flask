import os
path_dir = 'C:/Users/User/Downloads/flask/test/data'
file_list = os.listdir(path_dir)

for i in file_list:
    print('mongofiles --uri "mongodb+srv://yang:yang0803@test.xgkqo.mongodb.net/test" put %s\n' %(i));