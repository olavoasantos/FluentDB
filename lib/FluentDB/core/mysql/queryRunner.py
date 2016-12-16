from .connection import MysqlConnection


class MysqlQueryRunner(object):
    # MySQL connection
    connection = None

    # MySQL cursor
    cursor = None

    def __init__(self, connection: MysqlConnection):
        self.connection = connection
        self.cursor = self.connection.cursor()

        pass

    def create(self, query):
        self.cursor.execute(query)
        self.close()

        pass

    def insert(self, query, values=""):
        self.cursor.execute(query, values)
        id = self.cursor.lastrowid
        self.connection.commit()

        return id

    def update(self, query, values=""):
        self.cursor.execute(query, values)
        self.connection.commit()

        pass

    def delete(self, query, values=""):
        self.cursor.execute(query, values)
        self.connection.commit()

        pass

    def all(self, query):
        self.cursor.execute(query)

        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(self.cursor.column_names, row)))

        return results

    def first(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchone()

        return results

    def many(self, query, size=10):
        self.cursor.execute(query)
        results = self.cursor.fetchmany(size)

        return results

    def close(self):
        self.cursor.close()
        self.connection.close()

        pass
