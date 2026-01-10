import csv
import os
#this class is for the ticket category
class Category:
    def __init__(self, category, code):
        self.category = category
        self.code = code
    def GetCode(self):
        return self.code
    def GetCategory(self):
        return self.category
#this class is for when the ticket are purchased
class Ticket:
    def __init__(self, category, topup, price):
        self.category = category
        self.topup = topup
        self.price = price
#this class stores all the purchases that have been purchased
class Customer:
    def __init__(self):
        self.purchases = []
    def buy_ticket(self, ticket):
        self.purchases.append(ticket)
        save_purchase(ticket)
# this adds a ticket to the customer's purchase history and saved it to a file
def save_purchase(ticket):
    file_exists = os.path.isfile("purchases.csv")
    with open("purchases.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Category", "Topup", "Price"])
        writer.writerow([ticket.category, ticket.topup, ticket.price])
# this loads all the ticket categories from the CSV file
def load_categories():
    listOfCatClasses = []
    listOfCategories = []
    code = 0
    #this reads the product data from the CSV file
    with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            category = lines['category_title']
            if category not in listOfCategories:
                listOfCategories.append(category)
                listOfCatClasses.append(Category(category, code))
                code += 1
    return listOfCatClasses
# this loads all the top-up options and prices for a chosen category
def load_topups(chosen_category):
    topup_options = []
    topup_price = []
    with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        #this collects all the top-ups that match the selected category for example for example adult single will be the numebr 1 option
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
    print("Error: Please enter either C or A.")
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
#shows if the category chosen exists
    try:
        choice = int(input("Enter your choice: "))
        chosen_category = listOfCatClasses[choice].GetCategory()
    except (ValueError, IndexError):
        print("An invalid category choice has been entered.")
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
        print("An invalid top-up choice has been entered.")
        quit()

    print("You picked:", chosen_topup)
    print(f"This ticket costs £{chosen_price:.2f}")#https://pythonguides.com/format-numbers-as-currency-in-python/
#this confirms that the ticket has been purchasd
    a = input("Would you like to purchase this ticket? (Y/N): ").upper()
    print("You entered", a)

    if a == 'Y':
        ticket = Ticket(chosen_category, chosen_topup, chosen_price)
        customer.buy_ticket(ticket)
        print(f"You have purchased a {chosen_topup} ticket. Your purchase has been saved.")
    else:
        print("You did not purchase a ticket. Have a good day!")

    quit()
#this is the code for the admin rights
else:
    while True:
        print("\nAdmin Menu")
        print("1. View all products")
        print("2. Edit a product price")
        print("3. Quit")

        admin_choice = input("Enter your choice: ")
#this displays all the products from the CSV file
        if admin_choice == "1":
            print("\n--- All Products ---")
            with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'r') as file:
                csvFile = csv.DictReader(file)
                for row in csvFile:
                    price = int(row['topup_price_in_pence']) / 100
                    print(f"{row['category_title']} - {row['topup_title']} - £{price:.2f}")#https://pythonguides.com/format-numbers-as-currency-in-python/

            input("\nPress enter to return to the admin menu...")
#this allows the admin to update the product price from the CSV file
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
                #this updates the price from pence to pounds
                products[choice]['topup_price_in_pence'] = str(int(new_price * 100))
#this changes the price to the new updated one
                with open('C:/Users/agbon/OneDrive - Nottingham Trent University/mobile_products.csv', 'w', newline='') as file:
                    fieldnames = products[0].keys()
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(products)

                print("The price has been successfully updated")

            except ValueError:
                print("An invalid input has been entered. Please enter numbers only.")
            except IndexError:
                print("The product number entered does not exist.")

            input("\nPress enter to return to the admin menu...")

        elif admin_choice == "3":
            print("Goodbye!")
            quit()

        else:
            print("This is an invalid choice. Please try again.")
