class MysqlTableBuilder(object):
    # Table name
    name = None

    # Table columns
    table = list()

    def __init__(self, name):
        self.name = name

        pass

    # Add columns
    def increments(self, name):
        self.table.append("{0} INT NOT NULL AUTO_INCREMENT PRIMARY KEY".format(name))

        return self

    def bigIncrements(self, name):
        self.table.append("{0} BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY".format(name))

        return self

    def tinyInteger(self, name, size=None):
        self.addColumn("TINYINT", name, [size])

        return self

    def smallInteger(self, name, size=None):
        self.addColumn("SMALLINT", name, [size])

        return self

    def mediumInteger(self, name, size=None):
        self.addColumn("MEDIUMINT", name, [size])

        return self

    def integer(self, name, size=None):
        self.addColumn("INT", name, [size])

        return self

    def bigInteger(self, name, size=None):
        self.addColumn("BIGINT", name, [size])

        return self

    def float(self, name, size=None, decimal=None):
        self.addColumn("FLOAT", name, [size, decimal])

        return self

    def double(self, name, size=None, decimal=None):
        self.addColumn("DOUBLE", name, [size, decimal])

        return self

    def decimal(self, name, size=None, decimal=None):
        self.addColumn("DECIMAL", name, [size, decimal])

        return self

    def char(self, name, size=None):
        self.addColumn("CHAR", name, [size])

        return self

    def string(self, name, size=255):
        self.addColumn("VARCHAR", name, [size])

        return self

    def text(self, name):
        self.addColumn("TEXT", name, [65535])

        return self

    def tinyText(self, name):
        self.addColumn("TINYTEXT", name, [255])

        return self

    def mediumText(self, name):
        self.addColumn("MEDIUMTEXT", name, [16777215])

        return self

    def longText(self, name):
        self.addColumn("LONGTEXT", name, [4294967295])

        return self

    def timestamp(self, name):
        self.addColumn("TIMESTAMP", name, [])

        return self

    def timestamps(self):
        self.timestamp("created_at")
        self.timestamp("updated_at")

        return self

    def rawColumn(self, query):
        self.table.append(query)

    def check(self, column, operator, value):
        self.table.append("CHECK ({0}{1}{2})".format(column, operator, value))

        return self

    # Add constraints
    def unique(self):
        self.addConstraint("UNIQUE")

        return self

    def nullable(self):
        self.addConstraint("IS NULL")

        return self

    def notNull(self):
        self.addConstraint("NOT NULL")

        return self

    def default(self, value):
        self.addConstraint("DEFAULT {0}".format(value))

        return self

    def rawConstraint(self, query):
        self.addConstraint(query)

    # Helper functions
    def build(self):
        columns = ", ".join(self.table)

        return "CREATE TABLE {0} ({1})".format(self.name, columns)

    def addColumn(self, type, name, parameters=None):
        query = "{0} {1}".format(name, type)
        parameters = list(filter(None.__ne__, parameters))
        params = ""
        if len(parameters):
            params = "({0})".format(", ".join(str(x) for x in parameters))

        self.table.append("{0}{1}".format(query, params))

        pass

    def addConstraint(self, type):
        position = len(self.table) - 1
        column = self.table[position]
        self.table[position] = " ".join([column, type])

        pass
