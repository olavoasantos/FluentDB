from ..vendor.inflector.Inflector import Inflector
from ..helpers.configuration import Configuration as config
from datetime import datetime


class FluentDB(object):
    # Database driver
    driver = None

    # Credentials
    credentials = None

    # Database connection
    connection = None

    # Query runner
    execute = None

    # Query
    query = None

    # Query builder
    builder = None

    # Table maker
    tableScheme = None

    # Table name
    Table = None

    # Inflector
    inflector = Inflector()

    def __init__(self):
        # Set credentials
        self.credentials = {"host": config.get('database')["host"], "database": config.get('database')["database"],
                            "user": config.get('database')["user"], "password": config.get('database')["password"]}

        # Set driver
        self.driver = config.get('database')['driver']

        # Initiate database driver
        self.initiate()

        pass

    def initiate(self):
        """
        Initiates the database driver classes
        :return: None
        """

        if self.driver == "mysql":
            # Import MySQL drivers
            from .mysql.connection import MysqlConnection
            from .mysql.queryRunner import MysqlQueryRunner
            from .mysql.queryBuilder import MysqlQueryBuilder
            from .mysql.tableBuilder import MysqlTableBuilder

            # Initiate connection
            __ = MysqlConnection(self.credentials)
            self.connection = __.make()

            # Initiate query runner
            self.execute = MysqlQueryRunner(self.connection)

            # Initiate select query builder
            self.builder = MysqlQueryBuilder()

            # Initiate table builder
            self.tableScheme = MysqlTableBuilder
        else:
            raise ValueError("Database driver not found.")

        pass

    def get(self, returnData=False):
        """
        Builds and executes query to fetch data from database.
        :return:    MySQL query results
        """

        if self.query:
            query = self.query
        else:
            query = self.builder.build()

        if returnData:
            result = self.execute.all(query)
        else:
            result = []
            for row in self.execute.all(query):
                result.append(self.initializeModel(row))

        return result

    def insert(self, data):
        if self.Table:
            data['created_at'] = data['updated_at'] = datetime.now()
            query = self.builder.create(self.Table, data)
        else:
            raise ValueError("Table is not set.")

        data['id'] = self.execute.insert(query, list(data.values()))

        return data

    def first(self, returnData=False):
        if self.query:
            query = self.query
        else:
            query = self.builder.build()

        rows = self.execute.all(query)
        if returnData:
            result = rows[0]
        else:
            result = self.initializeModel(rows[0])

        return result

    def newTable(self, name):

        return self.tableScheme(name)

    def create(self, table):
        tableQuery = table.build()

        return self.execute.create(tableQuery)

    def delete(self, id):
        query = self.builder.delete(self.Table)

        self.execute.delete(query, [id])

        return True

    def update(self, data):
        columns = list()
        values = list()
        for column in data.keys():
            if column not in ('id'):
                columns.append(column)
                if column != 'updated_at':
                    values.append(data[column])
                else:
                    now = datetime.now()
                    data[column] = now
                    values.append(now)

        if self.Table:
            query = self.builder.update(self.Table, columns, data['id'])
        else:
            raise ValueError("Table is not set.")

        self.execute.update(query, values)

        return data

    def raw(self, query):
        """
        Sometimes you may need to use a raw expression in a query.
        :param      query:  STR MySQL expression
        :return:    self
        """

        self.query = query

        return self

    # Wrapper around database driver
    def limitBy(self, limit, offset=None):
        """
        Sets the limit and offset for a query.
        :param      limit:   INT Limit of rows to be fetched
        :param      offset:  INT Offset of the first row to return
        :return:    self
        """

        self.builder.limitBy(limit, offset)

        return self

    def orderBy(self, column, order="ASC"):
        """
        Sort the result of the query by a given column.
        :param      column:  STR Column name
        :param      order:   STR Direction of the sort and may be either (ASC | DESC)
        :return:    self
        """

        self.builder.orderBy(column, order)

        return self

    def where(self, *args):
        """
        Add where clauses to the query.
        :param      args:   Single arg      Adds a clause to search for an entry with a given id (e.g. .where(3) -> WHERE id=3)
                                            :arg1   INT Sets id
                            Two args        Adds a clause to search for an entry with a given column and a given value (e.g. .where('name', 'Newton') -> WHERE name='Newton')
                                            :arg1   STR     Column name
                                            :arg2   STR/INT Value
                            Three args      Adds a clause to search for an entry with a given column, an operator and a given value (e.g. .where('name', '<>', 'Newton') -> WHERE name<>'Newton')
                                            :arg1   STR     Column name
                                            :arg2   STR     MySQL operator
                                            :arg3   STR/INT Value
        :return:    self
        """

        self.builder.where(*args)

        return self

    def table(self, name):
        """
        Sets the table name to the query.
        :param      table:  STR Table name
        :return:    self
        """

        self.Table = name
        self.builder.table(name)

        return self

    def select(self, *columns):
        """
        Specify a custom select clause for the query.
        :param      columns:    STR Multiple arguments each with a column name (defaults to "*")
        :return:    self
        """

        self.builder.select(*columns)

        return self

    def initializeModel(self, data):
        try:
            modelName = '{0}Model'.format(self.inflector.singularize(self.Table).capitalize())
            Model = getattr(__import__('models.{0}'.format(modelName)), modelName)
        except AttributeError and ImportError:
            from ..model.BaseModel import BaseModel as Model
            Model.table = self.Table

        return Model(data)
