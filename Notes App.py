import os


def getfile():
    filepath = input("\nEnter the file path where all your notes will be stored \n(make sure each slash is doubled): ")

    if not os.path.exists(filepath):
        print("\nFile path does not exist. Please try again.")
        return ""

    return filepath


def writefile(filename, description):
    note = open(filename, "w")
    note.write(description)
    note.close()


def addnote(filepath):
    title = (input("Enter the title of the note: "))
    description = input("Enter the contents of the note: ")

    if not title == "":
        title += ".txt"
        if not os.path.exists(filepath + title):
            writefile(filepath + title, description)
        else:
            inp = input("File already exists. Overwrite it? (y/n): ")
            if inp.lower() == "y":
                writefile(filepath + title, description)
            else:
                print("\n Canceled.")
                pass
    else:
        print("\nTitle cannot be empty.")


def listnotes(filepath):
    notes = []
    for filename in os.listdir(filepath):
        if filename.endswith(".txt"):
            notes.append(filename)

    return notes


def viewnote(filepath):
    notes = listnotes(filepath)

    for i, n in enumerate(notes):
        print(f"{i}: {n}")

    inp = input("\nEnter the index of the note to view: ")
    if inp.isdigit():
        inp = int(inp)
        if inp >= 0 and inp <= len(notes):
            note = notes[inp]
            filename = open(filepath + note, "r")
            for line in filename:
                line = line.strip()
                print(line)
            filename.close()
        else:
            print("\nInvalid index.")
    else:
        input("\nInvalid input. Please try again.")


def menu(file):
    print("\nWelcome to Notes++\n")
    print("1. Add a new note")
    print("2. View an existing note")
    print("3. Edit an existing note")
    print("4. Delete an existing note")
    print("5. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        addnote(file)
    if choice == "2":
        viewnote(file)


def runapp(filepath):
    while True:
        menu(file)


file = ""

while not os.path.exists(file):
    file = getfile()


runapp(file)
