'''
Desafio para vaga de desenvolvedor
github: github.com/TronGuy
'''

def inverter(string):
	new_string = ""
	for i in range(-1, -len(string) - 1, -1):
		new_string += string[i]
	return new_string

entrada = input("Digite o nome que deseja inverter:").strip()
nome = inverter(entrada)
print('String Invertida:',nome)
