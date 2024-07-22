from colorama import init, Fore, Style

init(autoreset=True)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{Fore.RED}Contact not found."
        except ValueError:
            return f"{Fore.RED}Give me name and phone please."
        except IndexError:
            return f"{Fore.RED}Invalid command."
    return inner

@input_error
def add_contact(name, phone):
    if name in contacts:
        return f"{Fore.RED}Contact {name} already exists."
    contacts[name] = phone
    return f"{Fore.GREEN}Contact added."

@input_error
def change_contact(name, new_phone):
    if name not in contacts:
        return f"{Fore.RED}Contact {name} not found."
    contacts[name] = new_phone
    return f"{Fore.GREEN}Contact updated."

@input_error
def show_phone(name):
    if name not in contacts:
        return f"{Fore.RED}Contact {name} not found."
    return f"{Fore.BLUE}{contacts[name]}"

@input_error
def show_all():
    if not contacts:
        return f"{Fore.RED}No contacts found."
    return "\n".join([f"{Fore.BLUE}{name}: {Fore.MAGENTA}{phone}" for name, phone in contacts.items()])

def main():
    print(f"{Fore.BLUE}Welcome to the assistant bot!")
    while True:
        user_input = input(f"{Fore.WHITE}Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            print(f"{Fore.BLUE}Good bye!")
            break

        elif command in ["hello", "hi"]:
            print(f"{Fore.BLUE}How can I help you?")

        elif command == "add":
            if len(args) < 2:
                print(f"{Fore.RED}Invalid command. Usage: add [name] [phone]")
            else:
                name, phone = args[0], args[1]
                print(add_contact(name, phone))

        elif command == "change":
            if len(args) < 2:
                print(f"{Fore.RED}Invalid command. Usage: change [name] [new_phone]")
            else:
                name, new_phone = args[0], args[1]
                print(change_contact(name, new_phone))

        elif command == "phone":
            if len(args) < 1:
                print(f"{Fore.RED}Invalid command. Usage: phone [name]")
            else:
                name = args[0]
                print(show_phone(name))

        elif command == "all":
            print(show_all())

        else:
            print(f"{Fore.RED}Invalid command.")

if __name__ == "__main__":
    main()
