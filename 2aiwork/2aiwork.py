# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:51:00 2020

@author: mayukai
"""
import time

#birthday=time.localtime()

#while 1:
    #print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    #既然要检查宠物死掉了没 就要得到每时每刻的 时分秒
    #now_hour=time.localtime().tm_hour
    #now_sec=time.localtime().tm_sec
    #now_min=time.localtime().tm_min
    #print(str(now_min) +"分钟"+ str(now_sec)+"秒")

class pet:
    def __init__(self,name):
        self.name=name
        
        #下面的规定宠物的血量 
        self.blood=100
        #出生年月日
        self.birthday=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        
        #出生时候的时分秒，用于计算出生了多长时间用于计时
        self.birth_hour=time.localtime().tm_hour
        self.birth_sec=time.localtime().tm_sec
        self.birth_min=time.localtime().tm_min
        
        
        self.feedtime=time.localtime().tm_hour*3600+time.localtime().tm_min*60+time.localtime().tm_sec
        
    def askname(self):
        print('我叫：'+self.name)
    
    #既然我们现在的血量是一直在变化的,直接对其操作不好,于是喂食的思路是提高初始血量
    def feed(self):
        #吃一次饭 加20血
        self.blood=self.blood+20
        
        
        
        
    def askbirthday(self):
        print(self.birthday)
        
    def hello(self):
        print("主人跟%s说话了，好开心"%name)
        
    def love(self):
        print("主人好坏啊，我还小~~")
        
    def sing(self):
        print("葫芦娃，葫芦娃，一根藤上七朵花")
    
    #记录什么时候可爱的宠物会被饿死,1s掉3克血
    def deadtime(self):
        self.past_time=0-((self.birth_hour-time.localtime().tm_hour)*3600+\
            (time.localtime().tm_min-self.birth_min)*60+\
                (self.birth_sec-time.localtime().tm_sec))
        
        self.now_blood= self.blood-self.past_time*3
        
        if self.now_blood<=0:
            print("对不起，因为长时间没有喂食，你的宠物%s已经饿死了"%(self.name))
            return 0
   
    def note(self):
        self.now_feedtime=time.localtime().tm_hour*3600+time.localtime().tm_min*60+time.localtime().tm_sec
        self.past_feed_time=self.now_feedtime-self.feedtime
        self.feedtime=self.now_feedtime
        print("距离上次喂食已经过去了%d"% self.past_feed_time)
        print("现在血量是 %d"%self.now_blood)
        
        

print("请给你的宠物起一个名字")
name=input()
mypet=pet(name)

while 1:
    
    if    mypet.deadtime()==0:
        print("你的宠物死掉了 gameover")
        break
        
    print("主人您好，您想对我干什么\n1.问名字 2.喂食 3.问生日 4.打招呼 5.说“我爱你” 6.让我唱歌")
    case=int(input())
    if case==1:
        print("你的名字？")
        mypet.askname()
    elif case==2:
        print("让你吃东西")
        mypet.feed()
    elif case==3:
        print("你的生日？")
        mypet.askbirthday()
    elif case==4:
        print("你好")
        mypet.hello()
    elif case==5:
        print("我爱你")            
        mypet.love()
    elif case==6:
        print("唱歌")
        mypet.sing()
    else:
        print("你输入错了")
    print("\n")
    mypet.note()