import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    create a database connection to an SQLite database
    :param db_file: database file
    :return: Connection object of None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        # print(sqlite3.version)
        return connection
    except Error as e:
        print(e)

    return connection
    # finally:
    #     if connection:
    #         connection.close()

def create_table(connection,create_table_sql):
    """
    create a table from the create_table_sql statement
    :param connection: connection object
    :param create_table_sql: a CREATE TABLE SQL statement
    :return:
    """

    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"sqliteexample.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
    #create a database connection
    connection = create_connection(database)

    # create tables
    if connection is not None:
        # create projects table
        create_table(connection, sql_create_projects_table)

        #create tasks table
        create_table(connection, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
    main()