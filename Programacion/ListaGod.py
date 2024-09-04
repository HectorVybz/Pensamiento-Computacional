def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos objetos vas a comprar? "))
            if cantidad > 0:
                return cantidad
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def agregar_productos(cantidad):
    productos = []
    for i in range(cantidad):
        producto = input(f"Ingrese el artículo #{i + 1}: ")
        productos.append(producto)
    return productos

def mostrar_productos(productos):
    print("\nEn tu lista están:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")

def eliminar_producto(productos):
    mostrar_productos(productos)
    while True:
        try:
            index = int(input("¿Qué número de producto quieres eliminar? ")) - 1
            if 0 <= index < len(productos):
                eliminado = productos.pop(index)
                print(f"Producto '{eliminado}' eliminado.")
                return
            else:
                print("Número de producto no válido. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def ordenar_productos(productos):
    productos.sort()
    print("\nLista ordenada alfabéticamente:")
    mostrar_productos(productos)

def main():
    cantidad = obtener_cantidad()
    productos = agregar_productos(cantidad)
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar productos")
        print("2. Eliminar producto")
        print("3. Ordenar productos")
        print("4. Mostrar total de productos")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            eliminar_producto(productos)
        elif opcion == "3":
            ordenar_productos(productos)
        elif opcion == "4":
            print(f"\nTotal de productos en la lista: {len(productos)}")
        elif opcion == "5":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
