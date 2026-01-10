# BusTicketPurchaseProject
A bus ticketing purchase project
Use Case 1 Set up the category class.
Use Case 2 The customer selects a category, and the system loads all top-up options for that category.
Use Case 3 The system displays all top-up options and prices for the chosen category.
Use Case 4 The customer selects a top-up, and the system shows the price of the ticket.
Use Case 5 The customer confirms the purchase, and the system saves the ticket to the purchases file.
Use Case 6 The admin views all products, and the system displays every category, top-up and price.
Use Case 7 The admin edits a product price, and the system updates the CSV file with the new price.
The program uses functions to load categories from the CSV file.
It uses functions to load top-up options for the selected category.
It uses a function to save each purchase into the purchases file.
It uses classes to organise the data for categories, tickets and customers.
The category class stores the name and code for each category.
The ticket class stores the category, top-up name and price for each purchase.
The customer class stores all purchases made during the session.
The program reads product information from the mobile_products.csv file.
It automatically creates the purchases.csv file when the first purchase is made.
It appends each new purchase to the purchases file for future reference.
The customer flow includes choosing a category, choosing a top-up, viewing the price and confirming the purchase.
The admin flow includes viewing all products, selecting a product, entering a new price and saving the updated price.
The program continues to run the  admin menu until the admin chooses to quit.
The program ends after the customer completes or cancels their purchase.
This project demonstrates the use of classes, functions, file handling and user input validation.
It shows how the program can be used to manage both customer and admin tasks.
It provides a simple but effective ticket purchasing system using Python.
