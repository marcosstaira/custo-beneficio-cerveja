print('Bem vindo ao seu programa cervejeiro, que lhe dirá qual opção de cerveja tem o melhor custo benefício! ')

def calculadoracerveja (cerveja1, cerveja2):

    custo1 = float(input(f'Digite o preço da {cerveja1} em R$'))
    custo2 = float(input(f'Digite o preço da {cerveja2} em R$ '))
    ml = int(input(f'Deseja inserir o volume da {cerveja1} em Mililitro(Digite 1) ou Litro(Digite 2)? '))
    if ml == 1:
        ml = int(input(f'Digite quantos ml tem a {cerveja1} '))
    elif ml == 2:
        ml = int(input(f'Digite quantos litros tem a {cerveja1} '))
        ml = ml * 1000

    custobeneficio1 = ml/custo1

    ml2 = int(input(f'Deseja inserir o volume da {cerveja2} Militro(Digite 1) ou Litro(Digite 2)? '))
    if ml2 == 1:
        ml2 = int(input(f'Digite quantos ml tem a {cerveja2} '))
    elif ml2 == 2:
        ml2 = int(input(f'Digite quantos litros tem sua a {cerveja2} '))
        ml2 = ml2 * 1000

    custobeneficio2 = ml2/custo2

    if custobeneficio1 > custobeneficio2:
        print(f'O custo benefício da {cerveja1} é melhor! ')
    elif custobeneficio2 > custobeneficio1:
        print(f'O custo benefício da {cerveja2} é melhor! ')
    else:
        print('As duas possuem o mesmo custo-benefício!')

calculadoracerveja(input('Digite o nome da cerveja 1 que deseja comparar. Ex: Antártica 1L '),input('Digite o nome da cerveja 2 que deseja comparar. Ex: Skol latão '))
loop = True
while loop == True:
    a = input('Deseja utilizar o programa novamente? Se sim digite 1, se não digite 0 para sair do programa')
    if a  == '1':
        calculadoracerveja(input('Digite o nome da cerveja 1 que deseja comparar. Ex: Antártica 1L '), input('Digite o nome da cerveja 2 que deseja comparar. Ex: Skol latão '))
    else:
        print('Você saiu do programa!')
        loop = False



