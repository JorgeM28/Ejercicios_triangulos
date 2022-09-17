# Determinar si un triangulo optuso, recto o agudo 

print("--------------------------------------------")
print("--------DEFINIR-EL-TIPO-DE-TRIANGULO--------")
print("--------------------------------------------")


#input
print("Ingresa tus datos donde c es el lado mayor")
A=int(input("\nIngrese el dato del lado a: "))
B=int(input("Ingrese el dato del lado b: "))
C=int(input("Ingrese el dato del lado c: "))

#procesing 

if (A+B)>C and (A+C)>B and (B+C)>A:

    if C**2 < A**2 + B**2:
        print("Los datos ingresados forman un triangulo agudo")
    elif C**2 == A**2 + B**2:
        print("Los datos ingresados forman un triangulo recto")
    elif C**2 > A**2 + B**2:
        print("Los datos ingresados forman un triangulo obtuso")
    else:
        print("Los datos ingresados no forman ninguno de los 3 tipos de triangulo")
else:
    print("Los datos ingresados no forman un triangulo")
    