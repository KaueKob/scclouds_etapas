from util import validaEntradaFibonacci

fib_arr = [0, 1]  
numero_valido = validaEntradaFibonacci();

if numero_valido < 2:               
    print(f"fib({numero_valido}) = {numero_valido}")  # em caso de valor de n menor que 2 ele retorna o valor digitado

else: 
    # em caso de n > 2 ele incia um loop adicionando
    # os resultados na lista pra depois que chegar no range maximo
    # para calcular a sequência é somado os dois numeros anteriores
    for i in range(2, numero_valido + 1):  
        fib_arr.append((fib_arr[i - 1]) + (fib_arr[i - 2])) 
    print(f"fib({numero_valido}) = {fib_arr[numero_valido]}")  
