import csv

print("Welcome to the NCTX Buses App")
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
            
print("Please choose a category of ticket")
for idx, cat in enumerate(listOfCatClasses):
    print("For" , cat.GetCategory(), "enter", idx)
choice = int(input("Enter your choice: "))
print("You picked:", listOfCatClasses[choice].GetCategory())
#print(lines['category_title', "contains", lines['category_description'])


  
