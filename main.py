import random
import sys
import replit
from desenhaVida import *

palavras = ["computador","programa","codificar","aula","maquina","professor","codecomet"]

palavra_escolhida = palavras[random.randint(0,len(palavras))-1]

vidas = 6
tentativas = 0
erros=[]

secreto = "-" * len(palavra_escolhida)

while secreto != palavra_escolhida:
	replit.clear()

	if vidas == 0:
		desenha_vida(0)
		print("Não foi dessa vez! Tente de novo!")
		sys.exit()
	
	tentativas+=1
	
	print (secreto)
	
	print("Vidas: ", vidas)
	desenha_vida(vidas)
	
	if len(erros)>0:
		print("Letras Erradas: ",erros)
	else:
		print("Letras Erradas:")

	letra = "--"
	while len(letra)>1:
		letra = input("Digite uma letra: ")
		if len(letra)>1:
			print("Por favor, digite apenas uma letra")

	tem_letra = []
	for i in range(len(palavra_escolhida)):
		if letra == palavra_escolhida[i]:
			tem_letra.append(i)
	
	if len(tem_letra)<1:
		vidas-=1
		erros.append(letra)

	for i in range(len(tem_letra)):
		secreto = secreto[:tem_letra[i]] + letra + secreto[tem_letra[i]+1:]

replit.clear()
print(secreto)
print("""	
			+---+
			|	|
			 	|
			 	|   O
				|  \|/
				|  / \
			========""")
print("Parabéns! Você acertou em ", tentativas, " tentativas")