#Funciones.
import os,time,msvcrt
import csv

pasajeros=[]

valor_normal=7000
valor_descuento = 0
def opcion1():
    print('Asientos disponibles: ')
    bus=[['O' for f in range(4)] for c in range(6)]
    for f in bus:
        print(bus)
    
    
         
def opc2():
    print('Comprar boletos: ')
    print('Bienvenido, el valor de entrada normal es de 7000 pesos, los estudiantes menores de 18 años tienen un descuento de el 20%, y los adultos mayores de 65 años un 15% ')
    nombre=validacion_nombre()
    edad=int(input('Ingrese su edad: '))
    valor_de_descuento=descuentos(edad)
    telefono=int(input('Ingrese su numero telefonico(sin el +56): '))
    pasajero= [nombre,edad,telefono,valor_de_descuento]
    pasajeros.append(pasajero)
    time.sleep(1)
    print('Cliente añadido con exito....')
def opc3():
    print('Mostrar las ventas realizadas: ')
    if len(pasajeros)==0:
        print('No llevas ninguna venta realizada, Ve a la opcion numero 2 primero..')
    else:
        for p in pasajeros:
            os.system('cls')
            print(f'Nombre: {p[0]}\n Edad: {p[1]}\nNúmero de telefóno: {p[2]}\nValor pagado es: ${p[3]}') 
            print('Ingresa una tecla para continuar...')
            msvcrt.getch()
def opc4():
    print('Imprimir en csv: ')
    if len(pasajeros)==0:
         print('No llevas ninguna venta realizada, Ve a la opcion numero 2 primero..')
    else:
         with open('ventas.csv','w',newline='') as archivo:
                escritor=csv.writer(archivo)
                escritor.writerow(pasajeros)
                     
                     
def Salir():
        print('Adios..')
        exit() 
def validacion_nombre():
    while True:
        nom=(input('Ingresa el nombre: ')).capitalize()
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print('Ingrese almenos de 3 caracteres y solo letras...')
            
def descuentos(p_edad):
    valor_descuento=0
    valor_normal=7000
    if p_edad <=18:
         valor_descuento== valor_normal*0.20
         return valor_descuento
    elif p_edad <=65:
         valor_descuento==valor_normal*0.15
         return valor_descuento
    else:
         valor_descuento=valor_normal
         return valor_descuento


