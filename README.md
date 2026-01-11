# BusTicketPurchaseProject
A bus ticketing purchase project that allows customers to buy tickets and admins to view and edit product prices.
Use Case 1
Set up the category system. The program will load all ticket categories from the CSV file.
First step is to create the Category class. This will store the category name and a code number.
Next step is to write a function to read the CSV file and collect all unique categories.
I tested this by printing the categories to the screen. The result worked and all categories appeared correctly.

Extension: Add the Ticket and Customer classes.
The Ticket class will store the category, top-up and price.
The Customer class will store all purchases made during the session.
I tested this by creating a dummy ticket and saving it. The purchases.csv file was created automatically. This worked.

Use Case 2
The customer selects a category, and the system loads all top-up options for that category.

I added a function to read the CSV file again and collect all top-ups that match the chosen category.
I displayed these to the customer with numbers next to each option.
Test: I selected different categories and checked that the correct top-ups appeared. This worked.

Use Case 3
The system displays all top-up options and prices for the chosen category.

I converted the price from pence to pounds so it displays correctly.
Test: I checked several prices manually to make sure the conversion was correct. This worked.

Use Case 4
The customer selects a top-up, and the system shows the price of the ticket.

I added input validation so the program stops if the user enters an invalid number.
Test: I entered valid and invalid numbers. The valid ones worked and the invalid ones stopped the program with an error message. This worked.

Use Case 5
The customer confirms the purchase, and the system saves the ticket to the purchases file.

I added a confirmation step. If the customer enters Y, the ticket is saved.
Test: I bought several tickets. Each one was added to purchases.csv. This worked.

Use Case 6
The admin views all products, and the system displays every category, top-up and price.

I added an admin menu with an option to view all products.
The program reads the CSV file and prints every row.
Test: I checked that all products appeared correctly. This worked.

Use Case 7
The admin edits a product price, and the system updates the CSV file with the new price.

I added a menu option to edit prices. The admin selects a product and enters a new price.
The program converts the price back to pence and updates the CSV file.
Test: I changed several prices and checked the CSV file. The updates worked.

The program uses functions to load categories, load top-ups and save purchases.
It uses classes to organise the data for categories, tickets and customers.

The program reads product information from the mobile_products.csv file.
It automatically creates the purchases.csv file when the first purchase is made.
It appends each new purchase to the purchases file for future reference.

The customer flow includes choosing a category, choosing a top-up, viewing the price and confirming the purchase.
The admin flow includes viewing all products, selecting a product, entering a new price and saving the updated price.

The program continues to run the admin menu until the admin chooses to quit.
The program ends after the customer completes or cancels their purchase.

This project demonstrates the use of classes, functions, file handling and user input validation.
It shows how the program can be used to manage both customer and admin tasks.
It provides a simple but effective ticket purchasing system using Python.
