def bola():
  p,r = map(int,input('0--->esqueda\n1--->direita\n').split())
  if p == 1 and r == 1:
    print('A')
  elif p == 1 and r == 0:
    print('B')
  elif p == 0 and r == 0:
    print('C')
  elif p == 0:
    print('C')
bola()