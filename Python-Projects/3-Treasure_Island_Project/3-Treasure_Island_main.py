import stuff as stf
import time
import arte



print(arte.treasure_chest)
print("Bienvenido a Treasure island!")
print("Tu misión es encontrar el tesoro que se oculta en el fondo de la isla.")
#time.sleep(5)
print("Tendrás que superar las diferentes pruebas para llegar a dicho tesoro. Empecemos." + "\n" * 5)
#time.sleep(5)

jugando = True
print(arte.boat)


print("Te has cruzado con una tormenta y tu barco se ha hecho pedazos. Terminas arrojado en una isla desierta.")
#time.sleep(6)
print("Logras ver palmeras, los restos de lo que antes era tu barco y un sendero que lleva a la selva")

while jugando:

  print("\n Opciones: ")
  print("1. Investigar Barco.")
  print("2. Investigar Palmeras.")
  print("3. Entrar en la selva.")
  print("4. Inventario.")
  
  try:
    ch1 = int(input("¿Qué haces?: "))
  except ValueError:
      print("⚠️ Ingresa un número válido.")
      continue  
  print("\n" * 2)
  
  
  
  if ch1 == 1:
    print("Investigas el barco...\n")
    time.sleep(2)
    stf.loot("Cuchillo Viejo","Brújula Oxidada")
  
  elif ch1 == 4:
    stf.mostrar_inv()










  print("Vas caminando y te encuentras con una intersección de 3 caminos.")
  print(arte.hall)

  caminos = int(input("Por cual continúas? (1:Izquierda // 2:Centro // 3:Derecha )"))
