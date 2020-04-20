#estructura de control permite modificar el flujo del algoritmo 

algo = 2
if(algo == 1 ):
    print("es igual a 1")
else:
    print("no es igual a 1")

#ciclos while

numeroDeTragos  =  5
cuantasLlevo     =   0

while cuantasLlevo  <  numeroDeTragos:
    cuantasLlevo = cuantasLlevo +1
    print("se toma " + str(cuantasLlevo) )
    

#Listas

miLista = ["perro","gato","caballo"]
# agregar elementos 
miLista.append("pato")
# Eliminar un elemento
miLista.remove("perro")
# agregar una lista 
miLista.extend(["mico", "elefante", "leon"])
#agregar un elemento el posicion que queremos
miLista.insert(0,"tortuga")
for animal in [miLista]:
    print(animal)

#Dixxionario
#Puede tener un elemento cla y un valor
MiDiccionario = {"nombre":"alejandro", "apellido":"ramirez", "edad": "24"}
#agregar un elemento al diccionario de datos
MiDiccionario.update({"nacionalidad": "Colombiano"})
#amacenar en las claves 
clave = MiDiccionario.keys()
# optener los valores
valor = MiDiccionario.values()
#logintid diccionario
cantidadElementos = MiDiccionario.items()

#realizar el recorrido de la clave en este caso el primer valor

for clave, valor in cantidadElementos:
    print(clave + ":" + valor)