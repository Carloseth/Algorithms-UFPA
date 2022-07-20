def porcdesconto(vtotal,vpago):
    desconto = vtotal - vpago 
    porcentagem = desconto / vtotal
    return f'O valor total da compra foi {vtotal} com o desconto saiu {vpago}, logo o desconto foi de {porcentagem}'

print('---> DESCONTO POR PEÇA <---')

k = float(input('Qual o valor total da compra?\n'))

j = float(input('Qual foi o valor pago?\n'))

d = porcdesconto(k,j)
#d = str('%.2f'%d)
print(d)