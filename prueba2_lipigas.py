
cant_cilindro_5kilos = 0;
cant_cilindro_15kilos = 0;
cant_cilindro_45kilos = 0;
name_cliente = " ";
contacto_cliente = " ";
precioCamion = 765000;
cant_camion = 0;
pesoMax_camion = 450;
cant_kilo = 0;
valor_total = 0;
op1 = True;
op2 = True;
op3 = 0;

while op1 == True:

    name_cliente = input ("Por favor! indicame su nombre: ")
    if len(name_cliente)>=3 :
        
        print("Bienvenido señor/@: ", name_cliente)
    else: 
        print("Lo siente su nombre debe tener como minimo 3 letras")
        
       
    contacto_cliente = input("Por favor! indicame su numero: ")
    if len(contacto_cliente) == 9:
            print("Felicidades se guardo correctamente su numero!")
            
    else:
            print("lo siento su numero debe ser minimo de 8 digitos y de 9 maximo: ") 
            op1 = True
    op1 = False




    while op2 == True:
          #menu de opciones
          print(" ")
          print("1_Compra de camion Estandar: ")
          print("2_ compra por kilos: ")
          print("3_Salir ")

          if op3 == 1:
                cant_camion = int(input("Por favor, me indicas cuanto camiones vas a comprar: "))
                valor_total = cant_camion * precioCamion;
          elif op3 == 2:
                if cant_kilo == pesoMax_camion:
                      valor_total = precioCamion 


