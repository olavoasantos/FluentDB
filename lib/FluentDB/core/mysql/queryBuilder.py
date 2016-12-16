class MysqlQueryBuilder(object):
    # Table name
    table = None

    # Selection
    selection = "*"

    # Restriction
    restriction = ""

    # Where
    Where = None

    # Order
    Order = None

    # Limit
    Limit = None

    # Action
    action = "SELECT {0} FROM {1}{2}"

    def build(self):
        self.buildRestrictions()

        return self.action.format(self.selection, self.table, self.restriction)

    def table(self, table):
        self.table = table

        return self

    def create(self, table, values):
        valHolder = []
        for i in values:
            valHolder.append('%s')

        return "INSERT INTO {0}({1}) VALUES({2})".format(table, ", ".join(values.keys()), ", ".join(valHolder))

    def update(self, table, columns, id):
        formatedColumns = list()
        for column in columns:
            formatedColumns.append("{0} = %s".format(column))

        return "UPDATE {0} SET {1} WHERE id = {2}".format(table, ", ".join(formatedColumns), id)

    def delete(self, table):
        return "DELETE FROM {0} WHERE id = %s".format(table)

    def select(self, *args):
        if len(args) > 1:
            self.selection = ",".join(args)
        elif len(args) == 1:
            self.selection = args[0]
        else:
            self.selection = "*"

        return self

    def buildRestrictions(self):
        if self.Where:
            self.restriction = " ".join((self.restriction, self.Where))
        if self.Order:
            self.restriction = " ".join((self.restriction, self.Order))
        if self.Limit:
            self.restriction = " ".join((self.restriction, self.Limit))

        pass

    def where(self, *args):
        if len(args) == 1:
            __ = "id={0}".format(args[0])
        elif len(args) == 2:
            if isinstance(args[1], str):
                __ = "{0}=\'{1}\'".format(args[0], args[1])
            else:
                __ = "{0}={1}".format(args[0], args[1])
        elif len(args) == 3:
            if isinstance(args[2], str):
                __ = "{0}{1}\'{2}\'".format(args[0], args[1], args[2])
            else:
                __ = "{0}{1}{2}".format(args[0], args[1], args[2])
        else:
            raise ValueError("Missing argument for where clause.")

        if self.Where:
            self.Where = "{0} AND {1}".format(self.Where, __)
        else:
            self.Where = "WHERE {0}".format(__)

        return self

    def orderBy(self, column, order="ASC"):
        self.Order = "ORDER BY {0} {1}".format(column, order)

        return self

    def limitBy(self, count, offset=None):
        if offset:
            vars = "{0}, {1}".format(offset, count)
        else:
            vars = count
        self.Limit = "LIMIT {0}".format(vars)

        return self
