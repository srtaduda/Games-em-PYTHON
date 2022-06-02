from random import choice
from time import sleep


print('-'*20)
print('-  J O K E N P Ô  - ')
print('-'*20)

print(''' - - - Opções: - - -
    (0) PEDRA
    (1) PAPEL
    (2) TESOURA''')

opcao = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

computador = ["PEDRA", "PAPEL", "TESOURA"]
c = choice(computador)
pedra = 'PEDRA'
tesoura = 'TESOURA'
papel = 'PAPEL' 

if opcao == 0:
    if c == 'TESOURA' and pedra == 'PEDRA':
        print(f'PARABÉNS, você venceu!\ncomputador escolheu {c}.')
    elif c == pedra:
        print(f'EMPATE, você jogou {pedra} e o computador jogou {c} também!')
    else:
        print(f'PERDEU! Você jogou {pedra}, computador jogou {c}.')

elif opcao == 1:
    if c == 'PEDRA' and papel == 'PAPEL':
        print(f'PARABÉNS, você venceu!\ncomputador escolheu {c}.')
    elif c == papel:
        print(f'EMPATE, você jogou {papel} e o computador jogou {c} também!')
    else: 
        print(f'PERDEU! Você jogou {papel}, computador jogou {c}.')

elif opcao == 2:
    if c == 'PAPEL' and tesoura == 'TESOURA':
        print(f'PARABÉNS, você venceu!\ncomputador escolheu {c}!')
    elif c == tesoura:
        print(f'EMPATE, você jogou {tesoura} e o computador jogou {c} também!')
    else: 
        print(f'PERDEU! Você jogou {tesoura}, Computador jogou {c}.')

        
   


