from neurana_1 import Neurona
from grafos_logicos import grafo_de_sentencia_logica


if __name__ == '__main__':
    grafo = {}
    while not grafo:
        sentencia_logica = input("Ingrese que sentencia quiere que la neurona aprenda 'and' o 'or': ")
        grafo = grafo_de_sentencia_logica(sentencia_logica)
        if not grafo:
            print("vuelve a intentarlo")
    cant = int(input("Ingrese la cantidad de veces que la neurona debe aprender: "))
    neurona = Neurona()
    neurona.entrenamiento(grafo, cant)
    print("La neurona se entreno con exito")
    print("Ahora vamos a operar con ella")
    cant = int(input("Cuantos calculos quiere hacer: "))
    for i in range(cant):
        a = int(input("Ingrese valor a: "))
        b = int(input("Ingrese valor b: "))
        resultado = neurona.operar(a, b)
        print(f"El resultado es: {resultado}")
