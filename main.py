import json

file = "data.json"


def choices():
    print("1. View data")
    print("2. Add data")
    print("3. Delete data")
    print("4. Edit data")
    print("5. Exit")


def view_data():
    with open(file, "r") as json_file:
        data = json.load(json_file)
        j = 0
        for i in data:
            dni = i["dni"]
            name = i["name"]
            email = i["email"]
            print(f"Index number: {j}")
            print(f"DNI: {dni}")
            print(f"Nombre: {name}")
            print(f"Correo: {email}")
            print("="*15)
            print("\n\n")
            j = j + 1


def add_data():
    item_data = {}
    with open(file, "r") as f:
        data = json.load(f)
    item_data["dni"] = input("Dni: ")
    item_data["name"] = input("Nombres: ")
    item_data["lastname"] = input("Apellidos: ")
    item_data["email"] = input("Correo: ")
    data.append(item_data)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def delete_data():
    view_data()
    new_data = []
    with open(file, "r") as f:
        data = json.load(f)
        data_length = len(data)-1
    print("Which index number would you like to delete?")
    delete_option = input(f"Select a number 0-{data_length}")
    i = 0
    for entry in data:
        if i == int(delete_option):
            pass
            i = i + 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(file, "w") as f:
        json.dump(new_data, f, indent = 4)

def edit_data():
    view_data()
    new_data = []
    with open(file, "r") as f:
        data = json.load(f)
        data_length = len(data)-1
    print("Which index number would you like to edit?")
    edit_option = input(f"Select a number 0-{data_length}: ")
    i = 0
    for entry in data:
        if i == int(edit_option):
            dni = entry["dni"]
            name = entry["name"]
            email = entry["email"]
            status = entry["status"]
            status = "Bloqueado"
            new_data.append({"dni": dni, "name": name, "email": email, "status": status})
            print("="*15)
            i = i + 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(file, "w") as f:
        json.dump(new_data, f, indent = 4)

while True:
    choices()
    choice = input("\nEnter number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        edit_data()
    elif choice == "5":
        break
    else:
        print("You did not select a correct number, please read more carefully")
