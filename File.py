# File System Simulator using Menu

root = {}          # root directory
current = root     # current directory

while True:
    print("\n----- File System Menu -----")
    print("1. Create Folder (mkdir)")
    print("2. Create File (touch)")
    print("3. List Files (ls)")
    print("4. Change Directory (cd)")
    print("5. Delete File/Folder (rm)")
    print("6. Exit")

    choice = int(input("Select option: "))

    # Create Folder
    if choice == 1:
        name = input("Enter folder name: ")
        if name not in current:
            current[name] = {}
            print("# Folder created")
        else:
            print("# Folder already exists")

    # Create File
    elif choice == 2:
        name = input("Enter file name: ")
        if name not in current:
            current[name] = None
            print("# File created")
        else:
            print("# File already exists")

    # List files
    elif choice == 3:
        print("# Files/Folders in current directory:")
        for item in current:
            print(item)

    # Change directory
    elif choice == 4:
        name = input("Enter folder name: ")
        if name in current and isinstance(current[name], dict):
            current = current[name]
            print("# Moved into folder")
        else:
            print("# Folder not found")

    # Remove file or folder
    elif choice == 5:
        name = input("Enter file/folder name to delete: ")
        if name in current:
            del current[name]
            print("# Deleted successfully")
        else:
            print("# File/Folder not found")

    # Exit
    elif choice == 6:
        print("# Exiting File System Simulator")
        break

    else:
        print("# Invalid choice")