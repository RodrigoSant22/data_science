'''salario = int(input('Salário? '))
imposto = input('Imposto em % (ex: 27.5)? ')

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)

if imposto < 10.:
    print('Imposto Baixo')
elif imposto > = 10. and <= 27.:
    print('Imposto Médio')
elif imposto >= 27. and >= 100:
    print('Imposto Alto')
else:
    print('Imposto Inválido')

imposto = 27.

while imposto > 0:
    imposto = input('Imposto ou (s) para sair: ')
    if not imposto:
        imposto = 27.
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)
    print('Valor real: %s', salario - (salario * (imposto * 0.01)))

    

#valor_imposto = 'Alto' if imposto < 27.5 else 'Muito Alto'
#print(valor_imposto)

#print('Valor real: {0}'.format(salario - (salario * (imposto * 0.01))))'''

def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * (imposto * 0.01))

print(salario_descontado_imposto(4000,imposto=7.))