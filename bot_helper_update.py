import os 
list_contact=list()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args




def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return"Помилка 😭"
        except IndexError:
            return"Enter the argument for the command"
        except Exception as eror:
            print(f"Error: {eror}")
    return inner




@input_error
def add_contact(*args):
    total_list={"Name":args[0],"Number":args[1]}
    list_contact.append(total_list)
    return "Contact added."


def show_all():
    print(list_contact)




@input_error
def change_contact(*args):
    update=False                    
    for name in list_contact:
        iteam=name["Name"]
        if iteam==args[0]:
            update=True
            name["Number"]=args[1]
            print("Контакт оновленно.")
    if update==False:
        print("Немає такого контакта")






@input_error
def show_phone(*args):
    update=False
    for name in list_contact:
        iteam=name["Name"]
        if iteam==args[0]:
            print(name)
            update=True
    return ("Немає такого, перевірте та спробуйте ще раз" if update==False else "Знайденно")
    





def main():
    os.system('cls')
    
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        

        if command in ["close", "exit"]:
            print("Good bye!")
            break


        elif command == "hello":
            print("How can I help you?")


        elif command=="add":
            print(add_contact(*args))
        

        elif command=="change":     
            print(change_contact(*args))
                    

        elif command=="phone":
            print(show_phone(*args))


        elif command=="all":
            show_all()


        elif command in ["cls","clear"]:
            os.system('cls')
            

        else:
            print("Invalid command.")


            


if __name__ == "__main__":
    main()