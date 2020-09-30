# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:59:22 2020

@author: 37494
"""

import pandas as pd

chengji=pd.read_csv('C:\\Users\\37494\\Desktop\\成绩单.csv',sep='\t',header=None)
print(chengji.index)
#数据框的情况

#改一下列名
print(chengji.columns)
chengji.columns=['name','chinese','math','english']
print(chengji.columns)

#数据框的所有值
print(chengji.values)
print(chengji.shape)
print(dir(chengji))

#读取数据框的数据
#每行的key可以作为一个属性
print(chengji.chinese)
print('chinese' in dir(chengji))

#%%
print('chinese' in dir(chengji))

#%% 不行失败了
#chengji.reindex(chengji.columns.insert(5,'sum'))
#%%
chengji.drop(1,1)

#%%
print(chengji['chinese'])  #可以有两种方式找到某一列
del chengji[:5]
#%%
print(chengji.columns)

#%%
chengji.insert(4,'sum',chengji.chinese+chengji.math+chengji.english)

#%%不能用省略号 要直接用columns
huizong=pd.DataFrame(columns=['name','sum','rank'])
print('sort_values' in  dir(chengji))
print(chengji.sort_values(by='sum',axis=0,ascending=True))
chengjisorted=chengji.sort_values(['sum'],axis=0,ascending=True)

#%%
huizong['name']=chengjisorted['name']

#%%索引值没有发生变化，如何修改呢？
print(huizong['name'][0])
#%%
for i in range(264):
    huizong['name'][i]=i
#%%
huizong['sum']='总分是:'+str(chengjisorted['sum'])

#%%
huizong['sum']=chengjisorted['sum']
#%%
huizong['sum']=str('a'+str(huizong['sum']))

#%%修改 index
huizong.index=range(263)
huizong.index=huizong.index+1
#%%
#%%注意有的时候都是indexs 和colcomns 的 没有 s 的时候的区别
for indexs in huizong.index:
    huizong['sum'][indexs]='总分:'+ str(huizong['sum'][indexs])
#%%？？？？
#for indexs in huizong.index:
#    huizong['rank']=('并列排名：'+str(huizong['index'][indexs-1]))if(huizong['rank'][indexs]==(huizong['rank'][indexs-1]))else('排名：'+str(huizong['index'][indexs]))
#%%
for indexs in huizong:
    print(huizong[indexs])
    
    #%%
huizong['rank2']=range(263)
huizong['rank2']=huizong['rank2']+1
#%%注意越界问题
for i in range(262):
    if huizong['sum'][i+1]==huizong['sum'][i]:
        huizong['rank'][i]='并列排名：'+str(huizong['rank2'][i-1])
    else:
        huizong['rank'][i]='排名'+str(i)
        #%%
for i in range(263):
   print(huizong['rank'][i])
   
#%%
huizong.index=sorted(huizong.index,reverse=True)

#%%
for i in range(1,264):
    if i>1 and i<263: 
        if huizong['sum'][i]!=huizong['sum'][i-1] and huizong['sum'][i]==huizong['sum'][i+1]:
            huizong['rank'][i]='并列排名:'+str(i)
        elif huizong['sum'][i]!=huizong['sum'][i-1] and huizong['sum'][i]!=huizong['sum'][i+1]:
            huizong['rank'][i]='排名:'+str(i)
        else:
            huizong['rank'][i]=huizong['rank'][i-1]
            
    elif i==1:
        if huizong['sum'][i]==huizong['sum'][i+1]:
            huizong['rank'][i]='并列排名:'+str(i)
        else:
            huizong['rank'][i]='排名:'+str(i)
    elif i==263:
        if huizong['sum'][i]==huizong['sum'][i-1]:
            huizong['rank'][i]='并列排名:'+str(i)
        else:
            huizong['rank'][i]='排名:'+str(i)
#%%插入列的时候必须赋值,和变量的对应了起来
huizong['a']='t'
#%%

for i in range(1,264):
    huizong['t'][i]=i
    if huizong['t'][i]%5==2:
        print(huizong['t'][i])   
#%%
del huizong['a']
del huizong['t']
#%%
huizong['t']=range(1,264)
#%%
huizong=huizong.sort_values(['t'],axis=0,ascending=False)
#%%
del huizong['t']
#%%必须保存为一个文件
huizong.to_csv("C:\\Users\\37494\\Desktop\\123.txt",index=False)


    