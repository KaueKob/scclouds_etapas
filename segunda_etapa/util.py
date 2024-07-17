def validaEntradaFibonacci():
    while True:  
        n = int(input("N: "))  

        if n >= 0:
            return n; # quando n maior que 1 retorna o valor finalizando a execucao da funcao definindo o valor de n

        else:  
	        print("N deve ser maior ou igual a 0") 

def validaEntradaPrimos():
    while True:  
        n = int(input("N: "))  

        if n > 1:
            return n; # quando n maior que 1 retorna o valor finalizando a execucao da funcao definindo o valor de n

        else:  
	        print("N deve ser maior do que 1.") 
