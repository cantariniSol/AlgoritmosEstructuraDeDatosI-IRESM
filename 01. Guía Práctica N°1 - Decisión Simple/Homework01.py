
def mayorA10(num):
    if (num > 10):
        print(f"El numero {num} es mayor a 10")
    else:
       print(f"El número {num} es igual o meno a 10")


mayorA10(8)

def dividirCuadrado(num1, num2):
    mayor = 0
    menor = 0

    if (num1 == num2):
        print(f'Los numeros ingresados son iguales.')
    elif (num1 >  num2):
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1


    div = (mayor * mayor) / (menor * menor)
    print(f'El resultado es: {div}')

dividirCuadrado(9, 3)

def celcius(f):

    c = (5/9) * (f - 32)
    print(f'La temperatura en Celcius es: °{c}')

celcius(89)

def esNumero ():
    num = int(input("Ingrese un número: "))
    if(num == 0):
        print(">>Es cero.")
    elif(num > 0):
        print(('>>Es positivo'))
    else:
        print('>>Es negativo')


esNumero()

def esIgualA(num1, num2, num3):
    if( (num1 + num2) == num3):
        print(f'La suma de {num1} y {num2} es igual a {num3}')
    else:
        print(f'La suma de {num1} y {num2} es distinta a {num3}')

esIgualA(4,4,8)
esIgualA(5,2,10)