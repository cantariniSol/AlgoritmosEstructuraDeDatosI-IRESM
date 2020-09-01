import funciones

def menu():

        print("_____________________ MENÚ _______________________")
        print("1. Número mayor a 10.")
        print("2. Suma igual al tercero.")
        print("3. Dividir el cuadrado.")
        print("4. Celcius.")
        print("--------------------------------------------------")
        num = int(input(">>Ingrese la opción que desea realizar: "))

        if (num == 1):
            s = funciones.mayor10() # La funcion mayor10() no retorna ningun valor por lo que no debería ser guardada en la variable s
            return print(str(s)) # Esta linea no debe escribirse
        elif (num == 2):
            n1 = int(input("Ingrese un número: "))
            n2 = int(input("Ingrese otro número: "))
            n3 = int(input("Ingrese un último número: "))
            m = funciones.sumaIgualAlTercero(a=n1, b=n2, c=n3) # La funcion sumaIgualAlTercero no retorna ningun valor por lo que no debería ser guardada en la variable m
            return print(str(m)) # Esta linea no debe escribirse
        elif (num == 3):
            n3 = int(input("Ingrese un número: "))
            n4 = int(input("Ingrese otro número: "))
            j = funciones.dividirCuadrado(num1=n3, num2=n4)
            return print(str(j)) # La palabra reservada return no debe escribirse, lo que se debería imprimir es print(f"El resultado es: {j}")
        elif (num == 4):
            l = funciones.celcius()
            return print(str(f"{l}°")) # La palabra reservada return no debe escribirse



menu()



