print (" Calculadora con condicional")

numero1 = float(input("Digite un numero:"))
numero2 = float (input("Digite un numero:"))
operacion = input ("Digite la operacion: ")

if operacion == 's':
    suma = numero1+numero2
    print(f"\nLa suma es: {suma}")

elif operacion == 'R':
    resta= numero1-numero2
    print(f"\nLa resta es: {resta}")

elif operacion == 'M':
    multiplicacion = numero1*numero2
    print(f"\nLa multiplicacion es: {multiplicacion}")
elif operacion== 'D' :
    div = numero1/numero2
    print(f"\nLa divion es: {divion}")

else:
    print("\nSe equivoco de operacion")
    
 
