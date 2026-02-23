#list of all records
expense_records =[]
#tupel to store all details of each record
expense =()
#dictionary for total categories
category_totals ={}
#set for unique categories
unique_categories =set()

#loop to input 6 user expences:
n=1
print("Enter your expenses:\n")
while n<=6:
    category = input(f"\nEnter category for expense >{n}:(eg. 'food', 'transport', 'utilites' etc)> ")
    amount = float(input(f"Enter amount for expense($) >{n}:>"))
    date = input(f"Enter date for expense >{n}:(format: (2026-01-16)> ")

    #store these in tuple expense:
    expense = (category, amount, date)

    #append it to the list of expense record
    expense_records.append(expense)
    n += 1


#we are done with getting the date and now we need to scan it and manage the categories:

#we will loop through the expense recore and categorize the expenses:

highest_expense = None
lowest_expense = None

max_amount = 0
min_amount = float('inf')

for category,amount,date in expense_records:
    amount = float(amount)
    #it checks if the category is there if not then it adds it >>
    unique_categories.add(category)

    #now we need to add each category in the dictionary with its respected amount and
    #if it already exits then the amount will be add to the previous:
    category_totals[category] = category_totals.get(category,0) + amount


    #extracting the highest and lowest expense:
    if amount > max_amount:
        max_amount = amount
        highest_expense = ( category, amount, date)
    
    if amount < min_amount:
        min_amount = amount
        lowest_expense = ( category, amount, date)

# now extract all the amounts to a different list.
expense_amount = list(category_totals.values())

#now we will calculate total and average
total_expense = sum(expense_amount)

if len(expense_amount)>0:
    avg_expense = total_expense / len(expense_amount)

else:
    avg_expense = 0


#dictionary to store overall stats:

expense_stats = {
    "Total Spending": total_expense,
    "Average Expense": avg_expense,
    "Highest Expense": highest_expense,
    "Lowest Expense": lowest_expense
}



#time to print everything:

print(F"\n","="*5,"OVERALL SPENDING SUMMARY","="*5)
print(f"    TOTAL SPENDING: {total_expense}$")
print(f"    AVERAGE EXPENSE: {avg_expense}$")
print(f"    HIGHTEST EXPENSE: {highest_expense[1]}$---(CATEGORY: {highest_expense[0]},DATE: {highest_expense[2]})")
print(f"    LOWEST EXPENSE: {lowest_expense[1]}$---(CATEGORY: {lowest_expense[0]},DATE: {lowest_expense[2]})")




print(F"\n","="*5,"UNIQUE CATEGORIES SPENT ON","="*5)
print(" You have spent on the following categories:")
for i in unique_categories:
    print(  i)


print(F"   ","="*5,"SPENDING BY CATEGORY","="*5)
for key, value in category_totals.items():
    print(f"    {key}: {value}")    
