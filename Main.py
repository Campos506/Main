#Se importa la libreria os para saber si existe un document y la Clase Lector del modulo anterior
import class_lector
import os

#Metodo principal
def Principal():
  valor_correcto = False
  nombre_documento = ""

  print('INICIO DEL PROGRAMA')
  #Se verifica si el nombre de archivo ingresado por el usuario existe
  while valor_correcto == False:
    nombre_documento = (input("Ingrese un nuevo nombre de archivo: ")+".txt")
    if os.path.exists(nombre_documento):
      valor_correcto = True
    else:
      print("El archivo especificado no existe para ser leido\n")

  terminar_programa = False
  while terminar_programa == False:
    #Se crea la instancia de la clase Lector para poder utilizar sus metodos y atributos
    documento = class_lector.Lector(nombre_documento)
    try:
      Seleccion = input("\nMENU. 1- Nuevo sismo  2- Mas fuerte de un dia  3- Profundidad promedio  4- Salir >>> ")
      #Si se selecciona la opcion 1 se procede a crear un vector generico y llenarlo con lo que el usuario ingresa
      if(Seleccion == "1"):
        vector_generico = [0] * 7
        vector_generico[0] = input("Ingrese comentario: ")
        vector_generico[1] = input("Ingrese identificador: ")
        vector_generico[2] = input("Ingrese fecha (AAAA-MM-DD): ")
        vector_generico[3] = input("Ingrese hora (HH:MM): ")      
        vector_generico[4] = input("Ingrese magnitud: ")      
        vector_generico[5] = input("Ingrese profundidad: ")
        vector_generico[6] = input("Ingrese locacion: ")
        #Se envia el vector generico al metodo 1
        documento.Metodo_1(vector_generico)

        if(vector_generico[0] == ""):
          print("Se ingreso el sismo al archivo")
        else:
          print("Se ingreso el comentario y el sismo al archivo")
      
      #Si se selecciona la opcion 2 se solicita el año, mes y dia que se desea consultar al usuario
      elif(Seleccion == "2"):
        documento.Metodo_2(input("Ingrese año: "), input("Ingrese mes: "), input("Ingrese dia: "))
      
      #Si se selecciona la opcion 3 se obtiene el promedio de profundidades con el metodo 3
      elif(Seleccion == "3"):
        documento.Metodo_3()

      #Si se selecciona la opcion 4 se termina el programa
      elif(Seleccion == "4"):
        print("\nFIN DEL PROGRAMA")
        terminar_programa = True
      
      else:
        print("\nEsa no es una opcion valida")

    except ValueError:
      print("No se ha ingresado un tipo de dato correcto")


#SE LLAMA AL METODO PRINCIPAL PARA INICIAR EL PROGRAMA
Principal()