from random import randint
import sys
import os
from time import sleep

# Definindo funções
	
def restart_program():
    python = sys.executable
    os.execl( python, python, * sys.argv )
    
def limpar_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def espaco():
	print(' '  *30 )
	
# Título

espaco()
print('\033[36m \t ADIVINHE ')
espaco()

# Introdução

print('\033[97m Vou pensar em um número de 1 a 100. tente adivinhar...')
print('\033[97m Você tem 7 tentativas:')
print()
print('\033[36m PROCESSANDO...')
print()

# Gerador de informações

numero_aleatorio = randint(1, 5)
tentativas = 0
palpite = None

# Função principal

while palpite != numero_aleatorio:
	sleep(0.5)
	palpite = int(input('\033[0;37m Digite seu palpite: '))
	tentativas = tentativas + 1
	
# Caso acerte
	
	if palpite == numero_aleatorio:
		espaco()
		print('\033[1;32m PARABÉNS!  Você me venceu em {} tentativas'.format( tentativas ))
		sleep(0.6)
		espaco()
		break;
		
# Tentativas
		
	elif tentativas >= 3 and palpite != numero_aleatorio:
		espaco()
		print('\033[1;31m Suas chances foram excedidas!!')
		print( )
		sleep(0.6)
		break;
	
# Chutes
		
	elif palpite > numero_aleatorio:
		print('\033[1;31m Hmm... Chutou alto demais!! tente novamente: ')
	elif palpite < numero_aleatorio:
		print('\033[1;31m Chute baixo! Tente denovo: ')
		
# Finalização
		
while True:
						if palpite == numero_aleatorio or tentativas >=3:
							inicializacao = input('\033[0;36m Deseja reinicar o jogo ? ').lower()
							espaco()
							
						if inicializacao == 'n' or inicializacao == 'não':
							print('\033[36m Obrigado por jogar!')
							break;
							
# Reinicialização					
						
						elif inicializacao == 's' or inicializacao == 'sim':
							
							print('\033[36m REINICIANDO JOGO...')
							sleep(0.7)
							limpar_terminal()
							restart_program(
