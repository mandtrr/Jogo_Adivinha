from random import randint
computador = randint(0, 5)
print ('-=-' * 10)
print ('\033[31mVou pensar em um número entre o 0 e o 5. Tente adivinhar...\033[m')
print ('-=-' * 10)
jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!!')

else:
    print(f'Não foi dessa vez!! Pensei no número {computador} HAHAHA')