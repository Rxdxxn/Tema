p=1
x=[1,3,5,7,9]
y=[2,4,6,8,10]
print('Suma tuturor componentelor de x=',sum(x))
print('Suma tuturor componenetelor de y=',sum(y))
print('Suma primelor trei componente=',sum(x[:3]))
for i in range(0,len(x)):
    p=p*x[i]
print('Produsul x=',p)
print('Valoarea absoluta=',y[2])
print('Suma primelor componente=',sum(x[:1]+y[:1]))

