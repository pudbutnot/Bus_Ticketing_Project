import csv
import os

class Category:
    def __init__(self, category, code):
        self.category = category
        self.code = code
    def GetCode(self):
        return self.code
    def GetCategory(self):
        return self.category

class Ticket:
    def __init__(self, category, topup, price):
        self.category = category
        self.topup = topup
        self.price = price

class Customer:
    def __init__(self):
        self.purchases = []
    def buy_ticket(self, ticket):
        self.purchases.append(ticket)
        save_purchase(ticket)

def save_purchase(ticket):
    file_exists = os.path.isfile("purchases.csv")
    with open("purchases.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Category", "Topup", "Price"])
        writer.writerow([ticket.category, ticket.topup, ticket.price])

def load_categories():
    listOfCatClasses = []
    listOfCategories = []
    code = 0
    with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            category = lines['category_title']
            if category not in listOfCategories:
                listOfCategories.append(category)
                listOfCatClasses.append(Category(category, code))
                code += 1
    return listOfCatClasses

def load_topups(chosen_category):
    topup_options = []
    topup_price = []
    with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines['category_title'] == chosen_category:
                topup_options.append(lines['topup_title'])
                topup_price.append(int(lines['topup_price_in_pence']) / 100)
    return topup_options, topup_price


greeting = """Welcome to the NCTX Buses App"""
print(greeting)

try:
    response = input("Are you a customer or an admin? (C/A): ").upper()
    if response not in ['C', 'A']:
        raise ValueError
except ValueError:
    print("Error: Please enter C or A.")
    quit()
finally:
    print("You have entered a valid input")

print("You entered", response)

if response == 'C':
    print("Please choose a category of ticket")

    customer = Customer()
    listOfCatClasses = load_categories()

    for idx, cat in enumerate(listOfCatClasses):
        print("For", cat.GetCategory(), "enter", idx)

    try:
        choice = int(input("Enter your choice: "))
        chosen_category = listOfCatClasses[choice].GetCategory()
    except (ValueError, IndexError):
        print("Invalid category choice.")
        quit()

    print("You picked:", chosen_category)

    print("Please choose a top-up type")
    topup_options, topup_price = load_topups(chosen_category)

    for idx, option in enumerate(topup_options):
        print("For", option, "enter", idx)

    try:
        topup_choice = int(input("Enter your top-up choice: "))
        chosen_topup = topup_options[topup_choice]
        chosen_price = topup_price[topup_choice]
    except (ValueError, IndexError):
        print("Invalid top-up choice.")
        quit()

    print("You picked:", chosen_topup)
    print(f"This ticket costs £{chosen_price:.2f}")

    a = input("Would you like to purchase this ticket? (Y/N): ").upper()
    print("You entered", a)

    if a == 'Y':
        ticket = Ticket(chosen_category, chosen_topup, chosen_price)
        customer.buy_ticket(ticket)
        print(f"You have purchased a {chosen_topup} ticket. Your purchase has been saved.")
    else:
        print("You did not purchase a ticket. Have a good day!")

    quit()

else:
    while True:
        print("\nAdmin menu")
        print("1. View all products")
        print("2. Edit a product price")
        print("3. Quit")

        admin_choice = input("Enter your choice: ")

        if admin_choice == "1":
            print("\n--- All Products ---")
            with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
                csvFile = csv.DictReader(file)
                for row in csvFile:
                    price = int(row['topup_price_in_pence']) / 100
                    print(f"{row['category_title']} - {row['topup_title']} - £{price:.2f}")

            input("\nPress Enter to return to the admin menu...")

        elif admin_choice == "2":
            products = []
            with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
                csvFile = csv.DictReader(file)
                for row in csvFile:
                    products.append(row)

            print("\n--- Select a product to edit ---")
            for idx, p in enumerate(products):
                price = int(p['topup_price_in_pence']) / 100
                print(f"{idx}. {p['category_title']} - {p['topup_title']} - £{price:.2f}")

            try:
                choice = int(input("Enter product number: "))
                new_price = float(input("Enter new price (£): "))
                products[choice]['topup_price_in_pence'] = str(int(new_price * 100))

                with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'w', newline='') as file:
                    fieldnames = products[0].keys()
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(products)

                print("Price has been successfully updated")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except IndexError:
                print("The product number does not exist.")

            input("\nPress Enter to return to the admin menu...")

        elif admin_choice == "3":
            print("Goodbye!")
            quit()

        else:
            print("Invalid choice. Try again.")
