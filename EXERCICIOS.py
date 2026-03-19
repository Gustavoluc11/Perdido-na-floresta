idade = int(input('Digite sua idade: '))
ingresso = input('Você tem ingresso? (sim/não): ').lower()

if idade >= 18 and ingresso == 'sim':
    print('Seja bem-vindo')
else:
    if idade < 18:
        print('Vc não pode entra pq é menor de idade')
    if ingresso != 'sim':
        print('Você não pode entrar pq n tem ingresso')