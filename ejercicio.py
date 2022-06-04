nombre = input("Ingresar Nombre: ")
apellido = input("Ingresar Apellido: ")
horas = int(input("Ingresar cantidad de horas trabajadas: "))
dias = int(input("Cantidad de Dias trabajados: "))

valor_Uf = 32500
valor_Hora = 9500

isapres = {"mas vida": 2, "colmena":2, "colamena2":2.11, "colmena3": 2.34, "colmena4":2.76, "colmena5":2.78}

desc_fonasa = 0.07
desc_afp = 0.12
desc_AFC = 0.03

def sueldoFinal (horas, dias):

    sueldo_final = (horas * valor_Hora) * dias

    return (print (sueldo_final))

sueldoF = sueldoFinal(horas, dias)

def descuento_Isapre(isapres):
    hola = ""
    va = ""
    for i, v in isapres.items():
        hola = i
        va = v
    
    return va

print (descuento_Isapre(isapres))