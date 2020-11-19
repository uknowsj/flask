import pandas as pd
from pandas import DataFrame as df

df1 = pd.DataFrame({'text':[],'score':[]})
df1.loc[0]=['hi1',20]
df1.loc[1]=['hi2',30]
df1.loc[2]=['hi3',40]
df1.loc[3]=['hi4',50]
# df2 = df1.sort_values(by="score", ascending=False).head(2)
# print(list(df2['text']))

# df3 = df1.sort_values(by="score", ascending=False).head(2)
# print(df3)



# list1 = ['11111','11111','11111111']
# list2 = ['2222222','22','22222']

# list1.extend(list2)
# print(list1)

# dic={}
# dic["pos"]=list1
# dic["neg"]=['sadas','asda']

# dic2={}
# dic2['33']=dic
# print(dic2)


print(df1)
t = str(df1['text'])
t=t.lower()
print(t)