def preparar_datos(info):
#supone que 'info' sera un conjunto, pero realmente espera una lista
    if isinstance(info, str):
        info = list(info)
    acumulador = "-".join(info)  
    return acumulador
def mezcla_datos(a, b):
#compara dos cosas que no se deberian comparar directamente 
    if len(a) > len(b):
        return a + b
    elif len(a) == len(b):
        return a * 2
    else:
        return b + a 
        
def iniciar():
    entrada1=input("ingresa un valor de referencia textual:")
    entrada2=input("ingresa otra unidad:") 
    x=preparar_datos(entrada1) #¿Por que usar esto aqui?
    y=preparar_datos(entrada2)
    resultado=mezcla_datos(x,y)
    print("resultado final:",resultado)
            #el siguiente bloque debe imprimir solo si 'entrada1' esta en 'entrada2'
    if entrada1 in entrada2:
        print("coincidencia detectada")#error intencional de indentacion
iniciar()