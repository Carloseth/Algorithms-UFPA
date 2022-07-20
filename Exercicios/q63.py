def reajuste1(salario):
    if salario >= 0 and salario <= 400:
        reajuste = salario * (15/100)
        total = salario + reajuste
        perc = 15

    elif salario > 400 and salario <=800:
        reajuste = salario + (12/100)
        total = salario + reajuste 
        perc = 12

    elif salario > 800 and salario <=1200:
        reajuste = salario + (10/100)
        total = salario + reajuste
        perc = 10
    elif salario > 1200 and salario <=2000:
        reajuste = salario + (7/100)
        total = salario + reajuste
        perc = 7
    else:
        reajuste = salario + (4/100)
        total = salario + reajuste
        perc = 4
    return f' Novo salário: {total:.2f} \n Rejuste ganho: {reajuste} \n Em percentual: {perc}%'
k = float(input('Digite o salário do funcionário: '))
resp = reajuste1(k)
print(resp)