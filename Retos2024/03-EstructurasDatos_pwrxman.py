"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""


print("===========  L I S T A S      =========")
"""
Lists are used to store multiple items in a single variable.
Lists are created using square brackets or It is also possible to use the list() constructor when creating a new list.
List items can be of any data type.
List items are ordered.  it means that the items have a defined order, and that order will not change.
    If you add new items to a list, the new items will be placed at the end of the list.
List allow duplicate values.
List items are changeable, meaning that we can change, add, and remove items in a list after it has been created.
List items are indexed, the first item has index [0], the second item has index [1] etc.
Lists are defined as objects with the data type 'list': <class 'list'>

"""
# Creando LISTA Usando Brackets
my_list: list = ["Brais", "Black", 4 , True, 3.1416, ["a", "b", "c", "d"]]   

# Creando LISTA Using the list() constructor to make a List:
thislist = list(("xerox", "tomas", "apple", "banana", "cherry")) # note the double round-brackets
print(thislist)                    
print(my_list)

empty_list = list() # this is an empty list, no item in the list

my_list.append("Castor")  # Inserción
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso al segundo elemento, recuerda que empieza en cero
my_list[1] = "Cuervillo"  # Actualización
print(my_list)

thislist.sort()
print(thislist)

lst = ['item1','item2','item3', 'item4', 'item5']
f_item, s_item, t_item, *rest = lst  # Hace un emparejamiento de cada nombre de estos con el correspondiente elemento de la lista
                        # El *rest crea una lista con los elementos restantes 
print(f_item)     # item1
print(t_item)    # item2
print(s_item)     # item3
print(rest)           # ['item4', 'item5']

print(type(my_list))


print("===========  T U P L E      =========")
"""
Tuples are used to store multiple items in a single variable.
Tuples are created using round brackets or It is also possible to use the tuple() constructor to make a tuple.
Tuple items can be of any data type.
Tuple items are ordered.  it means that the items have a defined order, and that order will not change.
Tuples are unchangeable (or immutable), meaning that we cannot change, add or remove items after the tuple has been created.
Tuple Allows duplicate members.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Tuples are defined as objects with the data type 'tuple': <class 'tuple'> 

"""
# Creando TUPLE con parentesis
my_tuple: tuple = ("Andrei", "Med", "@amed", "66")
print(my_tuple)

# Creando TUPLE usando el constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))


print("===========  S E T      =========")
"""
Sets are used to store multiple items in a single variable.
Sets are created using curly brackets {},or It is also possible to use the set() constructor to make a set.
Set items can be of any data type.
Set is a an unordered collection, means that the items in a set do not have a defined order.
Set is an unchangeable* collection, meaning that we cannot change the items after the set has been created,
        but you can remove items and add new items.
Set is an unindexed collection
Sets cannot have two items with the same value, meaning duplicate items are not allowed
Sets are defined as objects with the data type 'set' <class 'set'> 
"""

# Creando un SET usando llaves {}
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)

# Creando un SET usando e constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 


my_set.add("mouredev@gmail.com")  # Inserción
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))


print("===========  D I C T I O N A R Y      =========")
"""
Dictionaries are used to store data values in key:value pairs. 
Dictionary items can be of any data type.
Dictionaries are created using curly brackets, and have keys and values or It is also possible to use the dict() constructor.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Dictionary is a collection which is ordered a partir de la version 3.7, it means that the items have a defined order, and that order will not change.
Dictionary is a collection changeable, meaning that we can change, add or remove items after the dictionary has been created. 
Dictionary is a collection that do not allow duplicates, it means cannot have two items with the same key.
Dictionary can contain dictionaries, this is called nested dictionaries.
Dictionaries are defined as objects with the data type 'dict'<class 'dict'> 

"""

# Creando un Diccionario usando {}
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
print(my_dict)

# Creating a Dictionary Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))


# Diccionario anidado
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(child1)
print(child2)
print(child3)
print(myfamily)


"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

global agenda
agenda = {}
global key
key = dict()

def searching():
    print("\nBuscando contactoF")
    nombre = input("Dime el nombre a Buscar: ")
    # key["name"] = nombre
    if nombre in agenda.keys():
        print(f"Encontre el nombre {nombre} solicitado y su teléfono es {agenda[nombre]}\n")
      
    else:
        print(f"No existe el contacto {nombre}\n")    


def adding():
    print("\nAñadiendo contactoF")
    nombre = input("Dime el nombre del nuevo contacto: ")
    # print(f"============>  nombre = {nombre}")
    if nombre in agenda.keys():
        #x = agenda.get('"' + nombre + '"')
        #print(f"Ya existe un contacto con el nombre -> {nombre} y telefono {x}\n\n")
        print(f"Ya existe un contacto con el nombre -> {nombre} y telefono {agenda[nombre]}\n\n")
              
    else:
        # print(f"Nombre no Duplicado  ============>  nombre = {nombre}")
        tel = input("Introduce el número telefónico del contacto: ")
        if tel.isdigit() and len(tel) > 0 and len(tel) <= 11:
            # print(f"Variable nombre ->    {nombre}")
            # lstname: list = [nombre]
            # print(lstname)
            # lsttel = [tel]
            # print(lsttel)
            # newcontact = dict(zip(lstname, lsttel))
            # print(newcontact)
            # agenda.update(newcontact)
            # print(f"Se añadió nuevo contacto nombre: {nombre} y telefono {lsttel[0]}\n\n")  
            agenda[nombre] = tel
            print(f"Se añadió nuevo contacto nombre: {nombre} y telefono {agenda[nombre]}\n\n")

        else:
            print("Debes introducir un teléfono solo con números y un máximo de 11 dígitos.\n\n")   

def updating():
    print("Modificar contactoF")
    nombre = input("Dime el nombre del contacto que deseas actualizar: ")
    if nombre in agenda.keys():
        x = agenda.get(nombre)
        tel = input("Dime el nuevo telefono  para este contacto: ")
        agenda[nombre] = tel
        print(f"Se actualizó el contacto {nombre} con el telefono {agenda[nombre]}\n\n")
    else:
        print(f"No existe el contacto {nombre}\n")

def deleting():
    print("Eliminando contactoF")      
    nombre = input("Dime el nombre del contacto que deseas eliminar: ")
    if nombre in agenda.keys():
        agenda.pop(nombre)
        print(f"Se eliminó el contacto {nombre}")
    else:
        print(f"No existe el contacto {nombre}\n")

def my_agenda():

    operacion = "0"
    
    while operacion != "5": 
        print("1. Buscar Contacto")
        print("2. Añadir Nuevo Contacto")
        print("3. Modificar Contacto")
        print("4. Eliminar Contacto")
        print("p. Genrra Lista de Contactos")
        print("5. Terminar")

        operacion = input("Seleccione la operación deseada: ")

        match operacion:
          case "1":
              searching()
          
          case "2":
              adding()
          
          case "3":
              updating()

          case "4":
              deleting()
          
          case "p":
              for x, y in agenda.items():
                  print(x, y) 

          case "5":
            print("Terminar")  
            break

          case _:
            print("Opcion seleccionada NO válida.")               

my_agenda()

