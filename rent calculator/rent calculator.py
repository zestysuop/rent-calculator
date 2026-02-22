rent = int(input("Enter the monthly rent: "))
food = int(input("Enter the monthly food expenses: "))
electricity_spent = int(input("Enter the monthly electricity expenses: "))
charges_per_unit = int(input("Enter the electricity charges per unit: "))
persons = int(input("Enter the number of persons sharing the rent: "))
total_bill = rent + food + (electricity_spent * charges_per_unit)
bill_per_person = total_bill / persons
print("The total bill is: ", total_bill)
print("The bill per person is: ", bill_per_person)
