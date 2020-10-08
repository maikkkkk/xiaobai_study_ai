data_dict={}
#exm=("xiaoa":(1,2,3),"xiaob":(2,3,4)}
# with 表示是模块，当这个模块结束之后 会自动关闭文件
with open("E:/project/github/1aiwork/成绩单.txt",'r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        datas=line.split() #datas是最后一行的切割 
        name=datas[0]
        yuwen=int(datas[1])
        shxuue=int(datas[2])
        yingyu=int(datas[3])
        total=yuwen+shxuue+yingyu
        #再用字典保存在一起 首先创建 一个空字典
        data_dict.update({name:[yuwen,shxuue,yingyu,total]})  
        

#把语句放到print（）外面 意味着print（） 就已经关闭了文件
print(datas)
#这个order 之后就是里面是元组的列表
data_order=sorted(data_dict.items(),key=(lambda x:x[1][3]),reverse=True)
#%% 先做来名次 然后再加排名
#先保存上一个的成绩和名次的问题,然后再比较 然后看名字要不要相等
for item in data_order:
    name=item[0]
    chengji=item[]


#print(data_order)