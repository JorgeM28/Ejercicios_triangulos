# Determinar si un triangulo optuso, recto o agudo 

print("--------------------------------------------")
print("--------DEFINIR-EL-TIPO-DE-TRIANGULO--------")
print("--------------------------------------------")


#input

A=int(input("\nIngrese el dato del lado a: "))
B=int(input("Ingrese el dato del lado b: "))
C=int(input("Ingrese el dato del lado c: "))

#procesing

if (A+B)>C and (A+C)>B and (B+C)>A:

    if A==B==C:
        print("Los datos ingresados forman un triangulo equilatero")
    elif A==B!=C or B==C!=A or C==A!=B:
        print("Los datos ingresados forman un triangulo isoceles ")
    elif A!=B!=C:
        print("Los datos ingresados forman un triangulo escaleno")
else:
    print("Los datos ingresados no forman ninguno de los 3 tipos de triangulo ")

#finish