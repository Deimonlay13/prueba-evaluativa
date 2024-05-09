

import os
import time
l = ("cls")
os.system(l)
m = int(1)
p1 = 0
p1p = 0
p1t = 0
p2 = 0 
p2p = 0
p2t = 0
p3 = 0
p3p= 0
p3t = 0
p4 = 0
p4p = 0
p4t = 0  
total = 0 
tdp = 0
op = 0
desc = 0
dc1 = 0
lent = 1
while m == 1:


    print(" ")
    print(" ")
    print("Bienvenido a Sushi koda ")
    print("Que desea comprar.(opciones 1-4 )")
    print("1. Pikachu Roll  Valor: $4500")
    print("2. Otaku Roll  Valor: $5000")
    print("3. Pulpo Venenoso Roll  Valor: $5200")
    print("4. Anguila Elèctrica Roll  Valor: $4800")
    print(" ")
    try:
        op = int(input("Seleciones el Roll que quiera (1-4)  :"))
        print(" ")
    except ValueError:
        print(" ")
        print("indica un numero valido")
        time.sleep(1.6)
        os.system(l)
        continue
        


    if op == 1:
        while op ==1:
          try: 
            p1 = int(input("escogio Pikachu Roll  Valor: $4500 - Cuantos desea comprar: "))
            if p1 < 0:
               print(" ")
               print("porfavor ingresa un  numero mayor o igual a 0")
               print(" ")
               continue
            print(" ")
            p1p = (p1 + p1p)
            p1t = (p1p)
            p1t = (p1t * 4500)
            break 
          except ValueError:
            print(" ")
            print("seleciones una numero porfavor ") 
            print(" ")
            continue
            
    elif op == 2: 
        while op==2:
         try:
            p2 = int(input("escogio Otaku Roll  Valor: $5000 - Cuantos desea comprar: "))
            if p2 < 0:
               print(" ")
               print("porfavor ingresa un  numero mayor o igual a 0")
               print(" ")
               continue
            print(" ")
            p2p = (p2 + p2p)
            p2t = (p2p)
            p2t = (p2t * 5000)
            break
         except ValueError:
            print(" ")
            print("seleciones una numero porfavor ") 
            print(" ")
            continue
    elif op == 3:
        while op ==3:
         try:
            p3 = int(input("escogio Pulpo Venenoso Roll  Valor: $5200 - Cuantos desea comprar: "))
            if p3 < 0:
               print(" ")
               print("porfavor ingresa un  numero mayor o igual a 0")
               print(" ")
               continue
            print(" ")
            p3p = (p3 + p3p )
            p3t = (p3p)
            p3t = (p3t * 5200)
            break
         except ValueError:
            print(" ")
            print("seleciones una numero porfavor  ") 
            print(" ")
            continue
    elif op == 4:
        while op ==4:
         try:
            p4 = int(input("escogio Anguila Electrica Roll  Valor: $4800 - Cuantos desea comprar: "))
            if p4 < 0:
               print(" ")
               print("porfavor ingresa un  numero mayor o igual a 0")
               print(" ")
               continue
            print(" ")
            p4p = (p4 + p4p)
            p4t = (p4p) 
            p4t = (p4t * 4800)
            break
         except ValueError:
            print(" ")
            print("seleciones una opcion valida porfavor (1-4)")   
            print(" ")
            continue
    else:
        print("seleciones una opcion valida porfavor (1-4)")   
        continue 

    t = (p1t + p3t + p4t + p2t)
    lent = 1
    while lent ==1:
        try: 
            m = int(input("desea seguir comprar otro Roll?: (1 = SI)(2 = No) (porfavor selecione 1 o 2) : "))
            if m ==1:
              lent =2
            elif m ==2 :
             lent = 2 
            else: 
               print("")
               print("seleciona una opcion valida (1 - 2)")
               print(" ")
               continue
            lent = 2 
            time.sleep(1.6)
            os.system(l)
        except ValueError:
            print(" ")
            print("seleccione una opcion valida (1 - 2 )")
            print(" ")
            continue

    
    
    t = (p1t + p3t + p4t + p2t)
    tp = (p1p + p2p + p3p + p4p)
    if m == 1:
        continue
    elif m == 2:
        print(" ")
    

    while m == 2:


        
        
    
        try:
            
            print(" ")
            dc1 = int(input("Posee un codigo de Descuento ?(1 = si) (2 = no): "))
            if (int(dc1))>= 1 and (int(dc1))<= 2:
                print(" ") 
            else:
                print(" ")
                print("ingrese 1 o 2")   
        except ValueError:
            print(" ")
            print("Debe ingresar 1 o 2") 
            continue   
        
               
        if dc1 == 1:
          print(" ")
          dc = input("INGRESE EL CODIGO DE DESCUENTO: ")  
          if dc == ("soyotaku"):
              print(" ")
              print("SE REALISO EL DESCUENTO DEL %10 ")
              print(" ")
              desc = (t / 10)
              total =(t - desc)
              print("*"*40)
              print(f"TOTAL PRODUCTO:{tp}")
              print("*"*40)
              print("     Producto           cantidad        Precios")
              print(f"1-Pikachu Roll:            {p1p}        Valor:${p1t}")
              print(f"2-Otaku Roll:              {p2p}        Valor:${p2t}")
              print(f"3-Pulpo Venenoso Roll:     {p3p}        Valor:${p3t}")
              print(f"4-Anguila Electrica Roll:  {p4p}        Valor:${p4t}")
              print("*"*40)
              print(f"Subtotal a pagar:${t}")
              print(f"Descuento por Codigo:${desc}")
              print(f"Total:${total}")
              print(" ")
              break
          elif dc != ("soyotaku"):
            print(" ")
            print("codigo invalido")
            print(".")
            dc1 = input("Desea REIGRESAR el Codigo? (1- si)(volver a el menu = X ) selecione 1 o X: ")
            print(" ")
            if dc1 == 1:
              print(" ")
              continue
            elif dc1 ==("X"):
                m =1 
                continue
            else:
                print(" ")
                m = 1
                continue
        elif dc1  == 2:
            print(" ")
            total = (t)
            print("*"*40)
            print(f"TOTAL PRODUCTO:{tp}")
            print("*"*40)
            print("     Producto           cantidad        Precios")
            print(f"1-Pikachu Roll:            {p1p}        Valor:${p1t}")
            print(f"2-Otaku Roll:              {p2p}        Valor:${p2t}")
            print(f"3-Pulpo Venenoso Roll:     {p3p}        Valor:${p3t}")
            print(f"4-Anguila Electrica Roll:  {p4p}        Valor:${p4t}")
            print("*"*40)
            print(f"Subtotal a pagar:${t}")
            print(f"Descuento por Codigo:${desc}")
            print(f"Total:${total}")
            print(" ")
            break
        else:
            print(" ")
           
    if dc1 ==("X"):
       print(" ")
       continue

    while lent == 2:
        try: 
         m = int(input("Desea hacer otro pedido?(1-si)(2-No): "))
         if m ==2:
            break
         
         if m ==1:
            m =1
            p1 = 0
            p1p = 0
            p1t = 0
            p2 = 0 
            p2p = 0
            p2t = 0
            p3 = 0
            p3p= 0
            p3t = 0
            p4 = 0
            p4p = 0
            p4t = 0  
            total = 0 
            tdp = 0
            op = 0
            desc = 0
            dc1 = 0
            lent = 1
            break
         else:
          print(" ")
          print("ingresa 1 - 2 porfavor")

        except ValueError:
          print(" ")
          print("ingresa un numero porfavor")
          continue
    continue

        
print(" ")
print(" ")
print("gracias por comprar")

    
        


      



    



    
    




     
    


