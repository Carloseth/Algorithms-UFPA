import math
#centimetros = metros * 100;
#ceil() arredonda pra cima
#floor() arredonda pra baixo
#.split()
def calcular_Quantidade_Lajotas(larg_Sala, comprimento_Sala, larg_lajota, comprimento_Lajota):
    larg_Sala *= 100
    comprimento_Sala *= 100
    qtd_Largura = larg_Sala / larg_lajota
    qtd_Largura = math.ceil(qtd_Largura)
    qtd_Comprimento = (comprimento_Sala / comprimento_Lajota)
    qtd_Comprimento = math.ceil(qtd_Comprimento)
    qtd_Total = qtd_Largura * qtd_Comprimento
    return qtd_Total
def programa():
    larg_Sala, comprimento_Sala = map(int, input(('Digite a largura e o comprimento da sala em metros:\n')).split())
    larg_Lajota, comprimento_Lajota = map(int,input(('Digite a largura e o comprimento da lajota em centimetros: \n ')).split())
    quantidade_Lajotas = calcular_Quantidade_Lajotas(larg_Sala, comprimento_Sala, larg_Lajota, comprimento_Lajota)
    print(f'Serão necessárias: {quantidade_Lajotas} lajotas para preencher a sala.')
programa()

#Aprendizado: Sempre passar variaveis de uma função como parametros na outra.
# aprendi a usar .ceil e .floor da biblioteca Math
# aprendi a usar as funções map() e split()