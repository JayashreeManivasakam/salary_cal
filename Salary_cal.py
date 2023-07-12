sun=int(input())
mon=int(input())
tue=int(input())
wed=int(input())
thr=int(input())
fri=int(input())
sat=int(input())
sum = 0
ws=0
w=[mon,tue,wed,thr,fri]
for i in range (0,5):
    sum=sum+100*w[i]
    if(w[i]>8):
        sum=sum+((w[i]-8)*15)
    ws=w[i]+ws
    if(ws>40):
        sum=sum+((ws-40)*25)
if(sun>0):
    sum=sum+(sun*50)+(sun*100)
if(sat>0):
    sum=sum+(sat*25)+(sat*100)
print(sum)
