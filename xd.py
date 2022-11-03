
from matplotlib.dates import julian2num
from numpy import append


list=[[1," hola","pero",["juan","sera"]],[2,"sd","pol",["pepe","raul","sene"]],[3,"dfp"," per",["caro","xiomi","te"]],[4,"sad","odf",["karen","saru"]]]

numero=int(input("Indique que numero de libro desea editar : "))

for element in list:
        if numero in element :
            list.remove(element)

lista_autores=[]
val=input("Agregue el primer valoe : ")
val2=input("Agregue el segundo valoe : ")
opcion=int(input("Indique si el autor que va a editar cuantos autores tiene : " ))

for i in range(opcion):
    valor=input(f"Indique el {i+1} autor : ")
    lista_autores.append(valor) 

lista=[]
lista.append(numero)
lista.append(val)
lista.append(val2)
lista.append(lista_autores)

list.append(lista)
list.sort()

for element in list:
    element[0]=list.index(element)+1

print(list)

# for element in list:
#     if str(element).find(l)>0:
#             print(str(element).replace("[","",1).replace("]","",1))

# numero=int(input("Indique la cantidad de valores de autores : "))

# for element in list:
#     print("")
#     for elemento in element:
#         if len(element[3])==numero:
#             print(elemento,end=",")



# lista=['aea','csdf','b3fsdf','2','5','dsdfsdf']

# lista_ordenada=sorted(lista)
# print(lista)
# print(lista_ordenada)
# lista_autores=[]
# lista_ordenada=[]
# for element in list:
#     lista_autores.append(element[1])

# lista_autores.sort()
# print(lista_autores)

# for elemento in lista_autores:
#     for element in list:
#         if elemento in element:
#             lista_ordenada.append(element)

# for element in lista_ordenada:
#         element[0]=lista_ordenada.index(element)+1

# print(lista_ordenada)

# for lista in list:
#     if "sd" in lista:
#         print(lista)

# numero=int(input("Indique el valor a eliminar : "))

# for element in list:
#     if numero in element :
#         list.remove(element)

# for element in list:
#     element[0]=list.index(element)+1

    
# print(list)

