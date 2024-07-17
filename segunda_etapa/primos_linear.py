from util import validaEntradaPrimos

# criando lista de numeros primos
nums_primo = []  
numero_valido = validaEntradaPrimos();

# criando laco de repeticao para verificacao de numero primo
for i in range(2, numero_valido + 1):  
	
	for j in range(2, i):  
		if i % j == 0: 
			break   # em caso de o numero for dividido por um numero menor e restar 0, definir nao numero primo
	
	else:
		nums_primo.append(i) 

# exibindo resultado de numero primos ao usuario
print(f"p({numero_valido}) = {nums_primo}")  

