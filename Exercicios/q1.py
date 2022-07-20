def valorGasto():
    distancia = 312
    autonomia_Do_Carro = float(input('Digite quantos KM seu carro faz por litro: '))
    preco = float(input('Digite o preco atual do combustivel: '))
    valor_Gasto_Gasolina = (distancia / autonomia_Do_Carro) * preco
    print(f'O valor gasto foi de: R${valor_Gasto_Gasolina:.2f}' )
valorGasto()