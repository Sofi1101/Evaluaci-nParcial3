import csv
def menu():
    while True:
        print("\n***Bienvenido al sistema de gestión de inventario***")
        print("1. Agregar producto al inventario")
        print("2. Leer el inventario")
        print("3. Clasificar productos y generar archivo de texto")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            agregarproducto()
        elif opcion == "2":
            leerinventario()
        elif opcion == "3":
            clasificarproductos()
        elif opcion == "4":
            print("ADIÓS")
            break
        else:
            print("¡Opción inválida, intentelo nuevamente!")
def agregarproducto():
    with open("inventario.csv", "a", newline="") as file:
        writer = csv.writer(file)
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría (Electrónica, Textil o Calzado): ")
        precio = input("Ingrese el precio del producto: ")
        writer.writerow([id, nombre, categoria, precio])
    print("Producto agregado exitosamente!")
def leerinventario():
    try:
        with open("inventario.csv", "r") as file:
            for line in file:
                print(line.strip())
    except ValueError:
        print("El archivo no existe.")
def clasificarproductos():
    categorias = {"Electrónica": [], "Textil": [], "Calzado": []}
    try:
        with open("inventario.csv", "r") as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                categoria = row[2]
                if categoria in categorias:
                    categorias[categoria].append(f"{row[1]} Precio: {row[3]}")
        
        with open("clasificacion_productos.txt", "w") as file:
            for categoria, productos in categorias.items():
                file.write(f"{categoria}:\n")
                for producto in productos:
                    file.write(f"{producto}\n")
                file.write("\n")
        print("Archivo de clasificación se ha generado exitosamente")
    except ValueError:
        print("El archivo no existe")
menu()