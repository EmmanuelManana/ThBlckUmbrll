import pyodbc

for driver in pyodbc.drivers():
    print(driver)

# define server name, drive and database name
server = 'DESKTOP-4L29225\SQLEXPRESS'
database = 'ThBlkUmbrll'
driver = 'ODBC Driver 17 for SQL Server'

class Database:

    def __init__(self):
        self.__conn = pyodbc.connect('DRIVER={'+driver+'}; \
                            SERVER=' + server + '; \
                            DATABASE=' + database + ';\
                            Trusted_Connection=yes;')

    def get_connection(self):
        return self.conn
        
    def close_conn(self):
        self.conn.close()

    def write_query(self, sql_query, params=None):
        """ execute an sql query.

        Args:
            sql_query: string. a string representing the sql query
            params: tuple(optional). the values if any to be executed by the sql_query

        returns:
            writes to the db
        """
        cursor = self.__conn.cursor()
        if params:
            cursor.execute(sql_query, params)
            cursor.commit()
        else:
            cursor.execute(sql_query)
            cursor.commit()
            
    def fetch_query(self, sql_query, params=None):
        """ execute an sql query.

        Args:
            sql_query: string. a string representing the sql query
            params: tuple(optional). the values if any to be executed by the sql_query

        returns:
            request: tuple. the query result 
        """
        cursor = self.__conn.cursor()
        if params:
            cursor.execute(sql_query, params)
            request = cursor.fetchall()
            return request
        else:
            cursor.execute(sql_query)
            request = cursor.fetchall()
            return request
