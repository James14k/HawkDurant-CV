cant_cilindro_5kilos = 0;
cant_cilindro_15kilos = 0;
cant_cilindro_45kilos = 0;
name_cliente = " ";
contacto_cliente = " ";
precioCamion = 765000;
cant_camion = 0;
pesoMax_camion = 450;
excedente = 0;
respuesta = " "
cant_kilo_1 = 0;
cant_kilo_2 = 0;
cant_kilo_3 = 0;
cant_kilo_total = 0;
valor_total_1 = 0
primerBucle = True
option_2 = True;
op3 = 0;

while primerBucle == True:
       print(" ")
       name_cliente = input ("Por favor! indicame su nombre:\n ")
       if len(name_cliente) > 2:
          print("Bienvenido señor/@: ", name_cliente)
       else:
           primerBucle = True
           print("Error, por favor ingrese un nombre que tengas mas de 2 letras")
           
       contacto_cliente = input("Por favor! indicame su numero: ")
       if len(contacto_cliente) == 9:
          print("Felicidades se guardo correctamente su numero!")  
          primerBucle = False    
       else:
            primerBucle = True
            print("lo siento su numero debe ser minimo de 9 digitos maximo: ")
            
while option_2 == True:
    
    #menu de opciones
      print(" ")
      print("1_Compra de camion Estandar: ")
      print("2_ compra por kilos: ")
      print("3_Salir ")
      
      #manejo de errores
      try:
         op3 = int(input("Ingresa una opción entre 1-3: \n"));
      except ValueError:
                        print("Selecciona una opción (1-3), ya que la elegida es incorrecta");
                        continue;
      if op3 == 1:
          cant_camion = int(input("Por favor, me indicas cuanto camiones vas a comprar: "))
          valor_total_1 = cant_camion * precioCamion;
          print("El total a pagar por el/los ", cant_camion, "camion/es es de: $", valor_total_1)
          
      elif op3 == 2:
            cant_cilindro_5kilos = int(input("Por favor, indicame la Cantidad de cilindro de 5kg vas a necesitar: "))
            cant_kilo_1 = cant_cilindro_5kilos * 5
            
            cant_cilindro_15kilos =  int(input("Por favor, indicame la Cantidad de cilindro de 15kg vas a necesitar: "))
            cant_kilo_2 = cant_cilindro_15kilos * 15
            
            cant_cilindro_45kilos =  int(input("Por favor, indicame la Cantidad de cilindro de 45kg vas a necesitar: "))
            cant_kilo_3 = cant_cilindro_15kilos * 45
            
            cant_kilo_total = cant_kilo_1 + cant_kilo_2 + cant_kilo_3
            
            if cant_kilo_total == pesoMax_camion:
               valor_total_1 = valor_total_1 + precioCamion 
               print("El total a pagar es de $", valor_total_1)
               
            elif cant_kilo_total > pesoMax_camion:
                 excendente =  cant_kilo_total - pesoMax_camion 
                 valor_total_1 = valor_total_1 + ( excedente * 1700 ) + precioCamion + 10000
                 print("El total a pagar es de $", valor_total_1)

      elif op3 == 3:
           respuesta = input(" Deseas hacer otra compra : ( Presione 1/SI  |  2/ NO) ")
           if respuesta == "1":
               option_2 = True
           else:
               option_2 = False 
               
 #Factura     
print("Nombre cliente: ",name_cliente)
print("Contacto cliente: ",contacto_cliente)
if cant_camion != 0:
   print("Cantidad camion: ",cant_camion,"unidades")
elif cant_kilo_total != 0:
     print("Cantidad kilo: ",cant_kilo_total,"kg")
elif valor_total_1 != 0:
     print("Valor total: $",valor_total_1)
