#ejercicio bus

from funciones import *

while True:
    opc=menu()
    if opc=='1':
        mostrar_asientos()
    elif opc=='2':
        comprar_asientos()
    elif opc=='3':
        mostrar_ventas()
    elif opc=='4':
        exportar_csv()
    elif opc=='5':
        salir()
    else:
        print('OPCION INCORRECTA..')
    presionar_tecla()
