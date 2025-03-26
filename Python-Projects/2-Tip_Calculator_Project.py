print("Calculadora de propina\n")
cuenta = float(input("Ingresar valor de la cuenta: "))
opcion = int(input("Cuanto quisieras dar de propina? (10, 12 o 15 %?): "))
personas = int(input("Entre cuantas personas se dividen la cuenta?: "))

total = (cuenta * (1 + opcion / 100)) / personas

print(f"Se debe pagar: {round(total,2)} por persona ")