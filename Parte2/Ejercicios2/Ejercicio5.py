#creando una funcion que muestre la serie fibonacci entre el 0 al el numero adao
def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista #Cuando a+b sea mayor que num yo no seguira ejecutandose
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(20)
print(resultado)



prime_hasta = lambda num: list(filter(lambda x: all (x % i != 0 for i in range(2,int(x ** 0.5) +1 )),range(2,num)))
print(prime_hasta)
#Muestra[2,3,5,7,11,13]