def obtener_cantidad():
    while True:
        try:
            return int(input("¿Cuántos objetos vas a comprar? "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def agregar_productos(cantidad):
    productos = {}
    for i in range(cantidad):
        producto = input(f"Ingrese el artículo #{i + 1}: ")
        precio = float(input(f"Ingrese el precio del artículo #{i + 1}: "))
        productos[producto] = precio
    return productos

def mostrar_productos(productos):
    print("\nEn tu lista están:")
    for producto, precio in productos.items():
        print(f"{producto} - ${precio:.2f}")

def eliminar_producto(productos):
    mostrar_productos(productos)
    producto = input("\n¿Qué producto quieres eliminar?: ")
    if producto in productos:
        del productos[producto]
        print(f"Producto '{producto}' eliminado.")
    else:
        print("Producto no encontrado.")

def calcular_total(productos):
    total = sum(productos.values())
    print(f"\nEl total a pagar es: ${total:.2f}")

def main():
    cantidad = obtener_cantidad()
    productos = agregar_productos(cantidad)
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar productos")
        print("2. Eliminar producto")
        print("3. Mostrar total a pagar")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            eliminar_producto(productos)
        elif opcion == "3":
            calcular_total(productos)
        elif opcion == "4":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
