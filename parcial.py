print("Realizado por Andres Piratova, Claudia Moreno, Jonathan Ortega & Walter Cuprita")
agenda = {"Diana Flores": ["3002221144", "Diana.flores@hotmail.com"],"Diana": ["3002221145", "Diana@hotmail.com"]}

menu =  """
    ***********************
        V. Ver contactos
        N. Nuevo contacto
        B. Buscar contacto
        M. Modificar contacto
        S. Salir del programa
    ***********************
    """

menuModificar =  """
    ***********************
        n. Modificar Nombre
        t. Modificar Telefono
        c. Modificar Correo
        a. Abandonar Modificacion
    ***********************
    """

def Agregar(n,t,c):
    agenda[n] = [t, c]

def Buscar(n):
    if(n in agenda):
        return (agenda[n])
    else:
        return "No existe el contacto telefónico"

def Modificar(n,t,c):
    a=1

ejecutando = True
while ejecutando == True:
    print(menu)
    letraCapturada = str(input("Digite una opción: ")).lower()
    if (letraCapturada == "v" or letraCapturada == "n" or letraCapturada == "b" or letraCapturada == "m" or letraCapturada == "s"):
        if (letraCapturada == "v"):
            print(agenda)
        if (letraCapturada == "n"):
            nombre = str(input("Ingrese el nombre: "))
            telefono = str(input("Ingrese el numero: "))
            preguntando = True
            while preguntando == True:
                pregunta = str(input("¿Desea agregar email [Si] o [No]?  ")).lower()
                if (pregunta == "si" ):
                    correo = str(input("Digite el email: "))
                    preguntando = False
                if (pregunta == "no"):
                    correo = "No agrego email"
                    preguntando = False
            Agregar(nombre,telefono,correo)
        if (letraCapturada == "b"):
            Bnombre = str(input("Ingrese el nombre a buscar: "))
            print(Buscar(Bnombre))
        if (letraCapturada == "m"):
            while True:
                Bnombre = str(input("Ingrese el nombre a buscar: "))
                print(Buscar(Bnombre))
                if(Bnombre in agenda):
                    print(menuModificar)
                    tempTelefono = (agenda[Bnombre][0])
                    TempCorreo = (agenda[Bnombre][1])
                    while True:
                        letraCapturada = str(input("Digite una opción: ")).lower()
                        if (letraCapturada == "n"):
                            nuevoNombre = str(input("Digite un nuevo nombre: "))
                            agenda[nuevoNombre] = agenda.pop(Bnombre)
                            print(menuModificar)
                        if (letraCapturada == "t"):
                            nuevoTelefono = str(input("Digite un nuevo telefono: "))
                            agenda[Bnombre][0] = nuevoTelefono
                            print(menuModificar)
                        if (letraCapturada == "c"):
                            nuevoCorreo = str(input("Digite un nuevo correo: "))
                            agenda[Bnombre][1] = nuevoCorreo
                            print(menuModificar)
                        if (letraCapturada == "a"):
                            break
                else:
                    break            
        if (letraCapturada == "s"):
            ejecutando = False

