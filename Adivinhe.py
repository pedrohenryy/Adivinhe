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
	
def espaco():
	print(' '  *30 )

# Título

espaco()
print(Fore.CYAN + '\t ADIVINHE ')
print(Fore.CYAN + '_'  *30)
print(' ' *30)

# Introdução

print(Fore.WHITE + 'Vou pensar em um número de 1 a 100, tente adivinhar... ')
print(Fore.WHITE + 'Você tem 7 tentativas: ')
espaco()
print(Fore.CYAN + 'PROCESSANDO... ')
espaco()

# Gerador de informações

número_aleatório = randint( 1,100 )
tentativas = 0
palpite = None

# Função principal

while palpite != número_aleatório:
	sleep( 0.5 )
	palpite = int(input(Fore.WHITE + Style.NORMAL + 'Digite seu palpite: '))
	espaco()
	tentativas = tentativas + 1
	
# Caso acerte
	
	if palpite == número_aleatório:
		espaco()
		print(Fore.GREEN + Style.BRIGHT + 'PARABÉNS!  Você me venceu em {} tentativas '.format( tentativas ))
		print(Fore.CYAN + Style.NORMAL + '_' *30)
		sleep( 0.6 )
		espaco()
		break;
		
# Tentativas
		
	elif tentativas >= 7 and palpite != número_aleatório:
		espaco()
		print(Fore.RED + Style.BRIGHT + 'Suas chances foram excedidas!! ')
		print(Fore.CYAN + Style.NORMAL + '_'  *30)
		espaco()
		sleep( 0.6 )
		break;
	
# Chutes
		
	elif palpite > número_aleatório:
		print(Fore.RED + Style.BRIGHT + 'Hmm... Chutou alto demais!! tente novamente: ')
	elif palpite < número_aleatório:
		print(Fore.RED + Style.BRIGHT + 'Chute baixo! Tente denovo: ')
		
# Finalização
		
while True:
						if palpite == número_aleatório or tentativas >=3:
							inicializacao = input(Fore.WHITE + Style.NORMAL + 'Deseja reinicar o jogo ? ')
							espaco()
							
						if inicializacao == 'n' or inicializacao == 'não':
							print(Fore.CYAN + 'Obrigado por jogar! ')
							break;
							
# Reinicialização					
						
						elif inicializacao == 's' or inicializacao == 'sim':
							
							print(Fore.CYAN + 'REINICIANDO JOGO... ')
							sleep( 0.7 )
							limpar_terminal()
							restart_program()
