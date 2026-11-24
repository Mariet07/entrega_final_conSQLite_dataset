# Importa la librería dataset para trabajar con SQLite
import dataset

# Conecta con la base de datos base.db
miBase = dataset.connect("sqlite:///base.db")


# Crea o accede a la tabla Productos
tabla = miBase["Productos"]


# Menú principal del programa
while True:
    opciones = input("\nA - Agregar\nL - Listar\nS - Salir\nAC - Actualizar producto\nBT -Buscar en toda la base\nR - Remover por nombre\nID - Borrar por ID\n").upper()

    match opciones:

        # Agregar un nuevo producto a la base de datos
        case "A":
            agregarProducto = input("\nProducto: ").strip()
            agregarPrecio = float(input("\nPrecio: ").strip())
            agregarCategoria = input("\nCategoria: ").strip()

            agregar = {"Nombre":agregarProducto,"Precio":agregarPrecio,"Categoria":agregarCategoria}

            tabla.insert(agregar)

        # Mostrar todos los productos almacenados
        case "L":
            for items in tabla:
                print(f'ID:{items["id"]} | Producto: {items["Nombre"]} | Precio: {items["Precio"]} | Categoria: {items["Categoria"]}')
                
        # Eliminar un producto buscando por nombre
        case "R":
            removerNombre = input("\nProducto a remover: ").strip()
            
            tabla.delete(Nombre=removerNombre)
            
            print(f"\n{removerNombre} se ha quitado con exito!\n")

        # Eliminar un producto utilizando su ID 
        case "ID":
            borrarID = int(input("\nID de prod. a borrar: ").strip())
            tabla.delete(id=borrarID)
            
            print(f"\nEl producto cuyo ID es {borrarID} fue quitado con exito!!!\n")

        # Actualizar los datos de un producto existente mediante el ID       
        case "AC":
            idBuscar = int(input("\nID a actualizar: "))
            
            nombreActualizar = input("\nNombre nuevo: ")
            precioActualizar = float(input("\nprecio nuevo: "))
            catActualizar = input("\nCategoria nueva: ")
            
            actualizar = {"id":idBuscar,"Nombre":nombreActualizar, "Precio":precioActualizar,"Categoria":catActualizar}
            tabla.upsert(actualizar,["id"])

        # Buscar un producto por nombre en la base de datos
        case "BT":
            buscarTodo = input("\nProducto a buscar: ")

            # Convierte los resultados en una lista para poder contar cuántos hay
            encontrados = list(tabla.find(Nombre=buscarTodo))
            
            #for encontrado in encontrados:
            #    print(f'{encontrado["Nombre"]} Se encontró en ID: {encontrado["id"]}')

            
            # Si no se encontraron coincidencias
            if len(encontrados) == 0:
                print("\nProducto no encontrado\n")
            # Si existen coincidencias, mostrarlas    
            else:
                for encontrado in encontrados:
                    print(f'{encontrado["Nombre"]} Se encontró en ID: {encontrado["id"]}')

        # Salir del programa
        case "S":
            break
            
            
            
            
