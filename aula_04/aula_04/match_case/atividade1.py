codigo = int(input('Informe o código: '))

match codigo:
    case 1:
        print('Academia')
    case 2:
        print('Piscina')
    case 3:
        print('Salão de Festas')
    case 4:
        print('Cobertura VIP')
    case 5 | 6:
        print('Estacionamento')
    case 7 | 8 | 9:  # Utilização de | no lugar de or. Só para mostrar que é possível utilizar tbm desta forma.
        print('Áreas Comuns')
    case 10:
        print('Administração')
    case 11:
        print('Acesso Técnico')
    case _:
        print('Acesso negado')