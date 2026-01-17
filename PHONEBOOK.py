
contacts = {}
def show_menu():
    print("-" * 35)
    print(" 📖 PYTHON PHONEBOOK 📖 ")
    print("-" * 35)
    print("1. Add Contact")
    print("2. View all Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contacts():
    name = input("Enter Contact name: ").strip().capitalize()

    if name in contacts:
        print("❌ Contact already Exists!")
    else:
        phone = input("Enter phone number: ").strip().capitalize()
        contacts[name] = phone
        print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📫 Contact book is empty.")
    else:
        print("📞 CONTACT LIST:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
def search_contacts():
    name = input("Enter name to search: ").strip().capitalize()

    if name in contacts:
        print(f"📱 {name}'s number is {contacts[name]}")
    else:
        print("❌ Contact Not Found.")

def update_contacts():
    name = input("Enter name to update: ").strip().capitalize()

    if name in contacts:
        new_phone = input("Enter new phone number: ").strip().capitalize()
        contacts[name] = new_phone
        print("✅ Contact updated successfully!")
    else:
        print("❌ Contact not found.")

def delete_contacts():
    name = input("Enter name to delete: ").strip().capitalize()

    if name in contacts:
        del contacts[name]
        print("✅ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        update_contacts()
    elif choice == "5":
        delete_contacts()
    elif choice == "6":
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1-6.  ")