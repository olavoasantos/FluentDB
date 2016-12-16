from lib.FluentDB.core.FluentDB import FluentDB
from lib.FluentDB.helpers.decorator import decorate_all_functions, beforeAfterCall


@decorate_all_functions(beforeAfterCall)
class BaseModel(object):
    # Table name
    table = None

    # Model data
    __original = {}
    __attributes = {}

    # Secure data
    _secure = {'id', 'create_id'}
    __secure = {}

    # Visible fields
    __visible = {}

    # Hidden fields
    __hidden = {}

    def __init__(self, data={}):
        # Check table name
        if not self.table:
            raise AttributeError('Missing table name.')

        # Set secure fields
        self.setSecure()

        # Set model data
        self.setAttributes(data)
        self.setData(data)

        pass

    def setSecure(self):
        for key in self.__secure:
            self._secure.add(key)

        pass

    def setAttributes(self, data):
        for key in data.keys():
            isVisible = not bool(self.__visible) or key in self.__visible
            isNotHidden = key not in self.__hidden
            if isVisible and isNotHidden:
                setattr(self, key, data[key])

        pass

    def setData(self, data):
        for key in data.keys():
            self.__original[key] = data[key]
            self.__attributes[key] = data[key]

        pass

    def save(self):
        DB = FluentDB()
        isNotNew = bool(self.__original)

        try:
            if isNotNew:
                for key in self.__attributes:
                    if key not in self._secure:
                        self.__attributes[key] = getattr(self, key)
                    else:
                        self.__attributes[key] = self.__original[key]

                freshData = DB.table(self.table).where('id', self.__original['id']).update(self.__attributes)
            else:
                for key in self.__dict__:
                    if key not in self._secure:
                        self.__attributes[key] = getattr(self, key)

                freshData = DB.table(self.table).insert(self.__attributes)
                self.setData(freshData)

            self.setAttributes(freshData)

            return True
        except ValueError:
            return False

    def rollback(self):
        self.setAttributes(self.__original)
        self.save()

        return True

    def create(self, data):
        DB = FluentDB()

        try:
            freshData = DB.table(self.table).insert(data)
            self.setAttributes(freshData)
            self.setData(freshData)

            return True
        except ValueError:
            return False

    def delete(self):
        DB = FluentDB()

        try:
            DB.table(self.table).where('id', self.__original['id']).delete(self.__original['id'])

            del self

            return True
        except ValueError:
            return False

    def find(self, modelId):
        DB = FluentDB()

        try:
            data = DB.table(self.table).where('id', modelId).first(True)
            self.setAttributes(data)
            self.setData(data)

            return True
        except ValueError:

            return False

    def all(self):
        DB = FluentDB()

        try:
            return DB.table(self.table).get()
        except ValueError:
            raise SystemError('Could not fetch data from database.')

    def first(self):
        DB = FluentDB()

        try:
            data = DB.table(self.table).first(True)
            self.setAttributes(data)
            self.setData(data)

            return True
        except ValueError:
            raise SystemError('Could not fetch data from database.')
