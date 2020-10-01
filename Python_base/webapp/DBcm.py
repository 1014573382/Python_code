# from builtins import Exception

import mysql.connector
class ConnectionError(Exception):
      pass

class CredentialsError(Exception):
      pass

class SQLError(Exception):
      pass


class UseDatabase:
      def __init__(self, config: dict) -> None:
            """Add the database configuration parameters to the object.

            This class expects a single dictionary argument which needs to assign
            the appropriate values to (at least) the following keys:

                host - the IP address of the host running MySQL/MariaDB.
                user - the MySQL/MariaDB username to use.
                password - the user's password.
                database - the name of the database to use.

            For more options, refer to the mysql-connector-python documentation.
            """
            self.configuration = config

      def __enter__(self) -> 'cursor':
            """Connect to database and create a DB cursor.

            Return the database cursor to the context manager.
            """
            try:
                  
                  self.conn = mysql.connector.connect(**self.configuration)
                  self.cursor = self.conn.cursor()
                  return self.cursor
            except mysql.connector.errors.InterfaceError as err:
                  raise ConnectionError(err)
            except mysql.connector.errors.ProgrammingError as err:
                  raise CredentialsError(err)

      def __exit__(self, exc_type, exc_value, exc_trace) -> None:
            """Destroy the cursor as well as the connection (after committing).
            """
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            if exc_type is mysql.connector.errors.ProgrammingError:
                  raise SQLError(exc_value)
            elif exc_type:
                  raise exc_type(exc_value)
      
