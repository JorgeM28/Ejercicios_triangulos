# Determinar si dado tre numeros estos pueden formar un triangulo

print("-------------------------")
print("--------TRIANGULO--------")
print("-------------------------")



#input
while True:


    A=int(input("\nIngrese el dato del lado a: "))
    B=int(input("Ingrese el dato del lado b: "))
    C=int(input("Ingrese el dato del lado c: "))

    #procesing 

    if (A+B)>C and (A+C)>B and (B+C)>A:
        print("\nCon los datos ingresados si se forma un triangulo")
    else:
        print("\nCon los datos ingresados no se forma un triangulo")

#finish