#Ejercicio tipo prueba: Bus
import os,time,msvcrt
from funciones_ejercicio_tipo_prueba import *
os.system('cls')
while True:
    
    print('VENTA DE ASIENTOS EN UN BUS:\n1: Mostrar asientos disponibles\n2: Comprar asiento\n3: Mostrar ventas realizadas\n4: Generar archivo en csv\n5: Salir')
    opc=int(input('Ingrese una de las 4 opciones: '))
    if opc==1:
        pass
    elif opc==2:
        opc2()
    elif opc==3:
        opc3()
    elif opc==4:
        opc4()
    else:
        Salir()

