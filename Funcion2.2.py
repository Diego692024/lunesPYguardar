
# for es iterar, los metodos sirven para reutilizarlos, como si crearamos un codigo o formula que podemos 
# reutilizar, en este ejemplo se agarra el porsentaje de 10 del anterior ejercicio, (porcentaje2)
def porcentaje2 (numero, porsentaje=10): # un valor ya esta definido y el otro no son requeridos 
    resultado = numero * (porsentaje / 100)
    return resultado

def aplicar_porcentaje (lista):
    resultado_pocentaje = []
    for numero in lista: 
        resultado = porcentaje2(numero)
        resultado_pocentaje.append(resultado)
    return resultado_pocentaje

lista_numeros = [50,80,66,45,69]
resultado_pocentaje = aplicar_porcentaje(lista_numeros)
print(resultado_pocentaje)

