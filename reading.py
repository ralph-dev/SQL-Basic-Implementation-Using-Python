# Functions for reading tables and databases

import glob
from database import *

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
file_list = glob.glob('*.csv')


def read_database():
    '''() -> Database
    Return the Database (dictionary) representation of this table. The
    dictionary keys will be the Table Names, and the list will
    contain the table data for that column.
    REQ: Database should have a dictionary
    REQ: No two table names can be the same
    '''
    table = []
    # For every csv file in the same directory
    for element in file_list:
        # Create the table for the files by reading each file one by one
        table.append((read_table(element)))
    i = 0
    # For every csv file in the same directory
    for element in file_list:
        # Remove the .csv extension
        file_list[i] = element.replace(".csv", "")
        i += 1
    i = 0
    # Create the database dictionary
    database = {}
    # For everyone csv file that doesnt have the csv extension anymore
    for element in file_list:
        # Make the key the name of the file and the value the table we created
        database[element] = table[i]
        i += 1
    # Create a new Database Object
    new_database = Database(database)
    return new_database


def read_table(filename):
    '''(str) -> Table
    Return the Table (dictionary) representation of this table. The
    dictionary keys will be the column names, and the list will
    contain the values for that column.
    REQ: Table must have a dictionary
    REQ: Column names must be unique
    '''
    # Open the csv file
    if (".csv" not in filename):
        filename = filename + ".csv"
    with open(filename, "r") as function:
        # Read the first line of the file to get the headers
        line = function.readline().strip()
        # Split the line based on the commas to get each header into one list
        header = line.split(",")
        value = []
        list_holder = []
        number_of_rows = 0
        # Finds how many rows are in the file.
        for values in function:
            number_of_rows += 1
        # Loop for as many columns there are
        for i in range(0, len(header)):
            # Starting reading the file from the first line
            function.seek(0)
            # Skip the first line
            next(function)
            # Reset the list
            list_holder = []
            # For each line in the file
            for values in function:
                # Clear the trailing white space
                valued = values.strip()
                # Ignore blank lines
                if (valued != ""):
                    # Split the line and get the elements individuall
                    currentline = valued.split(",")
                    # Add the elements of the i column into a list
                    list_holder.append(currentline[i].strip())
            # Add the list with all the items in column i to the main list
            value.append(list_holder)
        dictionary_one = {}
        i = 0
        # Loop through all the headers
        for headers in header:
            # Set the values of the header key to the columns data
            dictionary_one[headers] = value[i]
            i += 1
    # Create a new Table object
    new_table = Table(dictionary_one)
    return new_table
