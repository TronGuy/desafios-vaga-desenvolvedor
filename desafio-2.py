'''
Desafio para a vaga de desenvolvedor
github: github.com/TronGuy
'''
#Funções
def fibonacci(number):
	while len(numbers) <= number:
		result = numbers[-1] + numbers[len(numbers) -2]
		numbers.append(result)
	for i in numbers:
		print(i)

def start():
	print(" --------- ALGORITIMO FIBONACCI ---------- ")
	entrada = int(input('Quantidade de termos desejada: ').strip())
	fibonacci(entrada)	

#Inicialização
numbers = [0,1]
result = 0
start()



