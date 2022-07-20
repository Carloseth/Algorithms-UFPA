def valordolar(fatura,dol):
    total = fatura *(2/100) #isso dá 30
    total1 = total * dol #isso dá 93
    tt2 = fatura * dol + total1
    return tt2
k = float(input('Insira o valor da fatura: '))

l = float(input('Qual a cotação atual do dolar? '))

J = valordolar(k,l)

J = ('%.0f'%J)

print(J)