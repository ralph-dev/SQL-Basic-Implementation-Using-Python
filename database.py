class Table():

    '''A class to represent a SQuEaL table'''

    def __init__(self, new_dict=None):
        '''(Table) -> NoneType
        Create a new Table that contains columns and rows
        '''
        self._dictionary_table = new_dict

    def number_of_rows(self):
        '''(Table) -> int
        Return the amount of rows in a Table object.
        REQ: There must be a row that is not blank in the table
        '''
        self.num_rows_table = 0
        # Get the first column in the dictionary
        values = self._dictionary_table[list(self._dictionary_table.keys())[0]]
        # Loop through all the values in a column and add one to
        # Number of rows eveyr time a row is loope through
        for key in values:
            self.num_rows_table += 1
        return self.num_rows_table

    def multiply_rows(self, multiplier):
        '''(Table, int, int) -> NoneType
        Multiply the rows in a Table by the multiplier
        '''
        # Loop through every row in the table and multiply the
        # occurance of the row
        for key in self._dictionary_table:
            self._dictionary_table[key] *= multiplier

    def merge(self, table_one, table_two):
        '''(Table, Table, Table) -> NoneType
        Merges the two Table objects passed into one new Table object
        REQ: Column Names must be unique
        REQ: The row number must be consistent in one dictionary
        REQ: Tables have Dictionaries
        REQ: Both tables must have more than zero rows
        '''
        self._dictionary_table = dict(table_one.get_dict(),
                                      **table_two.get_dict())

    def where_constraints_greater(self, where_split_cond_one,
                                  where_split_cond_two):
        '''(Table, str, str, str) -> Table
        Return a Table after it has been modified to fit the constraint
        passed inside the query
        '''
        i = 0
        while i < self.number_of_rows():
            try:
                # Check which conditions where_split_cond_two fits into
                if("." not in where_split_cond_two and type(
                        where_split_cond_two) != float):
                    # Check which conditions where_split_cond_two fits into
                    if (self._dictionary_table[where_split_cond_one][i] <=
                            where_split_cond_two):
                        # Remember that index so we can remove it later
                        #  by adding it To list of indexs
                        self.rows_delete(i)
                        i -= 1
                # Check which conditions where_split_cond_two fits into
                elif("." in where_split_cond_two and type(
                        where_split_cond_two) != float):
                    # Compares the value of the dictionary to the constraint
                    if (self._dictionary_table[where_split_cond_one][i] <=
                            self._dictionary_table[where_split_cond_two][i]):
                        self.rows_delete(i)
                        i -= 1
                # Check which conditions where_split_cond_two fits into
                elif("." in where_split_cond_two and type(
                        float(self._dictionary_table[where_split_cond_one][i])
                        ) == float):
                    # Compares the value of the dictionary to the constraint
                    if (float(self._dictionary_table[where_split_cond_one]
                              [i]) <= float(
                            self._dictionary_table[where_split_cond_two][i])):
                        self.rows_delete(i)
                        i -= 1
            except:
                if(type(where_split_cond_two) != float):
                    # Compares the value of the dictionary to the constraint
                    if (self._dictionary_table[where_split_cond_one][i] <=
                            self._dictionary_table[where_split_cond_two][i]):
                        # Remember that index so we can remove it later
                        #  by adding it To list of indexes
                        self.rows_delete(i)
                        i -= 1
                else:
                    # If that value inside the column is false
                    if (float(self._dictionary_table[where_split_cond_one]
                              [i]) <= where_split_cond_two):
                        # Remember that index so we can remove it later
                        #  by adding it To list of indexs
                        self.rows_delete(i)
                        i -= 1
            i += 1
        # Now delete every row using the index at once
        return self

    def where_constraints_equal(self, where_split_cond_one,
                                where_split_cond_two):
        '''(Table, str, str, str) -> Table
        Return a Table after it has been modified to fit the constraint
        passed inside the query
        '''
        i = 0
        while i < self.number_of_rows():
            try:
                # Check which conditions where_split_cond_two fits into
                if("." not in where_split_cond_two and
                   type(where_split_cond_two) != float):
                    if (self._dictionary_table[where_split_cond_one][i] !=
                            where_split_cond_two):
                        # Remember that index so we can remove it later
                        #  by adding it To list of indexs
                        self.rows_delete(i)
                        i -= 1
                # Check which conditions where_split_cond_two fits into
                elif("." in where_split_cond_two and type(
                        where_split_cond_two) != float):
                    # Compares the value of the dictionary to the constraint
                    if (self._dictionary_table[where_split_cond_one][i] !=
                            self._dictionary_table[where_split_cond_two][i]):
                        self.rows_delete(i)
                        i -= 1
            except:
                if(type(where_split_cond_two) != float):
                    # Check which conditions where_split_cond_two fits into
                    if (self._dictionary_table[where_split_cond_one][i] !=
                            self._dictionary_table[where_split_cond_two][i]):
                        # Remember that index so we can remove it later
                        # by adding it To list of indexs
                        self.rows_delete(i)
                        i -= 1
                else:
                    # If that value inside the column is false
                    if (float(self._dictionary_table[where_split_cond_one]
                              [i]) != where_split_cond_two):
                        # Remember that index so we can remove it later
                        # by adding it To list of indexs
                        self.rows_delete(i)
                        i -= 1
            i += 1
        return self

    def rows_delete(self, index):
        '''(Table, list of int) -> NoneType
        Delete the whole row in the dictionary
        '''
        # through all every column in the table
        for i in self._dictionary_table.keys():
            # get rid of the value at that index
            self._dictionary_table[
                i].pop(-(len(self._dictionary_table[i])) + index)

    def select_specific_columns(self, dictionary_of_query, columns):
        '''(Table, dict, list of str) -> NoneType
        Edits the values of the dictionary
        '''
        # Loops through all the column names in the dictionary
        for column_header in self._dictionary_table:
            # If the query had a star for the column token use all the columns
            if ("*" in columns):
                dictionary_of_query[column_header] =\
                    self._dictionary_table[column_header]
            # If it didnt grab only the columns the query wanted
            else:
                if (column_header in columns):
                    # Attach the column data together in a new dictionary
                    dictionary_of_query[column_header] =\
                        self._dictionary_table[column_header]

    def cartesian_calculations(self, table_two):
        '''(Table, Table) -> Table
        Return a table where Each row in the first table is multiplied by
        the number of rows in the second table and vice versa
        REQ: Both Tables must have different column names
        '''
        # Creates a new table
        resulting_table = Table()
        # Gets the number of rows in the table
        num_rows_table_one = self.number_of_rows()
        num_rows_table_two = table_two.number_of_rows()
        # Multiplies the elements in both tables by the multiplier
        # self.multiply_rows(num_rows_table_two,0)
        a = {}
        for i in self._dictionary_table:
            a[i] = []
            for j in self._dictionary_table[i]:
                for v in range(num_rows_table_two):
                    a[i].append(j)
        self._dictionary_table = a
        table_two.multiply_rows(num_rows_table_one)
        # Mergers two Table objects together into a new Table object
        # To get the final result
        resulting_table.merge(self, table_two)
        return resulting_table

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self._dictionary_table = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._dictionary_table


class Database():

    '''A class to represent a SQuEaL database'''

    def __init__(self, new_dict=None):
        '''(Database) -> NoneType
        Create a new Table that contains columns and rows.
        '''
        self._database_table = new_dict

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self._database_table = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._database_table

    def column_pick(self, tables, column):
        '''(Database, list of str, int) -> Table
        Return a Table of the base table (First table after From Token)
        '''
        # Grab the first table from the list of tables and the database
        a_table = self._database_table[tables[column]]
        return a_table

    def select_columns(self, columns, tables):
        '''(Database, list of str, list of str) -> Table
        Return the dictionary that has all the columns that the query wants.
        '''
        dictionary_of_query = {}
        # Loop through all the table names in the database
        for table in self._database_table:
            # If the table name is being used in the query
            if (table in tables):
                column_in_table = self._database_table[table]
                column_in_table.select_specific_columns(dictionary_of_query,
                                                        columns)
        # Create a new Table object
        final_table = Table(dictionary_of_query)
        return final_table
