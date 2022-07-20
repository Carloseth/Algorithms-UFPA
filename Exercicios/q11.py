#QUESTÃO 11 V
def consumo2(rskwh,fatura):
    consumodew = (fatura/rskwh) *1000
    return consumodew
print("--->Consumo de watts<---")

k = float(input('Insira o valor em reais de 1Kw: \n'))

l = float(input('Insira o valor da fatura em reais:\n'))

J = consumo2(k,l)

J = ('%.0f'%J)

print(f'Valor de 1KW R${k}\n Fatura:R${l}\n consumo em Watts:{J}')