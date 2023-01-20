import math

peso= float(input("Ingrese su peso (en kg): "))
estatura = float(input("Ingrese su estatura (en metros): "))

IMC = peso / (estatura**2)

print("Tu indice de masa corporal es: ""{0:.2f}".format(IMC))
