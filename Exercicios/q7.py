def pig(numsemanas,valorpig):
    umasemana = (1*7) + (2*2)
    total = umasemana * numsemanas 
    pai = valorpig - total
    return pai
k = int(input('Quantas semanas? '))

l = float(input('Qual o valor no porquinho? '))

J = pig(k,l)

J = ('%.2f'%J)

print(J)