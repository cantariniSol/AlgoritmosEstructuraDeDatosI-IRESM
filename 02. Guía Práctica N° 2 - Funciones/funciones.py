def mayor10():
    n = int(input("Ingrese un número: "))
    if(n > 10):
       print(n)
    else:
        print(f"El número {n} es menor a diez.")

def sumaIgualAlTercero( a=0 , b=0, c=0 ):
    sumar = int(a + b)
    if (sumar == c):
        print(f"La suma de {a} y {b} es igual a {c}")
    else:
        print(f"La suma de {a} y {b} es distinta a {c}")


def dividirCuadrado(num1=1, num2=1):
    mayor = 0
    menor = 0

    if (num1 == num2):
        return str("Los numeros ingresados son iguales") # Esta linea solo debe retornar el numero 1
    elif (num1 >  num2):
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1

    div = int((mayor * mayor) / (menor * menor))
    return str(f"El resultado es: {div}") # Esta linea solo debe retornar la variable div

def celcius():
    f = int(input("Ingrese la temperatura en fahrenheit: "))
    c = int((5/9) * (f - 32))

    return c

