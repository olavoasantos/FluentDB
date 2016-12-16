import mysql.connector
from mysql.connector import Error, errorcode


class MysqlConnection(object):
    credentials = None

    def __init__(self, credentials):
        self.credentials = credentials

        pass

    def make(self):
        """
        Establish MySQL database.
        :return: mysql.database object
        """

        try:
            if self.credentials is None:
                raise ValueError("Missing credentials!")

            return mysql.connector.connect(**self.credentials)

        except Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError('Something is wrong with your user name or password')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                raise ValueError(e)
