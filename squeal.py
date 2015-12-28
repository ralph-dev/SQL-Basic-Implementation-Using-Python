from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results
first_element = 0
number_of_splits = 5
select_position = 1
from_position = 3
where_position = 5
many_tables = 2


def print_csv(table):
    '''(Table) -> NoneType
    Print a representation of table.
    '''
    dict_rep = table.get_dict()
    columns = list(dict_rep.keys())
    print(','.join(columns))
    rows = table.number_of_rows()
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))


def run_query(database, query):
    '''(Database, str) -> Table
    Return a Table object that represents the resulting table by
    taking a Database object and a string query as the parameters
    REQ: The Query must be in the proper format
    REQ: The Database must be a Dictionary
    REQ: The Database must contain the tables in the Query
    >>> run_query(read_database(),
    'select a.age,a.name,j.job from name,job where a.age>20')
    a.name,a.age,j.job
    Kevin,29,clerk
    Kevin,29,cashier
    Kevin,29,secretary
    Kevin,29,therapist
    >>> select a.age,a.name,j.job from name,job where a.age>9.2
    a.name,j.job,a.age
    Phillip,therapist,20
    Chris,secretary,20
    John,cashier,18
    Kevin,clerk,29
    Tyler,therapist,9.6
    George,secretary,19
    Jeremy,cashier,10.1
    Phillip,clerk,20
    Chris,therapist,20
    John,secretary,18
    Kevin,cashier,29
    Tyler,clerk,9.6
    George,therapist,19
    Jeremy,secretary,10.1
    Phillip,cashier,20
    Chris,clerk,20
    John,therapist,18
    Kevin,secretary,29
    Tyler,cashier,9.6
    George,clerk,19
    Jeremy,therapist,10.1
    Phillip,secretary,20
    Chris,cashier,20
    John,clerk,18
    Kevin,therapist,29
    Tyler,secretary,9.6
    George,cashier,19
    Jeremy,clerk,10.1
    '''
    final_table = Table()
    # Splits the query into a list of strings (tokens)
    tokens = query.split(' ', number_of_splits)
    # Grabs the columns specified after Select token
    columns = get_columns(tokens, select_position)
    # Grabs the tables specified after From token
    tables = get_tables(tokens, from_position)
    # Grabs the constraints after Where token
    constraints = get_constraints(tokens, where_position)
    # Create the Table
    final_table = database.column_pick(tables, first_element)
    # If there is more than two tables call cartesian product
    if (len(tables) >= many_tables):
        for i in range(1, len(tables)):
            table_two = database.column_pick(tables, i)
            final_table = cartesian_product(final_table, table_two)
    # If the Where token is in the query process the constraints
    if('where' in tokens):
        final_table = process_where_constraints(constraints, final_table)
    # Select and keep the columns that fit the query requirement
    final_table = database.select_columns(columns, tables)
    return final_table


def cartesian_product(table_one, table_two):
    '''(Table, Table) -> Table
    Return a table that is the product of two tables passed into the function.
    Each row in the first table is multiplied by the number of rows
    in the second table and vice versa
    REQ: Each Table must have its own Dictionary
    REQ: TableA and TableB must both have more than 0 rows
    REQ: Each Table must have an equivalent amount of completly filled rows
    REQ: The column names must be unique
    >>> d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
    >>> d2 = {'key_3': ['value_e', 'value_f'], 'key_4': ['value_g', 'value_h']}
    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(d1)
    >>> t2.set_dict(d2)
    >>> result_table = squeal.cartesian_product(t1, t2)
    >>> result_dict = result_table.get_dict()
    >>> expected_dict = {'key_1': ['value_a', 'value_a', 'value_b', 'value_b'],
                     'key_2': ['value_c', 'value_c', 'value_d', 'value_d'],
                     'key_3': ['value_e', 'value_f', 'value_e', 'value_f'],
                     'key_4': ['value_g', 'value_h', 'value_g', 'value_h']}
    >>> result_dict == expected_dict
    True
    >>> d1 = {'key_1': [], 'key_2': []}
    >>> d2 = {'key_3': [], 'key_4': []}
    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(d1)
    >>> t2.set_dict(d2)
    >>> result_table = squeal.cartesian_product(t1, t2)
    >>> result_dict = result_table.get_dict()
    >>> expected_dict = {'key_1': [], 'key_2': [], 'key_3': [], 'key_4': []}
    True
    '''
    # The list of tables is sent to cartesian product and
    # A Table object is returned
    final_table = table_one.cartesian_calculations(table_two)
    return final_table


def process_where_constraints(constraints, final_table):
    '''(list of str, Table) -> Table
    Return Table object after the intial table passed has been modified
    to fit the constraints in the query
    REQ: The Tables should have a dictionary
    REQ: The Tables should have Unique Column Names
    '''
    where_split_operand = ''
    where_split_cond_one = ''
    where_split_cond_two = ''
    # Loop through all the constraints
    for condition in constraints:
            # If the constraints has an equal sign then
            if ('=' in condition):
                # Split the constraint using the Equal sign
                query_split = condition.split('=')
                # Grab the first part of the condition
                where_split_cond_one = query_split[first_element]
                # Grab the second part of the condition
                where_split_cond_two = query_split[select_position]
                try:
                    where_split_cond_two = where_split_cond_two.strip("'")
                    where_split_cond_two = float(where_split_cond_two)
                except:
                    pass
                # Process the constraint using the
                # where_constraints_equal function
                final_table = final_table.where_constraints_equal(
                    where_split_cond_one, where_split_cond_two)
            # If the constraints has a Greather Than sign
            elif ('>' in condition):
                # Split the constraint using the Greater Than sign
                query_split = condition.split('>')
                # Grab the first part of the condition
                where_split_cond_one = query_split[first_element]
                # Grab the second part of the condition
                where_split_cond_two = query_split[select_position]
                try:
                    where_split_cond_two = where_split_cond_two.strip("'")
                    where_split_cond_two = float(where_split_cond_two)
                except:
                    pass
                # Process the constraint using the
                # where_constraints_greater function
                final_table = final_table.where_constraints_greater(
                    where_split_cond_one, where_split_cond_two)
    return final_table


def get_constraints(tokens, where_position):
    '''(List of str) -> List of str
    Return all the constraints specified after the Where token
    in the given query
    REQ: The tokens(Query) should be in the proper format
    '''
    constraints = []
    # If there is a where constraint that get the values
    if ('where' in tokens):
        # If there is more than one where constraint split by the comma
        if (',' in tokens[where_position]):
            constraints = tokens[where_position].split(',')
        else:
            constraints.append(tokens[where_position])
    return constraints


def get_tables(tokens, from_position):
    '''(List of str) -> List of str
    Return all the tables specified after the From token
    in the given query
    REQ: The tokens(Query) should be in the proper format
    '''
    tables = []
    if (',' in tokens[from_position]):
        tables = tokens[from_position].split(',')
    else:
        tables.append(tokens[from_position])
    return tables


def get_columns(tokens, select_position):
    '''(List of str) -> List of str
    Return all the columns specified after the Select token
    in the given query
    REQ: The tokens(Query) should be in the proper format
    '''
    columns = []
    # If there is more than one  column in query that break them into pieces
    if (',' in tokens[select_position]):
        columns = tokens[select_position].split(',')
    else:
        columns.append(tokens[select_position])
    return columns

if(__name__ == "__main__"):
    # Loop Controller
    loop_switch = True
    # Contiously ask for a query until a '' has been entered
    while(loop_switch):
        query = input("Enter a SQuEaL query, or hit enter to exit:")
        if(query != ''):
            print_csv(run_query(read_database(), query))
        else:
            loop_switch = False
