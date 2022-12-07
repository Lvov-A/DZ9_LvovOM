list_user = {
    "Leha": "0982046900",
    "Maha": "0956789101",
    "Vitos": "0980000000",
    "Sergo": "0986666666",
}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as exception:
            return exception.args[0]
    return wrapper


def parser(msg):
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
    list_contacts = ""
    for key, value in list_user.items():
        list_contacts += f'{key} : {value} \n'
    return list_contacts[:-2]

@input_error
def show_phone(name):
    res_phone = list_user.get(name)
    if res_phone == None:
        raise ValueError(f"Contact {name} not found")
    else:
        return res_phone

@input_error
def add_contact(name, phone):
    if not name or not phone:
        raise ValueError("More arguments needed")
    else:
        list_user[name] = phone
        return "Number saved"


OPERATIONS = {
    "show all": show_all,
    "phone": show_phone,
    "add": add_contact,
    "change": add_contact
}

def handler(user_msg):
    list_msg = parser(user_msg)
    if list_msg[0] == "hello":
        return "How can I help you?"   
    elif list_msg[0] == "add":
        return(OPERATIONS["add"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "change":
        return(OPERATIONS["change"](list_msg[1], list_msg[2]))        
    elif list_msg[0] == "phone":
        return(OPERATIONS["phone"](list_msg[1]))  
    elif list_msg[0] == "show_all":
        return(OPERATIONS["show all"]())    
    elif list_msg[0] == "good_bye" or list_msg[0] == "close" or list_msg[0] == "exit":
        return "Good bye!"
    else:
        return "Error command"

def main():
    while True:
        user_msg = input("Enter command:")
        result = handler(user_msg)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()