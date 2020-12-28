import database_functions as db
"""
[Create an app to creat, edit, retrieve and delete data using sqlite ]
"""

def menu_options(menu):
   
    """ Pull out all menu options or submenu options depending on menu parameter"""

    if menu == "main_menu":
        options = ["1. Work with databases", "2. Work with tables", "3. Work with data", "4. View queries", "5. Load files", "0. Exit"]
    elif menu == "databases":
        options = ["1. Create new database", "2. Modify database", "3. Drop database", "0. Back"]
    elif menu == "tables":
        options = ["1. Show tables", "2. Create new table", "3. Edit table",  "4. View data from table", "5. Drop table(s)", "0. Back"]
    elif menu == "insert":
        options = ["1. Insert data", "2. Update data", "3. Delete data", "0. Back"]
    elif menu == "views":
        options = ["1. View queries", "2. Create new query", "3. Drop query(s)", "0. Back"]
    elif menu == "files":
        options = ["1. Load file", "0. Back"]
        
    print()
    for choice in options:
        print(f"{choice}")
    print()
        
    choice = input("Please, Select an option: ")
    return choice
    
def task_todo(sub_menu_choice):
    """ Call out corresponding funtion for database, tables, view edtion or loading fiels according to option
    returns: function execution or or break the while loop
    """
    while True:
        task = menu_options(sub_menu_choice)
        if task == "0":
            break
        elif sub_menu_choice == "databases":
            db.database_tasks(task)
        elif sub_menu_choice == "tables":
            db.table_tasks(task)  
        elif sub_menu_choice == "views":
            db.view_query(task)  

def main():
    
    while True:
        print("\nWhat would You like to do next?")
        choice = menu_options("main_menu")
       
        if choice == "0":
            answer = input("Are you sure you want to exit? Please, enter Y/N\n")
            if answer:
                break
        elif choice == "1":
            # Go to database functions
            task_todo("databases") 
        elif choice == "2":
            # Work with tables
            task_todo("tables")  
        elif choice == "3":
            # Work with data
            task_todo("insert") 
        elif choice == "4":
            # Work with view
            task_todo("views")  
        elif choice == "5":
            # Load with files
            task_todo("files")  
            

if __name__== "__main__":

    main()