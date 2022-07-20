def programa():
    x = [int(x) for x in input().split()]
    result = calculadora(x)
    print(result)
def calculadora(l):
    menor = l[0]
    maior = l[0]
    s = 0
    for x in l:
        if x < menor:
            menor = x
        if x > maior:
            maior = x
    soma = maior + menor
    mult = maior * menor
    div = maior / menor
    menos = maior - menor
    print(f'{maior} + {menor} = {soma}')
    print(f'{maior} * {menor} = {mult}')
    print (f'{maior} / {menor} = {div}')
    print (f'{maior} - {menor} = {menos}')
programa()
