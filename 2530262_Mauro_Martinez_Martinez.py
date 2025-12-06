##Nombre: Mauro Martínez Martínez
##Matrícula: 2530262
## Grupo: IM 1-2

"""
Este trabajo implementa un CRUD en memoria para gestionar un conjunto de
ítems (por ejemplo, productos de inventario). El programa usa una estructura
tipo dict of dicts (clave = id del item) para permitir búsquedas rápidas por id.
La lógica de cada operación está encapsulada en funciones (create/read/update/delete),
y el usuario interactúa mediante un menú numérico. Se realizan validaciones
de entrada para evitar datos inválidos (ids vacíos, precios negativos, cantidades negativas).
"""

#DESCRIPCIÓN DEL PROBLEMA

"""
Problem: Gestor CRUD en memoria con funciones
Descripción: Implementar un CRUD que permita crear, leer, actualizar,
eliminar y listar ítems. Cada ítem tiene: id (único), name, price, quantity.
Entradas: opción del menú, item_id, name, price, quantity.
Salidas: mensajes de resultado y listado legible de ítems.
Validaciones: option 0..5, id no vacío, price >= 0.0, quantity >= 0, sin duplicados al crear.
"""

#CÓDIGO 

def create_item(items_dict, item_id, name, price, quantity):
    if item_id in items_dict:
        return False
    items_dict[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def read_item(items_dict, item_id):
    return items_dict.get(item_id)

def update_item(items_dict, item_id, new_name=None, new_price=None, new_quantity=None):
    item = items_dict.get(item_id)
    if item is None:
        return False
    if new_name is not None:
        item["name"] = new_name
    if new_price is not None:
        item["price"] = new_price
    if new_quantity is not None:
        item["quantity"] = new_quantity
    return True

def delete_item(items_dict, item_id):
    if item_id in items_dict:
        items_dict.pop(item_id)
        return True
    return False

def list_items(items_dict):
    return list(items_dict.items())

def parse_price(price_text):
    price = float(price_text)
    if price < 0.0:
        raise ValueError
    return price

def parse_quantity(quantity_text):
    q = int(quantity_text)
    if q < 0:
        raise ValueError
    return q

def input_non_empty(prompt):
    v = input(prompt).strip()
    if v == "":
        raise ValueError
    return v

def show_menu():
    print("==== CRUD MENU ====")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")

def main():
    items = {}
    while True:
        show_menu()
        option_text = input("Option: ").strip()
        try:
            option = int(option_text)
        except:
            print("Error: invalid input")
            continue
        if option < 0 or option > 5:
            print("Error: invalid input")
            continue

        if option == 0:
            break

        elif option == 1:
            try:
                item_id = input_non_empty("Item id: ")
                if item_id in items:
                    print("Error: invalid input")
                    continue
                name = input_non_empty("Name: ")
                price = parse_price(input_non_empty("Price: "))
                quantity = parse_quantity(input_non_empty("Quantity: "))
            except:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: invalid input")

        elif option == 2:
            try:
                item_id = input_non_empty("Item id: ")
            except:
                print("Error: invalid input")
                continue
            item = read_item(items, item_id)
            if item is None:
                print("Item not found")
            else:
                print("Item:", item_id, "-", f"name: {item['name']}, price: {item['price']}, quantity: {item['quantity']}")

        elif option == 3:
            try:
                item_id = input_non_empty("Item id: ")
            except:
                print("Error: invalid input")
                continue
            if item_id not in items:
                print("Item not found")
                continue

            name_text = input("New name (leave blank to keep current): ").strip()
            price_text = input("New price (leave blank to keep current): ").strip()
            quantity_text = input("New quantity (leave blank to keep current): ").strip()

            new_name = None
            new_price = None
            new_quantity = None

            try:
                if name_text != "":
                    new_name = name_text
                if price_text != "":
                    new_price = parse_price(price_text)
                if quantity_text != "":
                    new_quantity = parse_quantity(quantity_text)
            except:
                print("Error: invalid input")
                continue

            if update_item(items, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        elif option == 4:
            try:
                item_id = input_non_empty("Item id: ")
            except:
                print("Error: invalid input")
                continue
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        elif option == 5:
            all_items = list_items(items)
            print("Items list:")
            if not all_items:
                print("(no items)")
            else:
                for iid, data in all_items:
                    print(f"- {iid}: name={data['name']}, price={data['price']}, quantity={data['quantity']}")

    print("Goodbye!")

if __name__ == "__main__":
    main()


# CONCLUSIONES 

"""
El uso de funciones separadas para cada operación CRUD simplifica el
flujo principal y facilita pruebas unitarias. Elegir dict of dicts permite
accesos y modificaciones rápidas por id, evitando búsquedas lineales.
Las validaciones (id no vacío, price >= 0, quantity >= 0) previenen errores
de ejecución y mantienen la integridad de los datos. Para ampliar el sistema
se podría añadir persistencia (archivo JSON o base de datos) y manejo de usuarios.
"""

# REFERENCIAS 

"""
1) Python documentation - Data structures (dict, list)
2) Python documentation - Defining functions
3) Tutoriales sobre CRUD básico en Python
"""


#carga a github 

"""
    URL:
    https://github.com/Mauro-Mtz/MauRepo.git

    perdone si algunas cargas no tienen el url de github
    si los archivos no aparecen en el repoitorio solo informeme para subirlo
"""