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
            s = funciones.mayor10()
            return print(str(s))
        elif (num == 2):
            n1 = int(input("Ingrese un número: "))
            n2 = int(input("Ingrese otro número: "))
            n3 = int(input("Ingrese un último número: "))
            m = funciones.sumaIgualAlTercero(a=n1, b=n2, c=n3)
            return print(str(m))
        elif (num == 3):
            n3 = int(input("Ingrese un número: "))
            n4 = int(input("Ingrese otro número: "))
            j = funciones.dividirCuadrado(num1=n3, num2=n4)
            return print(str(j))
        elif (num == 4):
            l = funciones.celcius()
            return print(str(f"{l}°"))



menu()



