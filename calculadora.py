#Seta o inicio do programa
on = 'S'
while on == 'S':
    #Pede o valor da compra e a quantia de dinheiro entregue, transformando em 2 casas após a virgula
    preco = float('{:.2f}'.format(float(input('Digite o valor da compra: '))))
    dinheiro = float('{:.2f}'.format(float(input('Digite a quantia de dinheiro entregue: '))))
    print

    #Puxa o 1 loop
    loop = 1
    céd = 100
    totcéd = 0
    moed = 1
    totmoed = 0
    troco = dinheiro - preco
    troco = float('{:.2f}'.format(float(troco)))
    troco = troco

    #Faz o start do 1 loop, de cédulas
    while loop == 1:
        
        #Verifica se o troco se encaixa em cédula
        if troco >= céd:
            troco -= céd
            totcéd += 1
        
        #Faz a classificação em cédulas
        else:
            if totcéd > 0:
                print(f'Total de {totcéd} cédulas de R${céd}')
            if céd == 100:
                céd = 50
            elif céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 2
            elif céd == 2:
                céd = 0
            totcéd = 0
            #Caso o troco for igual a 0, ou menor que 2 (maximo de cedula) ele passa para o loop 2
            if troco == 0 or troco <2:
                break

    loop = 2

    #Inicio o loop 2, classificação das moedas
    while loop == 2:
        if troco >= moed:
            troco -= moed
            totmoed += 1
        else:
            if totmoed > 0:
                print(f'Total de {totmoed} moedas de R${moed}')
            if moed == 1:
                moed = 0.50
            elif moed == 0.50:
                moed = 0.25
            elif moed == 0.25:
                moed = 0.05
            elif moed == 0.05:
                moed = 0.01
            elif moed == 0.01:
                moed = 0
            totmoed = 0
            #Transforma o Troco para um valor float com 2 casas após a virgula
            troco = float('{:.2f}'.format(float(troco)))
            #Caso o troco for zerado ele passa para a pergunta de uma nova consulta
            if troco == 0:
                loop = 3
                break
    #Pergunta de nova consulta
    while loop == 3:
        on = input('Deseja realizar mais uma uma consulta?(S ou N): ')
        break

#Caso não queira fazer uma nova consulta, ele finaliza
while on == 'N':
    print('         \033[1;95mPrograma finalizado')
    print('=-'*20)
    print('\033[0;0m')
    
    break