from colorama import *
from random import randint
from time import sleep
import sys
import os

# Definindo funções
def restart_program():
    python = sys.executable
    os.execl( python, python, * sys.argv )

def limpar_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

# Título
print(Fore.CYAN + '\t ADIVINHE')
print(Fore.CYAN + '_'  *30)
print()

# Introdução
print(Fore.WHITE + 'Vou pensar em um número de 1 a 100. Tente adivinhar...')
print(Fore.WHITE + 'Você tem 7 tentativas: ')
print()
print(Fore.CYAN + 'PROCESSANDO...')
print()

# Gerador de informações
numero_aleatorio = randint(1,100)
tentativas = 0
palpite = None

# Função principal
while palpite != numero_aleatorio:
	sleep(0.5)
	palpite = int(input(Fore.WHITE + Style.NORMAL + 'Digite seu palpite: '))
	tentativas = tentativas + 1
	
# Caso acerte
	if palpite == numero_aleatorio:
		print(Fore.GREEN + Style.BRIGHT + 'PARABÉNS! Você me venceu em {} tentativas'.format(tentativas))
		print(Fore.CYAN + Style.NORMAL + '_' *30)
		sleep(0.6)
		break;
		
# Tentativas
	elif tentativas >= 7 and palpite != numero_aleatorio:
		print(Fore.RED + Style.BRIGHT + 'Suas chances foram excedidas!!!')
		print(Fore.CYAN + Style.NORMAL + '_'  *30)
		print()
		sleep(0.6)
		break;
	
# Chutes	
	elif palpite > numero_aleatorio:
		print(Fore.RED + Style.BRIGHT + 'Hmmm... Chutou alto demais!!! Tente novamente:\n')
	elif palpite < numero_aleatorio:
		print(Fore.RED + Style.BRIGHT + 'Chute baixo! Tente denovo:\n')
		
# Finalização	
while True:
	if palpite == numero_aleatorio or tentativas >=3:
		inicializacao = input(Fore.WHITE + Style.NORMAL + '\nDeseja reinicar o jogo? [S ou N]: ')
        
	if inicializacao == 'N' or inicializacao == 'n' or inicializacao == 'nao':
		print(Fore.CYAN + '\nObrigado por jogar!\n')
		break;
							
# Reinicialização					
	elif inicializacao == 'S' or inicializacao == 's' or inicializacao == 'sim':
		print(Fore.CYAN + '\nREINICIANDO JOGO...')
		sleep(0.7)
		limpar_terminal()
		restart_program()
