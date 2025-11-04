filePath = "C:\\Users\\acct6\\Downloads\\ExpenseLogger.txt"
file = open(filePath, "w")


def appendexpense(filename, expense, amount):
    file = open(filename, "a")
    file.write(f"\n{expense}: ${amount}")
    file.close()

def readexpense(filename):
    filename = open(filename, "r")
    for line in filename:
        line = line.strip()
        print(line.upper())
    filename.close()

def validate (expense, amount):
    check = 0

    if not expense.isalpha() and " " not in expense:
        print("Expense must contain only letters.")
    else:
        check += 1

    if amount.isdigit() or "." in amount:
        check += 1
    else:
        print("Invalid amount.")

    if check > 1:
        return True

while True:
    expense = input("\nEnter expense: ")
    amount = input("Enter amount: ")
    validated = validate(expense, amount)

    if validated:
        appendexpense(filePath, expense, amount)

    readexpense(filePath)


