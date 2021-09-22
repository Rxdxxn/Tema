z=['L','Ma','Mi','J','V','S','D']
v=[1034,994,1022,1231,1303,998,1091]
s=0
for i in range(0,len(v)):
    s=s+v[i]
print('Venitul săptămînal =',s)
n= s/len(v)
print('Media venitului',n)
print('Cel mai mare venit este in ziua de',z[v.index(max(v))])
print('Cel mai mic venit este in ziua de',z[v.index(min(v))])
