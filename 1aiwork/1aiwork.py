import pandas as pd

#导入数据
grade=pd.read_csv('C:\\Users\\37494\\Desktop\\成绩单.txt',sep='\t',header=None)
grade.columns=['name','chinese','math','english']

#计算
grade['sum']=grade['chinese']+grade['math']+grade['english']

#排序
gradesorted=grade.sort_values(by='sum',ascending=False)

#把index换一下
gradesorted.index=range(1,264)

#每一个i 要对前面的 和后面的 都比对 才可以
gradesorted['grade']=''
for i in gradesorted.index:
    if i>1 and i<263:
        if gradesorted['sum'][i]!=gradesorted['sum'][i-1]:
            if gradesorted['sum'][i]!=gradesorted['sum'][i+1]:
                gradesorted['grade'][i]="排名"+str(i)
            else:
                gradesorted['grade'][i]="并列排名"+str(i)
        else:
            gradesorted['grade'][i]=gradesorted['grade'][i-1]
    elif i==1:
         if gradesorted['sum'][i]!=gradesorted['sum'][i+1]:
                gradesorted['grade'][i]="排名"+str(i)
         else:
                gradesorted['grade'][i]="并列排名"+str(i)
    elif i==263:
         if gradesorted['sum'][i]!=gradesorted['sum'][i-1]:
                gradesorted['grade'][i]="排名"+str(i)
         else:
                gradesorted['grade'][i]="并列排名"+str(i-1)
 
#保存数据
gradesorted.to_csv('E:\\project\\python\\work\\总成绩排名.txt',sep='\t',index=False)

#%%查询程序
while(1):
    print("input a name")
    name=input()
    gradedone=pd.read_csv('E:\\project\\python\\work\\总成绩排名.txt',sep='\t')
    for i in gradedone.index:
        if name==gradedone['name'][i]:
            print(gradedone['grade'][i])
    