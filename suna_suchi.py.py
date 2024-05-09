nombre_cliente = " ";
pikachu_roll = 4500;
otaku_roll = 5000;
pulpo_venenoso_roll = 5200;
anguila_electrica_roll = 4800;
cant_pikachu = 0;
pedido = 0;
total_pikachu = 0;
cant_otaku = 0;
total_otaku = 0;
cant_pulpo = 0;
total_pulpo = 0;
cant_anguila = 0;
total_anguila = 0;
monto_total = 0;
total = 0;
total_con_descuento = 0;
descuento = "1";
respuesta = "1";
op = True;

nombre_cliente = input("Hola, Me indica su nombre por favor:\n");
print("Bienvenido a SUNA-SUSHI");
print(" ")

while op == True:
        print("**********NUESTRO MENU**********");
        print(" ")
        print("1. Pikachu Roll | $4500");
        print("2. Otaku Roll  | $5000");
        print("3. Pulpo Venenoso Roll  | $5200");
        print("4. Anguila Eléctrica Roll  | $4800");
        print("5. Salir");
        
        try:
            pedido = int(input("Ingresa una opción entre 1-5: \n"));
        except ValueError:
                        print("Selecciona una opción (1-5), ya que la elegida es incorrecta");
                        continue;
        if pedido == 1:
            cant_pikachu = int(input("cuanto pikachu_roll vas llevar: \n"));
            total_pikachu = pikachu_roll * cant_pikachu;
            print("El monto a pagar por su compra es de: $", total_pikachu);
            
        elif pedido == 2:
           cant_otaku = int(input(" cuanto otaku_roll vas a llevar: \n"));
           total_otaku = otaku_roll * cant_otaku;
           print("El monto a pagar por su compra es de: $", total_otaku);
           
        elif pedido == 3:
            cant_pulpo = int(input("cuanto pulpo_venenoso_roll vas a llevar:\n"));
            total_pulpo = cant_pulpo * pulpo_venenoso_roll;
            print("El monto a pagar por su compra es de: $", total_pulpo);
            
        elif pedido == 4:
            cant_anguila = int(input("cuanto anguila_electrica_roll:\n"));
            total_anguila = cant_anguila * anguila_electrica_roll;
            print("El monto a pagar por su compra es de: $", total_anguila);
            
        elif pedido == 5:
            respuesta = input("No deseas hacer otra compra: (SI = 1 | NO = 2 \n");
            if respuesta == 1:
                op = True;
            else:
                op = False;
descuento = input("cuentas con algun cupon de descuento: (SI = 1 | NO = 2) ");
if descuento == "1":
   monto_total = total_anguila + total_otaku + total_pikachu;
   total_con_descuento = monto_total * 10 / 100; 
   total = total_anguila + total_otaku + total_pikachu - total_con_descuento; 
   print("Gracias por su compra el monto total a pagar es de: $", total);   
else: 
    monto_total = total_anguila + total_otaku + total_pikachu;
    print("Gracias por su compra el monto total a pagar es de: $", monto_total);
    print("Hasta Pronto! ");
            
            