# Copyright (c) 2006 Bermi Ferrer Martinez
#
# bermi a-t bermilabs - com
# See the end of this file for the free software, open source license (BSD-style).

from .languages.english import English
from .languages.spanish import Spanish


class Inflector(object):
    """
    Inflector for pluralizing and singularizing nouns.

    It provides methods for helping on creating programs
    based on naming conventions like on Ruby on Rails.
    """

    def __init__(self, language=English):
        assert callable(language), "language should be a callable obj"
        self._language = language()

    def pluralize(self, word):
        '''Pluralizes nouns.'''
        return self._language.pluralize(word)

    def singularize(self, word):
        '''Singularizes nouns.'''
        return self._language.singularize(word)

    def conditional_plural(self, number_of_records, word):
        '''Returns the plural form of a word if first parameter is
        greater than 1.
        '''
        return self._language.conditional_plural(number_of_records, word)

    def titleize(self, word, uppercase=''):
        '''Converts an underscored or CamelCase word into a sentence.
        The titleize function converts text like "WelcomePage",
        "welcome_page" or  "welcome page" to this "Welcome Page".
        If the "uppercase" parameter is set to 'first' it will only
        capitalize the first character of the title.
        '''
        return self._language.titleize(word, uppercase)

    def camelize(self, word):
        '''Returns given word as CamelCased.
        Converts a word like "send_email" to "SendEmail". It
        will remove non alphanumeric characters from the word, so
        "who's online" will be converted to "WhoSOnline"
        '''
        return self._language.camelize(word)

    def underscore(self, word):
        ''' Converts a word "into_it_s_underscored_version"
        Convert any "CamelCased" or "ordinary Word" into an
        "underscored_word".

        This can be really useful for creating friendly URLs.
        '''
        return self._language.underscore(word)

    def humanize(self, word, uppercase=''):
        '''Returns a human-readable string from word
        Returns a human-readable string from word, by replacing
        underscores with a space, and by upper-casing the initial
        character by default.

        If you need to uppercase all the words you just have to
        pass 'all' as a second parameter.
        '''
        return self._language.humanize(word, uppercase)

    def variablize(self, word):
        '''Same as camelize but first char is lowercased
        Converts a word like "send_email" to "sendEmail". It
        will remove non alphanumeric character from the word, so
        "who's online" will be converted to "whoSOnline"'''
        return self._language.variablize(word)

    def tableize(self, class_name):
        ''' Converts a class name to its table name according to rails
        naming conventions. Example. Converts "Person" to "people".
        '''
        return self._language.tableize(class_name)

    def classify(self, table_name):
        '''Converts a table name to its class name according to rails
        naming conventions. Example: Converts "people" to "Person"
        '''
        return self._language.classify(table_name)

    def ordinalize(self, number):
        '''Converts number to its ordinal form.
        This method converts 13 to 13th, 2 to 2nd ...
        '''
        return self._language.ordinalize(number)

    def unaccent(self, text):
        '''Transforms a string to its unaccented version.
        This might be useful for generating "friendly" URLs'''
        return self._language.unaccent(text)

    def urlize(self, text):
        '''Transform a string its unaccented and underscored
        version ready to be inserted in friendly URLs.
        '''
        return self._language.urlize(text)

    def demodulize(self, module_name):
        return self._language.demodulize(module_name)

    def modulize(self, module_description):
        return self._language.modulize(module_description)

    def foreign_key(self, class_name,
                    separate_class_name_and_id_with_underscore=1):
        ''' Returns class_name in underscored form, with "_id" tacked on at the end.
        This is for use in dealing with the database.
        '''
        return self._language.foreign_key(
            class_name,
            separate_class_name_and_id_with_underscore
        )

    def conditionalPlural(self, number_of_records, word):
        '''Deprecated, alias of #conditional_plural for backwards
        compatibility.
        '''
        return self.conditional_plural(number_of_records, word)

    def foreignKey(self, class_name, separate_class_name_and_id_with_underscore=1):
        '''Deprecated, alias of #foreign_key for backwards compatibility.'''
        return self.foreign_key(class_name,
                                separate_class_name_and_id_with_underscore)

# Copyright (c) 2006 Bermi Ferrer Martinez
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to deal in this software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of this software, and to permit
# persons to whom this software is furnished to do so, subject to the following
# condition:
#
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THIS SOFTWARE.