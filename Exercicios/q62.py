def mult(A,B):
    if B % A == 0:
        print('São multiplos')
    else:
        return 'Não são multiplos'
v1,v2 = map(int,input('Insira dois num separados por espaço: ').split())
L = mult(v1,v2)
print(L) 