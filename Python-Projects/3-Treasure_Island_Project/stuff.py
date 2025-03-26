import time
import random
Inventario = []

def add_item(objeto):
    if objeto not in Inventario:
        Inventario.append(objeto)
        print(f"🔹 Has obtenido {objeto}!")
    else:
        print(f"Ya tienes {objeto} en tu inventario⚠️")

def tiene_obj(objeto):
    return objeto in Inventario

def mostrar_inv():
    print("\n🎒 Tu Inventario:")
    if not Inventario:
        print("   (Vacío)")
    else:
        for objeto in Inventario:
            print(f"   - {objeto}")

def usar_objeto(objeto):
    Inventario.remove(objeto)

def menu_inventario():
    while True:
        mostrar_inv()
        print("\nOpciones:")
        print("1. Volver")

        choice = input("Qué quieres hacer?: ")

        if choice == "1":
            print("Volviendo al juego...")
            time.sleep(1)
            break  

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

def loot(caso1, caso2):
    event = random.randint(1,3)
    if event == 1:
        print("No has encontrado nada.")
        time.sleep(0.4)
        print("Continúas con tu aventura")
        time.sleep(2)
    
    elif event == 2:
        print(f"Encuentras {caso1}")
        add_item(caso1)
    
    else:
        print(f"Encuentras {caso1}")
        print(f"Encuentras también {caso2}!!!")
        add_item(caso1)
        add_item(caso2)
    