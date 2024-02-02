
from datetime import date
info = []

def guard():
        
        Run = str(input("Ingrese su Run con solo 8 digito Ej:(19000123): "))
        flag = True
        while flag:
            if len(Run) > 8 or len(Run) < 8  :
                print("Run ingresado no valido!")
                Run = str(input("Ingrese nuevamente su Run con solo 8 digito Ej:(19000123): "))
            else:
                flag = False
                print("RUN Ingresado es correcto")
                
                
        nombre = str(input("Ingrese su Nombre y Apellido: "))
        
        today = date.today()
        print(today)

        Modelo = int(input("Indigue con el numero,el modelo de celular 1.-Samsung S20 2.-Iphone Xpro 3.-Xaomi Lite 20Pro: "))
        flag1 = True
        while flag1:
            if (Modelo) <= 0 or (Modelo) >= 4:
                print("Opcion ingresada de modelo, no es valida!")
                Modelo = int(input("Ingrese nuevamente el modelo de celular 1.-Samsung S20 ,  2.-Iphone Xpro , 3.-Xaomi Lite 20Pro::"))
            elif Modelo == 1:
                tipo = "Samsung S20"
                print(tipo)
                break
            elif Modelo == 2:
                tipo = "Iphone Xpro"
                print(tipo)
                break
            elif Modelo == 3:
                tipo = "Xaomi Lite 20Pro"
                print(tipo)
                break
            else:   
                flag1 = False
                print("Celular Ingresado!!")
               
        Tipo_reparacion = int(input("Ingrese el tipo de repacion: 1.-cambio de pantalla, 2.- cambio de batería, 3.- cambio de cámara "))
        flag2 = True
        while flag2:
            precio_base = 35000
            if (Tipo_reparacion) <= 0 or (Tipo_reparacion) >= 4:
                    print("Opcion ingresada no es valida!")
                    Tipo_reparacion = int(input("Ingrese nuevamente el tipo de repacion: 1.-cambio de pantalla, 2.- cambio de batería, 3.- cambio de cámara "))
            elif Tipo_reparacion == 1:
                pago = precio_base + 85000
                print(pago) 
                break
            elif (Tipo_reparacion) == 2:
                pago = precio_base + 120000
                print(pago)
                break
            elif (Tipo_reparacion) == 3:
                pago = precio_base + 185000   
                print(pago)    
                break
            else:
                flag2 = False

        informacion = [Run,nombre, today, tipo,pago]
        info.append(informacion)
        print("El celular ha sido registrado exitosamente.")


#buscar
def buscar_celular():
    Run = input("Ingrese el Run del cliente: ")
    encontrado = False
    for informacion in info:
        if informacion [0] == Run:
            mostrar_informacion_celular(informacion)
            encontrado = True
            break
    if not encontrado:
        print("Celular no encontrado.")

def mostrar_informacion_celular(informacion):
    print("---- Información del Celular ----")
    print("RUN:", informacion[0])
    print("Nombre:", informacion[1])
    print("Fecha de Ingreso:", informacion[2])
    print("Modelo de Celular:", informacion[3])
    print("Monto a Cancelar:", informacion[4])
    print("----------------------------------")


def imprimir():
    buscar = input("Ingrese el RUN del cliente: ")
    for i in info:
            if i [0] == buscar:
                print("--------  R E P O R T E  D E  Cliente --------\n")
                print("   Run     Nombre    Modelo  Tipo Repacion    Fecha ")
                print("-", i)    
    if not info:
            print("Código de Parte no existe")

def salir(f):
    f = False
    return (f)

flag = True

while flag:
    print("--------- REPARACIONES DE CELULAR ---------")
    print("\t----- Modelos -----")
    print("Samsung S20 --- Iphone Xpro --- Xaomi Lite 20Pro ")
    
    op = int(input("Digite el número de la opción: \n\t1. Ingreso de Informacion \n\t2. Buscar\n\t3. Mostrar\n\t4. Salir\n\t Ingrese un numero: "))
    if op == 1:
        m = guard()
    elif op == 2:
        buscar_celular()
    elif op==3:
        imprimir()
    elif op==4:
        flag = salir(flag)
    else:
        print("Opción fuera de rango")