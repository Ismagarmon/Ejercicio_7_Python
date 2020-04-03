#Ejercicio_ListaDatos_07

import time
import os


try:

    #Declaramos las listas

    provincias = ['Ávila','Burgos','León','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora','Castilla y León']
    casos_confirmados = ['414','719','821','262','1.030','567','523','886','192','5414']
    nuevos_casos_positivos = ['33','46','95','42','148','64','92','79','24','623']

    #Esta es la función que nos pasaste para hacer el ejercicio número 6 de funciones ¡muchas gracias!, es muy útil

    def pedirNumeroEntero():
        
        #Variable del bucle

        #bucle = 1 #Aquí he vuelto a cambiar el True por una variable.

        while True:
            try:
                num = int(input())
                break #bucle = 2 
            except ValueError:
                print('Error, al introducir los datos')
                print ("Intentalo de nuevo")
            
        return num

    def pedirCadenadeCaracteres():
        
        #Variable del bucle

        #bucle = 1 #Aquí he vuelto a cambiar el True por una variable.

        while True:
            try:
                num = input() #No se como poner para que solo reconozca una cadena de caracteres
                break #bucle = 2 
            except ValueError:
                print('Error, al introducir los datos')
                print ("Intentalo de nuevo")
            
        return num

    def pedirdatos():

        #Preguntamos cuantos paises quiere el usuario meter

        print("Introduce el número de provincias que quieres añadir a la lista: ")

        numero_de_provincias = pedirNumeroEntero()

        # Rellenamos los datos #Voy pillando el truquillo del bucle for
        for x in range(numero_de_provincias):
            #Introduzco el nombre de la provincia
            print("Ingrese el nombre de la provincia: ")
            nom_provincia = pedirCadenadeCaracteres()
            provincias.append(nom_provincia)
            #Introduzco el número de casos confirmados
            print("Ingrese el número de casos confirmados: ")
            num_casos = pedirNumeroEntero() 
            casos_confirmados.append(num_casos)
            #Introduce el número de nuevos casos positivos
            print("Ingrese el número de nuevos casos positivos: ")
            num_casos_positivos = pedirNumeroEntero()
            nuevos_casos_positivos.append(num_casos_positivos)

        input("Presione una tecla cualquiera...")

    def modificardatos():
        nombre = input("Introduce el nombre de la provincia: ")

        if nombre in provincias: #si esta el nombre en la lista me devuelve True
            #le pido el nuevo número de casos confirmados
            nuevos_casos = int(input("Introduce el número de los nuevos casos: "))
            indice = provincias.index(nombre)
            casos_confirmados[indice] = nuevos_casos

            nuevos_casos_positivos_modi = int(input("Introduce el número de los nuevos casos positivos: "))
            indice_1 = provincias.index(nombre)
            nuevos_casos_positivos[indice_1] = nuevos_casos_positivos_modi

            print("Nuevo número de casos confirmados es de : ", nuevos_casos,"y el de positivos es de: ",nuevos_casos_positivos_modi,".")

        else: #si no esta el nombre en la lista
            print("La provincia NO SE ENCUENTRA EN LA LISTA")

        input("\nPulse una tecla para continuar ....")

    def visualizardatos():

        print("Introduzca el nombre de la provincia que quieres ver: ")

        #Variable del número de paises que quiere visualizar

        #total_de_provincias = pedirNumeroEntero()

        nombre = pedirCadenadeCaracteres()

        if nombre in provincias: 
            indice = provincias.index(nombre)
            print("Provincias   Casos confirmados   Nuevos casos")
            print(provincias[indice]+"                 "+str(casos_confirmados[indice]),"             "+str(nuevos_casos_positivos[indice]))
        else:
            print("Introduce un valor adecuado al número de datos que hayas introducido.")
            #return total_de_provincias No se para que me devuelva otra vez la variable

        input("Presione una tecla cualquiera...")

    def eliminardatos():
        nombre = input("Introduce el nombre de la provincia que quieres eliminar: ")

        nombre = pedirCadenadeCaracteres()

        if nombre in provincias: 
            indice = provincias.index(nombre)
            eliminardatosdefinitivamente(indice)
            print("Se han eliminado correctamente los datos.")
            #Se queda pillado en cuanto los elimina, si es que los elimina claro

        else: #si no esta el nombre en la lista
            print("La provincia NO SE ENCUENTRA EN LA LISTA")

        input("\nPulse una tecla para continuar ....")

    def eliminardatosdefinitivamente(indice):
        provincias.remove(indice)
        casos_confirmados.remove(indice)
        nuevos_casos_positivos.remove(indice)


    #Variable del bucle

    varbucle = 1

    while varbucle == 1:
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        #borrar la pantalla Para DOS/Windows
        os.system ("cls")
        #Menú principal
        print("Bienvenido al programa.")
        print("1 - Rellenar datos.")
        print("2 - Visualizar datos.")
        print("3 - Modificar datos.")
        print("4 - Eliminar datos.")
        print("5 - Salir del programa.")

        opcion = pedirNumeroEntero()

        if opcion == 1:
            pedirdatos()
        elif opcion == 2:
            visualizardatos()
        elif opcion == 3:
            modificardatos()
        elif opcion == 4:
            eliminardatos()
        elif opcion == 5:
            varbucle = 2
        else:
            print("Introduzca una opción válida.")
    


except:
    print("Ha ocurrido algún error.")

#except ValueError:
    #print("No pude convertir el dato a un entero.")

#except Exception as e: # OJO SIEMPRE LA ULTIMA
    #print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )

#Me da error si descomento estos dos expect, ¿cómo les tengo que poner?

finally:
    print("Nos volveremos a ver.")