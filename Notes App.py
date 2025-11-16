import os


def getfile():
    while True:
        filepath = input(
            "\nEnter the file path where all your notes will be stored \n(make sure each slash is doubled): ")

        if filepath != "" and not filepath.endswith("\\") and not filepath.endswith("/"):
            filepath += "\\"

        if not os.path.exists(filepath):
            print("\nFile path does not exist. Please try again.")
            continue

        return filepath


def writefile(filename, description):
    try:
        with open(filename, "w") as note:
            note.write(description)
    except Exception as e:
        print(f"error writing file{e}")


def appendfile(filename, description):
    try:
        with open(filename, "a") as note:
            note.write("\n" + description)
    except Exception as e:
        print(f"error appending file{e}")


def addnote(filepath):
    title = input("Enter the title of the note: ").strip()
    description = input("Enter the contents of the note: ")
    illegalchars = '\\/:*?"<>'

    if any(c in illegalchars for c in title):
        print("\nTitle contains illegal characters. Please try again.")
        return

    if title == "":
        print("\nTitle cannot be empty. Please try again.")
        return

    title += ".txt"
    filename = filepath + title

    if not os.path.exists(filepath + title):
        writefile(filepath + title, description)
    else:
        inp = input("File already exists. Overwrite it? (y/n): ")
        if inp.lower() == "y":
            writefile(filepath + title, description)
        else:
            print("\n Canceled.")
            pass


def listnotes(filepath):
    notes = []
    try:
        for filename in os.listdir(filepath):
            if filename.endswith(".txt"):
                notes.append(filename)
    except FileNotFoundError:
        print("\nFile does not exist. Please try again.")
        return []

    if not notes:
        print("\nNo notes found.")

    for i, n in enumerate(notes):
        print(f"{i}: {n}")

    return notes


def viewnote(filepath):
    notes = listnotes(filepath)
    if not notes:
        return

    inp = input("\nEnter the index of the note to view: ")
    if inp.isdigit():
        inp = int(inp)
        if 0 <= inp < len(notes):
            note = notes[inp]
            filename = filepath + note
            try:
                with open(filename, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line)
            except Exception as e:
                print(f"Error reading file{e}")
        else:
            print("\nInvalid index.")
    else:
        print("\nInvalid input. Please try again.")


def writeorappend(filepath):
    notes = listnotes(filepath)
    if not notes:
        return

    inp = input("\nEnter the index of the note to change: ")
    if inp.isdigit():
        inp = int(inp)
        if 0 <= inp < len(notes):
            note = notes[inp]
            filename = os.path.join(filepath, note)

            inp = input("\n Would you like to add(a) or overwrite(o): ").lower()
            if inp == "a":

                inp = input("\nEnter what you would like to add: ")
                appendfile(filename, inp)
            elif inp == "o":

                inp = input("\nEnter the new contents of the note: ")
                writefile(filename, inp)
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("\nInvalid index.")
    else:
        print("\nInvalid input. Please try again.")


def removenote(filepath):
    notes = listnotes(filepath)
    if not notes:
        return

    inp = input("\nEnter the index of the note to remove: ")
    if inp.isdigit():
        inp = int(inp)
        if 0 <= inp < len(notes):
            note = notes[inp]
            filename = os.path.join(filepath, note)

            inp = input("\n Would you like to delete this note? (y/n): ")
            if inp.lower() == "y":
                try:
                    os.remove(filename)
                    print(f"\nNote {filename} removed.")
                except FileNotFoundError:
                    print("\nFile does not exist. Please try again.")
                except PermissionError:
                    print("\nPermission denied. Please try again.")
                except Exception as e:
                    print(f"\nError deleting file{e}")
            else:
                print("Canceled.")
        else:
            print("\nInvalid index")
    else:
        print("\nInvalid input. Please try again.")

#
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
    if choice == "3":
        listnotes(file)
        writeorappend(file)
    if choice == "4":
        removenote(file)
    if choice == "5":
        exit()
    else:
        print("\nInvalid input. Please try again.")


def runapp(filepath):
    try:
        while True:
            menu(file)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()


file = getfile()
runapp(file)
