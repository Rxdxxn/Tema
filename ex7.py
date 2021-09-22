z=['L','Ma','Mi','J','V','S','D']
v=[1234,1342,4321,1432,3241,3421,1243]
x=sum(v)
print('venitul al intreprinderii intr-o saptamana este', x)
y=round(x/7,2)
print('media venitului zilnic este', y)
n=z[v.index(max(v))]
print('ziua cu cel mai mare venit este', n)
m=z[v.index(min(v))]
print('ziua cu cel mai mic venit este', m)
