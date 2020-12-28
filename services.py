import sqlite3
from sqlite3 import Error

# Connexion function
def db_connection(db_file):
    """ create database connection to a database
    :param db_file: database file name
    :return: Connection object or None
    """
    conn = None
    try:
        #conn = sqlite3.connect(db_file)
        # create a temporarly database in memory
        conn = sqlite3.connect(db_file)
        print(f"{db_file} is ready to use.\n")
        return conn
    except Error as err:
        print(err)
    
    return conn

def close_connection(conn):
    """ close database connection to students_db
    """
    return conn.close()

# Database related functions
def database_tasks(task):

    database = input("Please, enter the name of the new database: \n")
    # create a database connection
    con = db_connection(database)
    if task == "1":
        if con:
            print(f"{database} was successfully created")
    elif task == "2":
        print("In order to modify/edit/delete tables go to table section")
    elif task == "3":
        if delete_db(con, database):
            print(f"{database} was successfully deleted")
    close_connection(con)

def delete_db(conn, database):
    """ Drop selected database
    :param table_name: 
    :return: 
    """
    import os

    if os.path.exists(database):
        os.remove(database)
        print(f"{database} successfully deleted!")
    else:
        print("The database does not exist")  

# Tables related  functions
def table_tasks(task):
    """Perform task on selected table.
    Args:
        task ([str]): [option to perform corresponding function]
    """
    database = input("Please, enter the name of the database: \n")
    # create a database connection
    con = db_connection(database)
    
    if task == "1":
        show_tables(con, database)
    elif task == "2":
        create_table(con)
    elif task == "3":
        modify_table(con, database)
    elif task == "4":
        print("View data from Table ****")
    elif task == "5":
        drop_table(con, database)

def show_tables(conn, dtbase):
    """ Select all tables from selected database
    :param table_name: string 
    :return: selected table
    """
    try:
        c = conn.cursor()
        c.execute('SELECT name from sqlite_master where type= "table"')
        print(f"{dtbase} has following tables: \n")
        # all tables get a number
        table_list = enumerate(c.fetchall(), 1)
        tb = []
        for number, table in table_list:
            if number:
                print(f"{number}.", *table)
                tb.append((number, table))
            else: 
                print("Unfortunately there is no table.")
                break
        return tb
    except Error as err:
        print("\n! ",  err,". Please, try it again.")

def create_table(conn):
    """ create a table in database
    :param table_name: 
    :return: 
    """
    sql_insert = 'CREATE TABLE'
    table_fields = ''

    # Insert data to create tables
    table_name = input("Please enter the name of the table: ")
    number_fields = input("Please insert the nr. of fields: ")
    fields = [input(f"Enter the name of field {f+1}? ") for f in range(int(number_fields))]
    datatypes = [input(f"Insert datatypes for {f}: ").upper() for f in fields]

    # Format field and datatype for sql sentence
    pair = [f + ' ' + d for f, d in zip(fields, datatypes)]
    separator = ', '
    table_fields += separator.join(pair)
    sql_insert += " " + table_name + "(" + table_fields + ")"      

    print(sql_insert, "\n")
    # Commit insert table query
    try:
        c = conn.cursor()
        c.execute(sql_insert)
        conn.commit()
        print(sql_insert + "; committed")
    except Error as err:
        print("\n!" + err +". Please, try it again.")

def drop_table(conn, dtbase):
    """[Delete selected table]

    Args:
        conn ([ojb]): [connextion to database]
    """
    sql_drop = "Drop table if exists "
    #Show tables to choose
    tables = show_tables(conn, dtbase)
    table_number = int(input("\nWhich table would you like to delete? ")) 
    # Add table to string sql to drop
    for number, table in tables:
        if number == table_number: 
            sql_drop = "Drop table if exists " + table[0] + ";"
    try:
        c = conn.cursor()
        c.execute(sql_drop) 
        print(f"\n Table was succesfully removed!\n")     
    except Error as err:
        print("\n! ",  err,". Please, try it again.")
      
def modify_table(conn, dtbase):
    """Modifies selected table.
    Args:
        conn ([obj]): [connection with database ]
        dtbase([obj]): [Name of selected database]
    """
    # Choose what to do with table
    print(">> Please, keep in mind, SQLite >ALTER TABLE<-statement can only perform 3 actions.")
    print("Which action would you like to perform?\n")
    action = input("- Rename table\n- Add new column\n- Rename a column\n\nChoose an action please: ").lower()
    show_tables(conn, dtbase)
    
    # Insert data to mofidy tables
    table_name = input("Which table should be edited?\n")

    if action == "rename":
        name = input("What is the new name?\n")
        sql_rename = "Alter table " + name + ";"
        print(sql_rename)
    elif action == "add":
        number_columns = input(f"Please insert the nr. of columns to be added: ")
        fields = [input(f"Enter the name of field(s)? ") for f in range(int(number_fields))]
        datatypes = [input(f"Insert values for {f}: ").upper() for f in fields]
        # Format field and datatype for sql sentence
        pair = [f + ' ' + d for f, d in zip(fields, datatypes)]
        separator = ', '
        fields += separator.join(pair)
        sql_add += " " + table_name + "(" + fields + ")" 
        print(sql_add)   
       
    elif action == "rename":
        sql_insert = "Rename INTO"
    else:
        print("Going back!") 
        return None
   


# Views and Queries related functions
def view_query(conn, table):
    """ Select data from table
    :param table_name: 
    :return: 
    """

    #sql_select = 'SELECT'
    show_tb = 'SHOW COLUMNS FROM '
    # Select table and columns
    name_tb = input("Please, the name of the table: ")
    t = show_tb + name_tb
    print(show_tb)
