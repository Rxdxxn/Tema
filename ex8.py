h=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[3,4,4,5,5,5,5,6,6,6,7,8,9,10,11,14,15,14,14,10,8,7,5,4]
gt=sum(t)
tm=round(gt/24)
print('temperatura medie este', tm)
x=max(t)
y=min(t)
print('maximul temperaturii este', x,'; minimul temperaturii este', y)
n=h[t.index(x)]
print('temperatura maxima s-a inregistrat la orele',n)
m=h[t.index(y)]
print('d)temperatura minima s-a inregistrat la orele',m)