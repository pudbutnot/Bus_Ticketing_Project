import csv

greeting="""Welcome to the NCTX Buses App"""
print(greeting)

try:
    response=input("Are you a customer or an admin? (C/A):").upper()
    if response not in ['C' , 'A']:
        raise ValueError("You have entered an invalid input. Please enter either C or A")
except ValueError as e:
    print("Error:", e)
    quit()
finally:
    print("You have entered a valid input")
print("You entered", response)
if response == 'C':
    print("Please choose a category of ticket")
else:
    print("Admin menu")
    print("1. View all products")
    print("2. Edit a product price")
    print("3.Quit")

admin_choice= input("Enter your choice:")

if admin_choice= "1":
    print("\n--- All Products ---")
    with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        price=int(row['topup_price_in_pence']) /100
        print(f"{row['category_title'} - {row['topup_title']} - £{price:.2f}")
    quit()

elif admin_choice == "2":
    products[]
    with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        products.append(row)
    print("\n--- Select a product to edit ---")
    for idx, p in enumerate(products):
        prince=int(p['topup_price_in_pence']) /100
        print(f"{idx}. {p.['category_title']} - {p['topup_title']} - £{price:.2f}")
    try:
        choice=int(input("Enter product number:"))
        new_price= float(input("Enter new price (£):"))
        products[choice]['topup_price_in_pence']= str(int(new_price * 100))

        with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
            fieldnames= products[0].keys()
            writer=csv.DictWriter(file, fieldnames= fieldnames)
            writer.writeheader()
            writer.writerows(products)
        print("Price has been successfully updated")
    except ValueError:
        print(" An invalid input has been entered. Please enter numbers only.")
    except IndexError:
        print("The product number does not exist.")
    quit()
else:
    print("Goodbye!")
    quit()
        



    
class Category:
#this represents the ticket category like student or an adult ticket
    def __init__(self, category, code):
        self.category = category
        self.code = code
    def GetCode(self):
        return self.code
    def GetCategory(self):
        return self.category
    
listOfCatClasses = []
listOfCategories = []
listOfCodes = []
#uses the csv file to load each ticket categories
with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    code = 0
    for lines in csvFile:
        category = lines ['category_title']
        if category not in listOfCategories:
            listOfCategories.append(category)
            cat1 = Category(category, code)
            listOfCatClasses.append(cat1)
            #print("For" , cat1.GetCategory(), "enter", cat1.GetCode())
            code += 1
#this displays all the available categories with their index number for example 1 could be student tickets            
for idx, cat in enumerate(listOfCatClasses):
    print("For" , cat.GetCategory(), "enter", idx)
#this converts the input the user puts to get a chosen category
choice = int(input("Enter your choice: "))
chosen_category=listOfCatClasses[choice].GetCategory()
print("You picked:", chosen_category)
#print(lines['category_title', "contains", lines['category_description'])


print("Please choose a top-up type")
topup_options = []
topup_price = []
#this finds all the topup options that belongs to each category
with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        if lines['category_title'] == chosen_category:
            topup_options.append(lines['topup_title'])
            #this converts the price from pence to pounds
            price_in_pounds = int(lines['topup_price_in_pence'])/100
            topup_price.append(price_in_pounds)
            
for idx, option in enumerate(topup_options):
    print("For", option, "enter", idx)
topup_choice= int(input("Enter your top_up choice: "))
chosen_topup = topup_options[topup_choice]
chosen_price= topup_price[topup_choice]
print("You picked:", chosen_topup)
print(f"This ticket costs £{chosen_price: .2f}")#https://pythonguides.com/format-numbers-as-currency-in-python/
#ask the user if they want to buy the ticket
a= input("""Would you like to purchase this ticket?
Answer Y for Yes and N for No: """)
print( "You entered", a)
if a == 'Y':
    print(f"You have purchased a {chosen_topup} ticket.")

