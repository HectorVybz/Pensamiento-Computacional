# Pidele al usuario una lista de objetos de supermercado y muestralos
    #append es para agregar algo en la lista y se ponga hasta el final
productos = []
cantidad = int(input("Que tantos objetos vas a comprar : "))
for i in range (cantidad):
    productos.append (input("Que articulos quieres comprar : "))
for i in productos:
    print("En tu lista esta : ", i)