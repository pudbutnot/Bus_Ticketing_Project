# BusTicketPurchaseProject
Use Case 1
I set up the category system by creating the Category class and writing the function that loads all categories from the CSV file. The program reads the file, collects the unique categories and displays them to the customer. I tested this by running the program and checking that the categories appeared correctly.

Use Case 2
The customer selects a category, and the system loads all top-up options for that category. I wrote the function that reads the CSV file again and finds all matching top-ups. I tested this by choosing different categories and confirming that the correct top-ups were shown.

Use Case 3
The system displays all top-up options and prices for the chosen category. I converted the prices from pence to pounds so they display properly. I tested this by checking the printed prices, and they were correct.

Use Case 4
The customer selects a top-up, and the system shows the price of the ticket. I added input validation so the program stops if the user enters an invalid number. I tested this by entering valid and invalid inputs, and the behaviour matched what I expected.

Use Case 5
The customer confirms the purchase, and the system saves the ticket to the purchase file. The program creates a Ticket object and writes the purchase to purchases.csv. I tested this by buying several tickets and checking that the file updated correctly.
Use Case 6
The admin views all products, and the system displays every category, top-up and price. The program reads the CSV file and prints each product. I tested this and confirmed that all products appeared as expected.

Use Case 7
The admin edits a product price, and the system updates the CSV file with the new price. The admin selects a product, enters a new price, and the program writes the updated value back to the file. I tested this by changing prices and checking the CSV file to confirm the update.

The program uses functions to load categories, load top-ups, and save purchases. It uses classes to organise the data for categories, tickets and customers. The program reads product information from the mobile_products.csv file and creates the purchases.csv  file automatically when the first purchase is made. It appends each new purchase to the file for future reference.

The customer flow includes choosing a category, choosing a top-up, viewing the price and confirming the purchase. The admin flow includes viewing all products, selecting a product, entering a new price and saving the updated price. The program continues to run the admin menu until the admin chooses to quit. The program ends after the customer completes or cancels their purchase.

This project demonstrates the use of classes, functions, file handling and user input validation. It provides a simple and effective ticket purchasing system using Python.
