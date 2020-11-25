import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    Drop database (sparkifydb) if exists, create a new one.
    :returns: The cursor and connection for (sparkifydb).
    '''
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    '''
    Drop tables based on sql_queries.py.
    :param cur: A cursor to perform database operations.
    :param conn: Connection to an existing database.
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
    Create tables based on sql_queries.py.
    :param cur: A cursor to perform database operations.
    :param conn: Connection to an existing database.
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    '''
    Drop the database, create a new one then create the tables based on sql_queries.py.
    '''
    cur, conn = create_database()
    
    # No need for droping all tables one by one, we already droping the whole database(sparkifydb) in previous function call line 21
    #drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()