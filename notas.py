a=5
print(a) #Imprime valor
print(type(a)) #Imprime el tipo de variable
print(id(a)) #Imprime el identificador de la variable
a=6
print(a)#Imprime valor
print(type(a)) #Imprime el tipo de variable
print(id(a)) #Imprime el identificador de la variable

lista = ["a","b","c"] #Después de creadas sí se pueden modificar
#lista[0]="z" cambiar la primera posición que es a por z
print(lista)

tupla = ("a", "b", "c") #Después de creadas NO se pueden modificar
#tupla[0]="z" No lo va a permitir porque no se pueden modificar luego de ser creadas
print(tupla)

#Añadir algo a mi lista
lista.append("x")
lista.append("y")
lista.append("z")
print(lista)



