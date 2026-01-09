from tkinter.font import names


class Contact:
    phone_directory = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Contact.phone_directory.append(self)

    def __str__(self):
        return f"{self.name} - {self.phone}"

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone})"

    def show_contact(self):
        return f"name: {self.name}\nContact: {self.phone}"

    @classmethod
    def show_all_contacts  (cls):
        if len(cls.phone_directory) == 0:
            print("No entry in phone book available")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())
    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone
        return f"Contact not found for: {search_name}"
    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number .isdigit():
            return True
        else :
            return False


n_contacts = int(input("How many Number of contacts you want to add: "))
for i in range(n_contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if Contact.validate_phone_number(phone):
        Contact(name, phone)
    else:
        print(f"Invalid phone number for: {name}, min 8 digits required")


c1 = Contact("Alv", 12345678)
c2 = Contact("Vake", "2erdwwfefef")
c3 = Contact("cred", "345678923344")
print(Contact.phone_directory)
Contact.show_all_contacts()
print("_________________________________________")
print(Contact.search_contact("Alv"))
#c1.show_contact()
print(Contact.search_contact("Mark"))


