from operator import is_
from util import validaEntradaPrimos

# criando a lista de numeros primos
nums_primo = []  

# chamando a funcao com numero_valido
numero_valido = validaEntradaPrimos()

# funcao que usa recursao para verificacao de numero primo
def is_primo(a, b):  		
	if a == b:	
		return True  # valor valido pra quando i tiver valor de 2 e colocar como numero primo ja que a contagem começa de 2

	elif b % a == 0:  # se divisivel por algum numero menor e restar 0 na divisel, definir nao numero primo
		return False

	else:  
		return is_primo(a + 1, b) # sem em caso de nem um nem outro, passar para o proximo anterior ate ficar em a == b

# inciando loop, se verdadeiro adiciona a lista na ultima posiçao se falso passa para o proximo numero do range
for i in range(2, numero_valido + 1):  

	if is_primo(2, i):  
		nums_primo.append(i)  # adiciona o valor na lista a partir do ultimo adicionado

# mostra o resultado ao usuario
print(f"p({numero_valido}) = {nums_primo}")  
