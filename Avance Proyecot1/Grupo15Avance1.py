#Usuario 1 es: Cliente1 y su contraseña es: 1205
#Usuario 2 es: Cliente2 y su contraseña es: 7777
User1 = "Cliente1"
User2 = "Cliente2"
Contra1 = 1205
Contra2 = 7777
usuario = (input("Digite su usuario: "))
Password = int(input("Digite su contraseña: "))

if (User1 == usuario and Contra1 == Password) or (User2 == usuario and Contra2 == Password):
    print ("Usted ingrsó correctamente")
    #aporte de Cristopher alvarez Chavarría
    print("Registros Médicos")
    Nombre = ""
    Nombre= input("digite su Nombre:")
    Codigo = ""
    Codigo= input("digite su Codigo:")
    Telefono = ""
    Telefono= input("digite su Telefono:")
    Correo = ""
    Correo= input("digite su Correo:")
    Disponibilidad = ""
    Disponibilidad = input("¿Cual es su disponibilidad de horario de Lunes a Viernes en mañanas o tardes y fines de semana?")
    # aporte de Axel
    print("Datos del dueño")
    nombre_completo=(input("1.Digite Su nombre completo:")) 
    cedula=int(input("2.Digite su cedula:"))
    celular=int(input("3.Digite cecular:"))
    correo_electronico=str(input("4.Correo electronico:"))
    dirreccion=str(input("5.Digite su dirrecion"))
    #Aporte Esteban Cerdas
    print("Datos de la mascota")
    Nombre_Mascota = input("Ingrese el nombre de su mascota: ")
    Raza = input("Ingrese la raza: ")
    Fecha_Nacimiento = input("Ingrese la fecha de nacimiento de su mascota: ")
    Sexo = input("Ingrese el sexo de su mascota: ")
    Peso = input("Ingrese el peso de su mascota: ")
    Caracteristias = input("Ingrese característicos de su macota: ")
    Alimento = input("Ingrese el alimento que consume su mascota ")
    Observaciones = input("Ingrese observaciones generales que haya visto en su mascota: ")
    print(" Muchas gracias por brindar sus datos.")
    print(" Le atenderemos pronto!!!")
    
    #****Avance 2 ****
    #Aporte Esteban
    #modulo clínico

    
    def Cita():
        turno = input("¿Qué turno desea? (MAÑANA, TARDE o FIN DE SEMANA): ")
        horario = ""
        if turno == "MAÑANA":
            print("Los horarios para mañana son:")
            print("1. 9 AM")
            print("2. 10 AM")
            print("3. 11 AM")
            horario = input("Digite la hora que desea para su cita: ")
        elif turno == "TARDE":
            print("Los horarios para tarde son:")
            print("1. 1 PM")
            print("2. 2 PM")
            print("3. 3 PM")
            horario = input("Digite la hora que desea para su cita: ")
        elif turno == "FIN DE SEMANA":
            print("Los horarios para fin de semana son:")
            print("1. 9 AM")
            print("2. 10 AM")
            print("3. 11 AM")
            horario = input("Digite la hora que desea para su cita: ")
    
        return turno, horario
        


    def vacunas (turno, horario, seleccionVacunas):
        print("**Vacunación**")
        print("== Opciones de vacunas ==")
        print("1. Polivalente")
        print("2.Gripe")
        print("3.Giardia")
        print("4.Antirábica")
        seleccionVacunas =input("Ingrese la vacuna que desea aplicar: ")
        if seleccionVacunas == "Polivalente":
            print("Vacuna Polivalete")
            print("Cantidada de dosis: "+ str(dosis_Polivalente))
            print("La aplicación de la vacuna es cada "+ str(aplicacion_Polivalente) +"días y una dosis anual")
            print("Día de aplicación: "+ Disponibilidad)
            print("Turno: " + turno)
            print("Hora: " + horario)

        elif seleccionVacunas == "Gripe":
            print("Vacuna de Gripe")
            print("Cantidada de dosis: "+ str(dosis_Gripe))
            print("La aplicación de la vacuna es a los 87 días de nacido y una dosis anual")
            aplicacion_Gripe = input("Vienes por dosis anual? (Si o No): ")
            if aplicacion_Gripe == "SI":
                print("Día de aplicación: "+ Disponibilidad )
                print("Turno: " + turno)
                print("Hora: " + horario)
            else:
                print("Pronto le atenderemos!")

        elif seleccionVacunas == "Giardia":
            print("Vacuna Giardia")
            print("Cantidada de dosis: "+ str(dosis_Giardia))
            print("La aplicación de la vacuna es cada "+ str(aplicacion_Giardia) +"días y una dosis anual")
            print("Día de aplicación: "+ Disponibilidad)
            print("Turno: " + turno)
            print("Hora: " + horario)

        elif seleccionVacunas == "Antirábica" :
            print("Vacuna de Antirábica")
            print("Cantidada de dosis: "+ str(dosis_Antirabica))
            print("La aplicación de la vacuna es a los 129 días de nacido y una dosis anual")
            aplicacion_Gripe = input("Vienes por dosis anual? (SI o NO): ")
            if aplicacion_Antirabica == "SI":
                print("Día de aplicación: "+ Disponibilidad)
                print("Turno: " + turno)
                print("Hora: " + horario)
            else:
                print("Pronto le atenderemos!")

        return turno, horario, seleccionVacunas


    def cancelacion (turno, horario, seleccionVacunas):
        if turno == "MAÑANA":
            print("== Cancelación de cita ==")
            print(" **Cita de: " + Nombre_Mascota)
            print("Dueño:" + nombre_completo)
            print(" Cita agendada para: "+ Disponibilidad)
            print("Turno: " + turno)
            print("Hora: " + horario)
            print("Se aplicará la vacuna de "+ seleccionVacunas)
            print("Médico a cargo: Enrique")

        elif turno == "TARDE":
            print("== Cancelación de cita ==")
            print(" **Cita de: " + Nombre_Mascota)
            print("Dueño:" + nombre_completo)
            print(" Cita agendada para: "+ Disponibilidad)
            print("Turno: " + turno)
            print("Hora: " + horario)
            print("Se aplicará la vacuna de "+ seleccionVacunas)
            print ("Médico a cargo: Carlos ")

        elif turno == "FIN DE SEMANA":
            print("== Cancelación de cita ==")
            print(" **Cita de: " + Nombre_Mascota)
            print("Dueño:" + nombre_completo)
            print(" La cita se realizó el día de fin de semana.")
            print("Turno: " + turno)
            print("Hora: " + horario)
            print("Se aplicará la vacuna de "+ seleccionVacunas)
            print("Médico a cargo: Luis")

        cambioCita=input("Desea realizar un cambio? (Si o No): ")
        if cambioCita == "SI" :
            print("1.Agendar Cita")
            print("2.Vacunación")
            seleccionCambio = int(input("Seleccione en donde desea realizar el cambio"))
            if seleccionCambio == 1:
                turno, horario = Cita()
            elif seleccionCambio == 2:
                turno, horario,seleccionVacunas = vacunas(turno, horario, seleccionVacunas)
        else:
            print("Gracias por su cita")
        
        return turno, horario, seleccionVacunas

    
    
    seleccionModulo = 0
    seleccionVacunas = ""
    #Vacuna Polivalente
    dosis_Polivalente = 4
    aplicacion_Polivalente = 20
    #Vacuna de Gripe
    dosis_Gripe = 1
    aplicacion_Gripe = ""
    #Vacuna Giardia 
    dosis_Giardia = 2
    aplicacion_Giardia = 21
    #Vacuna Antirábica
    dosis_Antirabica = 1
    aplicacion_Antirabica = ""
    #Cambio de cita
    cambioCita = ""
    seleccionCambio = 0
    while seleccionModulo != 4:
        print("**Módulo Clínico**")
        print("1.Agendar cita")
        print("2.Vacunación")
        print("3.Cancelación de cita")
        print("4. Salir")
        seleccionModulo = int(input("Ingrese la opción que desea realizar: "))
        if seleccionModulo == 1:
            turno, horario = Cita()
        elif seleccionModulo == 2:
            turno, horario,seleccionVacunas = vacunas(turno, horario, seleccionVacunas)
        elif seleccionModulo == 3:
           turno, horario, seleccionVacunas = cancelacion (turno, horario, seleccionVacunas)
    
else:
 print("Usuario o contraseña incorrectos")






