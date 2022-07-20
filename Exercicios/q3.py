def ValorDol(dol):
    x = 15000 * dol 
    return x
print('---> CONVERSÃO DE DOLAR PRA REAL <---')

l = float(input('Qual a cotação atual do Dolar?\n'))

R = ValorDol(l)

R = str('%.0f'%R)

print(f'Com a cotação atual do dolar de {l}$ valor em reais que precisa ser guardado é R${R}')