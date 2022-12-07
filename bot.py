list_user = {
    "Leha": "0982046900",
    "Maha": "0956789101",
    "Vitos": "0980000000",
    "Sergo": "0986666666",
}

def parser():
    msg = input("Enter command:")
    msg = msg.replace("show all", "show_all")
    msg = msg.replace("good bye", "good_bye")
    msg = msg.split(' ')
    command = msg[0].lower()
    name = None
    phone = None
    if len(msg) >= 2:
        name = msg[1]
    if len(msg) == 3:
        phone = msg[2]

    return command, name, phone

def show_all():
    for key, value in list_user.items():
        print(key, value)

def show_phone(name):
    res_phone = list_user.get(name)
    print(res_phone)

def add_contact(name, phone):
    if not name or not phone:
        print("More arguments needed")
    else:
        list_user[name] = phone

OPERATIONS = {
    "show all": show_all,
    "phone": show_phone,
    "add": add_contact,
    "change": add_contact
}

def handler():
    while True:
        list_msg = parser()
        if list_msg[0] == "hello":
            print("How can I help you?")   
        elif list_msg[0] == "add":
            OPERATIONS["add"](list_msg[1], list_msg[2]) 
        elif list_msg[0] == "change":
            OPERATIONS["change"](list_msg[1], list_msg[2])        
        elif list_msg[0] == "phone":
            OPERATIONS["phone"](list_msg[1])  
        elif list_msg[0] == "show_all":
            OPERATIONS["show all"]()       
        elif list_msg[0] == "good_bye" or list_msg[0] == "close" or list_msg[0] == "exit":
            print("Good bye!")
            break

if __name__ == "__main__":
    handler()