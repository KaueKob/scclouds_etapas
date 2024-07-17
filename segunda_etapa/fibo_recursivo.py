from util import validaEntradaFibonacci

numero_valido = validaEntradaFibonacci()
def fib(value):
	
	if value == 0 or value == 1:   # essa funcao faz chamadas recursivas ate chegar ao caso base com a relaçao F(n)=F(n−1)+F(n−2).
		return value

	else:
		return fib(value - 1) + fib(value - 2)  # nesse caso ele vai diminuindo, ate chegar no caso base, 
	                                            # armazenando os values pra depois fazer a soma.


print(f"fib({numero_valido}) = {fib(numero_valido)}")  # a partir do calculo ele informa o resultado de fibonacci