import os,time,msvcrt
import csv
#FUNCIONES PINCIPAL: 

bus=[['O' for x in range(4)] for y in range (7)] #-> [O,O,O,O,O]
pasaje=5000
ventas=[]

def mostrar_asientos():
    cont=1
    print('\tMostrar asientos: ')
    print('   1 2 3 4')
    print('    ______')
    for fila in bus:
        print(cont,'| ',end=' ')
        for asiento in fila:
            print(asiento, end=" ")
        print(' |')
        cont += 1
    print('  |___________|')      
def comprar_asientos():
    hay_asiento =False
    for fila in bus:
        for asiento in fila:
            if asiento=="O":
                hay_asiento=True
                break
    if hay_asiento == False:
        print('No hay asiento disponibles')
        return
    print('\tComprar asientos: ')
    nombre=validar_nom()
    edad=validar_edad()
    telefono=validar_telefono()
    print('...Ahora selecione su asiento ')
    time.sleep(2)
    while True:
        os.system('cls')
        mostrar_asientos()
        fila=validar_numero("fila",[1,2,3,4,5,6,7])
        columna=validar_numero('columna',[1,2,3,4])
        if bus[fila-1][columna-1]=="O":
            es_estudiante=validar_estudiante()
            if es_estudiante =='S' and edad >=18:
                pagar = pasaje * 0.8
            elif edad>=65:
                pagar=pasaje*0.85
            else:
                pagar=pasaje     

            bus[fila-1][columna-1] ="X"
            venta=[nombre,edad,telefono,fila,columna,pagar]
            ventas.append(venta)
            print('ASIENTO COMPRADO...')
            break
        else:
            print('Lo siento, el asiento esta ocupado')
            time.sleep(1)
def mostrar_ventas():
    print('\tMostrar ventas')
    if not ventas:
        print('NO existen ventas.')
    else:
        acum = 0
        print('\tVentas')
        for v in ventas:
            print(f'Nombre: {v[0]}, Edad: {v[1]}, Número telefonico: {v[2]},Fila: {v[3]}, Columnas: {v[4]}, Venta: ${v[5]}')
            acum += v[5]
        print('Total de las ventas: $',acum)    
def exportar_csv():
    print('\tExportar csv: ')
    if not ventas:
        print('NO hay ventas..')
    else:
        nombre_archivo=input('Ingrese nombre de el archivo')+'.csv'
        with open(nombre_archivo,'w',newline=' ') as archivo:
            escritor=csv.writer(archivo)
            escritor.writerows(ventas)
                
def salir():
    print('ADIOS, GRACIAS POR COMPRAR...')
    exit()







#FUNCIONES DE AYUDA:
def menu():
    os.system('cls')
    print('\tMenu\nMostrar asientos\nComprar asientos\nMostrar ventas realizadas\nExportar cvs\nSalir. ')
    opc=input('Ingrese una opcion: ')
    os.system('cls')
    return opc
def presionar_tecla():
    print('\nPresione una tecla para continuar')
    msvcrt.getch()
def validar_nom():
    while True:
        nom=input('Ingrese nombre: ')
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print('ERROR, debe tener al menos 3 caracteres')
def validar_edad():
    while True:
        try:
            edad=int(input('Ingrese su edad: '))
            if edad>=10 and edad<=120:
                return edad
            else:
                print('ERROR, la edad debe estar entre 10 y 120 años')
        except:
            print('ERROR, debe ser un número entero.')
def validar_telefono():
    try:
        tel=int(input('Ingrese su Número telefonico: '))
        if len(str(tel))==9 and str(tel)[0]==9:
            return tel
        else:
            print('ERROR')
    except:print('Debe ser un número entero')
def validar_numero(p_palabra,p_opciones):
    try:
        num=int(input(f'Ingrese {p_palabra}: '))
        if num in p_opciones:
            return num
        else:
            print(f'ERROR, {p_palabra.upper()} DEBE ESTAR ENTRE 1 Y {p_opciones[-1]}')        
    except:
        print('ERROR, debe ser un número entero..')        
def validar_estudiante():
    while True:
        es_estudiante=input('Indique si es estudiante(S:si, N:no): ')
        if es_estudiante.upper() in('S','N'):
            return es_estudiante.upper()
        else:
            print('ERROR, Ingrese S o N')

