def consumo(rskwh,consumomensal):
    fatura = rskwh * consumomensal/1000
    return fatura
print('--->Conta de luz de acordo com o consumido<---')

k = float(input("Insira o valor do KWH: \n"))

l = int(input('Insira o consumo mensal em WH:\n'))

J = consumo(k,l)

J =('%.2f'%J)

print(f' O usuário consumiu:{l}W\n sendo cobrado:R${k} por hora\n será cobrado na fatura:R${J}')