def visitar(historial, pagina_actual, nueva_pagina):
    if pagina_actual is not None:
        historial.append(pagina_actual)

    print(f"Visitar: {nueva_pagina}")
    return nueva_pagina

def regresar(historial, pagina_actual):
    if not historial:
        print("Regresar -> sin anterior")
        return pagina_actual

    pagina_anterior = historial[-1]
    print(f"Regresar -> {pagina_anterior}")
    return pagina_anterior

def mostrar_actual(pagina_actual):
    if pagina_actual is None:
        print("No hay una pagina actual.")
    else:
        print(f"Pagina actual: {pagina_actual}")

def mostrar_historial(historial):
    if not historial:
        print("El historial esta vacio.")
        return

    print("Historial (de la mas reciente a la mas antigua):")
    for pagina in reversed(historial):
        print(f"- {pagina}")

def main():
    historial = []
    pagina_actual = None

    while True:
        print("\n--- Menu de navegacion ---")
        print("1. Visitar pagina")
        print("2. Mostrar pagina actual")
        print("3. Mostrar historial")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            nueva_pagina = input("Ingresa la pagina: ").strip()
            if not nueva_pagina:
                print("Error: la pagina no puede estar vacia.")
            else:
                guardar_actual = input(
                    "Deseas guardar la pagina actual en el historial? (s/n): "
                ).strip().lower()
                if guardar_actual == "s":
                    pagina_guardada = pagina_actual or nueva_pagina
                    historial.append(pagina_guardada)
                    print(f"Pagina guardada: {pagina_guardada}")

                pagina_anterior = pagina_actual
                pagina_actual = nueva_pagina
                print(f"Visitar: {nueva_pagina}")

                if pagina_anterior is not None:
                    desea_regresar = input(
                        "Deseas regresar a la pagina anterior? (s/n): "
                    ).strip().lower()
                    if desea_regresar == "s":
                        pagina_actual = regresar(historial, pagina_actual)
        elif opcion == "2":
            mostrar_actual(pagina_actual)
        elif opcion == "3":
            mostrar_historial(historial)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida. Selecciona un numero del 1 al 4.")

if __name__ == "__main__":
    main()