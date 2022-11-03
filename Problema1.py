""" Tarea 1
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, autorl y autor(es). Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es) """





biblioteca=list()

class Libro:
    def __init__(self,id,titulo,genero,ISBN,editorial,autor):
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__ISBN=ISBN
        self.__editorial=editorial
        self.__autor=autor

    #Getters
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_genero(self):
        return self.__genero
    def get_ISBN(self):
        return self.__ISBN
    def get_editorial(self):
        return self.__editorial
    def get_autor(self):
        return self.__autor

    #Setters    
    def set_id(self,id):
        self.__id=id
    def set_titulo(self,titulo):
        self.__titulo=titulo
    def set_genero(self,genero):
        self.__genero=genero
    def set_ISBN(self,ISBN):
        self.__ISBN=ISBN
    def set_editorial(self,editorial):
        self.__editorial=editorial
    def set_autor(self,autor):
        self.__autor=autor

    
#Pantalla Inicial
def mostrar_opciones():
    print("Bienvenido a tu biblioteca de confianza\nA continuacion tienes varias opciones las cuales tu puedes tomar a tu criterio\nElige una opcion\nOpción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\nOpción 2: Listar libros.\nOpción 3: Agregar libro.\nOpción 4: Eliminar libro.\nOpción 5: Buscar libro por ISBN o por título.\nSe debe sugerir las opciones y listar el resultado.\nOpción 6: Ordenar libros por título.\nOpción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.\nOpción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.\nOpción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\nOpción 10: Guardar libros en archivo de disco duro (.txt o csv).")

#Opcion 1
def leer_archivos():
    #añadimos los libros a la lista general para que ahi se pueda modificar primero leyendo el archivo y 
    try:
        documento=input("Indique el nombre del archivo(con 3 libros añadidos) para cargarlo a la plataforma ya sea .txt o csv ejemplo 'libro.txt' : ")
        libros = open(documento,"r")
        contenido=libros.read()
        lista=contenido.split("\n")
        for element in lista:
            valor=element.split(",")
            valor[0]=int(valor[0])
            biblioteca.append(valor)
        print(biblioteca)
    except Exception as ex :
        print(f"El archivo esta dañado o no se encuentra {type(ex)}")

    else:
        print("Los archivo han sido cargados correctamente")


     
#Opcion 2
def listar_libros():
    print("Id,Título, Género, ISBN, Editorial y Autor(es)")
    for lista in biblioteca:
        print("")
        for element in lista:
            print(element,end=",")
            

#Opcion 3
def agregar_libros():
    lista=[]
    id=len(biblioteca)+1
    titulo=input("Indique el titulo del libro a agregar : ").title()
    genero=input("Indique el genero del libro a agregar : ").title()
    ISBN=input("Indique el ISBN del libro a agregar : ").title()
    editorial=input("Indique la editorial del libro a agregar : ").title()
    autor=input("Indique el autor del libro a agregar(Si el libro tiene mas de un autor separelo por comas ejm:ulises,homero) : ").title().split(",")
    
    libro=Libro(id,titulo,genero,ISBN,editorial,autor)  
 
    lista.append(libro.get_id())
    lista.append(libro.get_titulo())
    lista.append(libro.get_genero())
    lista.append(libro.get_ISBN())
    lista.append(libro.get_editorial())
    lista.append(libro.get_autor())
    print(lista)
    biblioteca.append(lista)
    print("Libro Agregado correctamente")
    print(biblioteca)

#Opcion 4: Eliminar libro
def eliminar_libros():
    listar_libros()
    numero=int(input("Indique el valor a eliminar : "))
    for element in biblioteca:
        if numero in element :
            biblioteca.remove(element)

    for element in biblioteca:
        element[0]=biblioteca.index(element)+1

#Opcion 5 : Buscar libro por ISBN O titulo 

def buscar_libros1():
    opcion=int(input("1.Busqueda por ISBN\n2.Busqueda por titulo\nIndique la opcion : "))
    if opcion==1:
        isbn=input("Indique el codigo de isbn a buscar (ejemplo:'934-212-45324-2-3')   : ").title()
        for element in biblioteca:
            if isbn in element:
                print(element)
    elif opcion==2:
        titulo=input("Indique el nombre del titulo de la obra (ejemplo:'Trilce')   : ").title()
        for element in biblioteca:
            if titulo in element:
                print(element)

#Opcion 6 : Ordenar libros por titulo
def ordenar_libros():
    lista_autores=[]
    lista_ordenada=[]
    for element in biblioteca:
        lista_autores.append(element[1])

    lista_autores.sort()
    print(lista_autores)

    for elemento in lista_autores:
        for element in biblioteca:
            if elemento in element:
                lista_ordenada.append(element)

    for element in lista_ordenada:
            element[0]=lista_ordenada.index(element)+1

    for lista in lista_ordenada:
        print("")
        for element in lista:
            print(element,end=",")


#Opcion 7: Buscar libro por autor editoria o genero 

def buscar_libros2():
    opcion=int(input("1.Busqueda por autor\n2.Busqueda por editorial\n3.Busqueda por genero\nIndique la opcion : "))
    if opcion==1:
        autor=input("Indique el nombre del autor a buscar (ejemplo:'Franz Kafka')   : ").title()
        for element in biblioteca:
            if str(element).find(autor)>0:
                print(str(element).replace("[","",1).replace("]","",1))
    elif opcion==2:
        editorial=input("Indique el nombre del editorial de la obra (ejemplo:'Heraldos Negros')   : ").title()
        for element in biblioteca:
            if editorial in element:
                print(element)
    elif opcion==3:
        genero=input("Indique el nombre del genero de la obra (ejemplo:'Heraldos Negros')   : ").title()
        for element in biblioteca:
            if genero in element:
                print(element)

#Opcion 8 : Buscar libros por numero de autores 

def buscar_libros3():
    autores=int(input("Ingresar una cantidad de autores para ver cuantos libros tienen esa cantidad de autores ingresadas: "))
    for element in biblioteca:
        print("")
        for elemento in element:
            if len(element[5])==autores:
                print(elemento,end=",")

#Opcion 9 : Editar o actualizar datos de un libro(titulo,genero,ISBN,editorial y autores)
def editar_libros():
    listar_libros()
    numero=int(input("Indique que numero de libro desea editar : "))

    for element in biblioteca:
            if numero in element :
                biblioteca.remove(element)

    lista_autores=[]
    val=input("Agregue el nuevo titulo : ").title()
    val2=input("Agregue el nuevo genero : ").title()
    val3=input("Agregue el nuevo ISBN : ").title()
    val4=input("Agregue el nuevo editorial : ").title()
    
    opcion=int(input("Indique si el libro que va a editar cuantos autores tiene : " ))

    for i in range(opcion):
        valor=input(f"Indique el {i+1} autor : ")
        lista_autores.append(valor) 

    lista=[]
    lista.append(numero)
    lista.append(val)
    lista.append(val2)
    lista.append(val3)
    lista.append(val4)
    lista.append(lista_autores)

    biblioteca.append(lista)
    biblioteca.sort()

    for element in biblioteca:
        element[0]=biblioteca.index(element)+1

    print(biblioteca)


#Opcion 10 : Guardar libros en archivo de disco duro
def guardar_libros():
    nombre= input("Indicar el nombre del archivo para guardarlo en la computadora con extension csv o txt (ejemplo : 'biblioteca.txt') : ")
    archivo= open(nombre,"w")
    for lista in biblioteca:
        archivo.write("\n")
        for element in lista:
            archivo.write(str(element)+",")


# leer_archivos()
# listar_libros()
# agregar_libros()
# eliminar_libros()
# buscar_libros()
# ordenar_libros()
# buscar_libros2()
# buscar_libros3()
# editar_libros()
# guardar_libros()
