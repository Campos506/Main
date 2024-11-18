class Lector:
 
  #Constructor
  def __init__(self, nombre_archivo):
    self.nombre_archivo = nombre_archivo
    self.documento_editar = open(nombre_archivo, "a")
    self.documento_leer = open(nombre_archivo, "r")

  #Metodo para agregar un nuevo sismo
  def Metodo_1(self, lista):
    if(lista[0] != ""):
      #Si existe un comentario lo agrega
      self.documento_editar.write("\n#"+str(lista[0])+"\n"+str(lista[1])+"\t"+str(lista[2])+"\t"+str(lista[3])+"\t"+str(lista[4])+"\t"+str(lista[5])+"\t"+str(lista[6]))
      self.documento_editar.close()
    
    else:
      #Si no existe un comentario no lo agrega
      self.documento_editar.write("\n"+str(lista[1])+" "+str(lista[2])+" "+str(lista[3])+" "+str(lista[4])+" "+str(lista[5])+" "+str(lista[6]))
      self.documento_editar.close()

  #Metodo para encontrar el sismo con la mayor magnitud
  def Metodo_2(self, año, mes, dia):
    vector_generico_linea = []
    vector_generico = []
    mayor_sismo = 0
    mayor_sismo_posicion = 0

    #Recorriendo las lineas para obtener los sismos con el dia, mes y año correspondientes
    for linea in self.documento_leer:
      vector_generico_linea = linea.strip().split("\t")
      if(len(vector_generico_linea) == 6):
        if(vector_generico_linea[1] == str(año)+"-"+str(mes)+"-"+str(dia)):
          vector_generico.append(vector_generico_linea)

    #Si se encuentran sismos en los dias correspondientes se busca cual es el que posee mayor magnitud
    if(len(vector_generico) != 0):
      for i in range(len(vector_generico)):
        if(float(vector_generico[i][3]) > mayor_sismo):
          mayor_sismo = float(vector_generico[i][3])
          mayor_sismo_posicion = i
      vector_generico_maximo = vector_generico[mayor_sismo_posicion]
      #Se imprime el sismo con mayor magnitud
      print("A la hora " +str(vector_generico_maximo[2])+ " se registró un sismo de magnitud "+str(vector_generico_maximo[3])+ " en escala de Richter y profundidad " +str(vector_generico_maximo[4])+ " km en " +str(vector_generico_maximo[5]))

    #Si no se encuentran sismos para esa fecha
    else:
      print("No hay sismos registrados para ese día.")
  
  #Metodo para obtener el promedio de profundidades
  def Metodo_3(self):
    vector_generico = []
    sumatoria_profundidades = 0

    #Se obtienen las profundidades de cada sismo y se guardan en un vector generico
    for linea in self.documento_leer:
      vector_generico_linea = linea.strip().split("\t")
      if(len(vector_generico_linea) == 6):
        vector_generico.append(vector_generico_linea[4])

    #Se recorre el vector generico de profundidades sumandolas
    for i in range(len(vector_generico)):
      sumatoria_profundidades = sumatoria_profundidades + float(vector_generico[i])
      
    #Se imprime la profundidad promedio
    print('La profundidad promedio es de',str(round(sumatoria_profundidades/len(vector_generico), 2)),'km')