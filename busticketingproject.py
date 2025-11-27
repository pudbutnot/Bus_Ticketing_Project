import csv

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
with open('C:/Users/N1401842/Projects/BusTicketPurchaseProject/mobile_products.csv', mode = 'r')as file:
    csvFile = csv.DictReader(file)
    code = 0
    for lines in csvFile:
        category = lines ['category_title']
        if category not in listOfCategories:
            listOfCategories.append(category)
            listOfCodes.append(code)
            cat1 = Category(category, code)
            listOfCatClasses.append(cat1)
            #print("For" , cat1.GetCategory(), "enter", cat1.GetCode())
            code += 1
            
print("Please choose a category of ticket")
for cat in listOfCatClasses:
    print("For" , cat.GetCategory(), "enter", cat1.GetCode())
choice = int(input("Enter your choice: "))
print("you chose ", listOfCatClasses[choice].GetCategory())
#print(lines['category_title', "contains", lines['category_description'])


        
