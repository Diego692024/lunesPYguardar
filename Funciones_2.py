#numero = input("introduce tu numero: ")
#porcentaje = input("introduce tu %: ")

def porcentaje (numero, porsentaje): # los dos valores son requeridos
    resultado = numero * (porsentaje / 100)
    return resultado
resultado = porcentaje(numero=80, porsentaje=10)
print (resultado)
##################################################################################################
def porcentaje2 (numero, porsentaje=10): # un valor ya esta definido y el otro no son requeridos 
    resultado = numero * (porsentaje / 100)
    return resultado


resultado = porcentaje2(numero=80)
print(resultado)
resultado = porcentaje2(numero=80, porsentaje=25)
print(resultado)


print(type(porcentaje2))  
#funcio esto 

# funcion regresa algo  
# metodo no regresa nada= solo imprime

