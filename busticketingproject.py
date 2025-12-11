import csv

greeting="""Welcome to the NCTX Buses App"""
print(greeting)
response=input("""Are you a customer or an admin?
Answer C for Customer and A for Admin: """)
print("You entered", response)
if response == 'C':
    print("Please choose a category of ticket")
else:
    quit()
class Category:
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
            
for idx, cat in enumerate(listOfCatClasses):
    print("For" , cat.GetCategory(), "enter", idx)
choice = int(input("Enter your choice: "))
chosen_category=listOfCatClasses[choice].GetCategory()
print("You picked:", chosen_category)
#print(lines['category_title', "contains", lines['category_description'])


print("Please choose a top-up type")
topup_options = []
with open('C:/Users/N1401842/OneDrive - Nottingham Trent University/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        if lines['category_title'] == chosen_category:
            topup_options.append(lines['topup_title'])
            
for idx, option in enumerate(topup_options):
    print("For", option, "enter", idx)
topup_choice= int(input("Enter your top_up choice: "))
print("You picked:", topup_options[topup_choice])

