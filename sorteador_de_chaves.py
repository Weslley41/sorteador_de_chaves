import os
import platform
from random import choice
from time import sleep

def clear():
	if (platform.system() == 'Windows'):
		os.system("cls")
	else:
		os.system("clear")
	
	sleep(0.2)

# Recebe e faz uma lista dos jogadores.
lista_jogadores = []
def recebe_lista():
	clear()
	nome_jogador = input("Para encerrar a lista de jogadores digite 'end'\nDigite o nome do jogador:\n--| ")

	if (nome_jogador in lista_jogadores):
		print(f"O jogador {nome_jogador} já está na lista")
		sleep(1)
		recebe_lista()
	elif (nome_jogador.lower() == "vazio"):
		print("Desculpa não posso deixar você usar esse nome.")
		sleep(1)
		recebe_lista()
	elif (nome_jogador.lower() == "end"):
		print("Ok! Gerando os confrontos...")
		sleep(2)
		clear()
	else:
		lista_jogadores.append(nome_jogador)
		recebe_lista()

# Define o tamanho da chave e caso precise adiciona 'jogadores' para completar.
def tamanho_chaveamento(lista_jogadores, tamanho_da_chave = 2):
	qntd_jogadores = len(lista_jogadores)

	if (qntd_jogadores > tamanho_da_chave):
		return tamanho_chaveamento(lista_jogadores, tamanho_da_chave * 2)
	else:
		diferenca_chave_jogadores = tamanho_da_chave - qntd_jogadores
		for i in range(diferenca_chave_jogadores):
			lista_jogadores.append('vazio')

		return tamanho_da_chave

# Cria o vetor de estrutura dos confrontos.
def criar_chaveamento(lista_jogadores, tamanho_da_chave, chaveamento = []):
	i = 0
	for i in range(tamanho_da_chave // 2):
		chaveamento.append([[], []])
		i += 1

	return chaveamento

# Faz o sorteio da primeira rodada.
def sorteia_jogadores(lista_jogadores, tamanho_da_chave, chaveamento, indice = 0):
	jogador = choice(lista_jogadores)

	if (jogador == 'vazio' and 'vazio' in chaveamento[indice]):
		sorteia_jogadores(lista_jogadores, tamanho_da_chave, chaveamento, indice)
	else:
		if (chaveamento[indice][0] == []):
			chaveamento[indice][0] = jogador
		else:
			chaveamento[indice][1] = jogador

		lista_jogadores.remove(jogador)

	if ([] not in chaveamento[len(chaveamento) - 1]):
		return chaveamento
	elif ([] not in chaveamento[indice]):
		sorteia_jogadores(lista_jogadores, tamanho_da_chave, chaveamento, indice + 1)
	else:
		sorteia_jogadores(lista_jogadores, tamanho_da_chave, chaveamento, indice)

# Faz a leitura do vencedor de cada confronto.
def recebe_vencedor(chaveamento):
	vencedor = input(f"\nQuem ganhou o jogo?\n[1] {chaveamento[0]}\n[2] {chaveamento[1]}\n--| ")
	while (vencedor not in ['1', '2']):
		clear()
		print("Digite uma opção válida")
		sleep(0.5)
		vencedor = input(f"\nQuem ganhou o jogo?\n[1] {chaveamento[0]}\n[2] {chaveamento[1]}\n--| ")

	return int(vencedor)

# Avança as fases até chegar ao vencedor.
def proxima_fase(chaveamento, tamanho_da_chave):
	lista_vencedores = []
	for i in range(len(chaveamento)):
		if ('vazio' in chaveamento[i]):
			vencedor = 2 if (chaveamento[i][0] == 'vazio') else 1
		else:
			vencedor = recebe_vencedor(chaveamento[i])

		lista_vencedores.append(chaveamento[i][vencedor - 1])

	tamanho_da_chave //=  2
	novo_chaveamento = criar_chaveamento(lista_vencedores, tamanho_da_chave, [])
	for j in range(0, tamanho_da_chave, 2):
		novo_chaveamento[j // 2][0] = lista_vencedores[j]
		novo_chaveamento[j // 2][1] = lista_vencedores[j + 1]

	# Controle: Passa para próxima fase ou final
	if (tamanho_da_chave > 2):
		clear()
		print("Próxima rodada:")
		sleep(1.5)
		imprimir(novo_chaveamento)
		sleep(1)
		proxima_fase(novo_chaveamento, tamanho_da_chave)
	else:
		clear()
		print("Chegamos na final!")
		sleep(2)
		vencedor = lista_vencedores[recebe_vencedor(lista_vencedores) - 1]
		
		clear()
		sleep(0.2)
		print(f"Vencedor: {vencedor}")
		sleep(3)

# Imprimir jogos da rodada no terminal
def imprimir(chaveamento):
	for i in range(len(chaveamento)):
		print(f"Jogo {i+1}: {chaveamento[i][0]} x {chaveamento[i][1]}")
		sleep(0.3)
	sleep(2)


def iniciar():
	clear()
	recebe_lista()
	tamanho_da_chave = tamanho_chaveamento(lista_jogadores)
	chaveamento = criar_chaveamento(lista_jogadores, tamanho_da_chave)
	sorteia_jogadores(lista_jogadores, tamanho_da_chave, chaveamento)
	imprimir(chaveamento)
	proxima_fase(chaveamento, tamanho_da_chave)


iniciar()
