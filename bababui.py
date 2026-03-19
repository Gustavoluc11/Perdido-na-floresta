print('Vc esta perdido em uma floresta')
caminho = input('Escolha um caminho (esquerda ou direita):').strip().lower()

#Esquerda

if caminho == 'esquerda':
        print('Vc encontrou um rio.')
        acao = input('Deseja atravessar ou voltar?: ').strip().lower()

        if acao == 'atravessar':
            print('Vc chegou a uma vila segura')
        elif acao == 'voltar':
            print('Vc permanece perdido na floresta')
        else:
            print('Opção invalida')

#Direira

elif caminho == 'direira':
    print('Vc encontrou uma montanha')
    acao = input('Deseja subir ou volta?:').strip().lower()

    if acao == 'subir':
        print('Vc encontrou um tesouro no topo')
    elif acao == 'voltar':
        print('Vc permanece perdido na floresta')
    else:
        print('Opção invalida')
