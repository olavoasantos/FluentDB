from configparser import ConfigParser


class Configuration(object):
    def __getattr__(self, item):
        return self.get(item)

    @staticmethod
    def get(section, filename='config.ini'):
        """
        Read database configuration file and return a dictionary object.
        :param section: section of configuration
        :param filename: name of the configuration file
        :return: a dictionary of database parameters
        """

        # Create parser and read configuration file
        parser = ConfigParser()
        parser.read(filename)

        # Get section variables
        dictionary = {}
        if parser.has_section(section):
            items = parser.items(section)

            for item in items:
                dictionary[item[0]] = item[1]
        else:
            raise Exception('{0} nor found in {1} file.').format(section, filename)

        return dictionary
