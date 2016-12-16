# ModelBase
# -----------------------------------------------------------------------------------------
# This is the generic Model which your custom model will inherit from.
#
# @mod  !required
#
from lib.FluentDB.model import BaseModel

# decorate_all_functions, beforeAfterCall
# -----------------------------------------------------------------------------------------
# Wrapper functions which are called before and after a method is triggered. As an example,
# upon calling UserModel.save(), the system will call UserModel.beforeSave()
# before saving and UserModel.afterSave() after saving.
#
# @mod  !optional
#
from lib.FluentDB.helpers.decorator import decorate_all_functions, beforeAfterCall

# hashlib (https://docs.python.org/2/library/hashlib.html)
# -----------------------------------------------------------------------------------------
# This module implements a common interface to many different secure hash and message
# digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224,
# SHA256, SHA384, and SHA512 (defined in FIPS 180-2) as well as RSA’s
# MD5 algorithm (defined in Internet RFC 1321).
#
# @mod  !optional
#
import hashlib


# Only use this if using beforeAfterCall.
@decorate_all_functions(beforeAfterCall)
class UserModel(BaseModel):
    """
    UserModel
    -------------------------------------------------------------------------------------------
    Model related to the 'users' table. This is an example of model. Modify this as you wish.
    Each database table should have a corresponding "Model" which is used to interact with
    that table. Models allow you to query for data in your tables, as well as insert new
    records in them. As a convention, all models must be placed within the ./models
    directory on the projects main folder. Also, both the model's file and the
    the model's class should be named using '{Singular database name}Model'
    (e.g. db name = 'users' => file name = class name = 'UserModel').
    """

    # *
    # The table associated with the model.
    #
    # @var string   !Required
    # **
    table = 'users'

    # *
    # The attributes that should be hidden from the model.
    #
    # @var dict (default) {}
    # **
    __hidden = {}

    # *
    # The attributes that should be visible in the model. If is empty,
    # the model will shows all which are not listed in __hidden.
    #
    # @var  dict    !optional  (default)    {}
    # **
    __visible = {}

    # *
    # The attributes that should not be modified in the model.
    #
    # @var dict    !optional  (default)    {}
    # **
    __secure = {}

    # *
    # beforeSave(*args)
    # -----------------------------------------------------------------------------------------
    # This is an example use of a beforeAfterCall function that is called before saving a
    # model. Before persisting the data to the database, the password is hashed. This
    # is an optional method.
    # **
    def beforeSave(*args):
        """
        Function called before executing self.save(). It hashes the 'password' attribute.
        args[0] represents 'self' object.

        :param args:    Mixed
        :return: pass
        """
        args[0].password = args[0].hash(args[0].password)

        pass

    # *
    # hash(string)
    # -----------------------------------------------------------------------------------------
    # Hashes a given string using SHA256 algorithm. This is an optional method but good for
    # password security.
    # **
    @staticmethod
    def hash(string):
        """
        It Hashes a given string using SHA256 algorithm.

        :param string:  str
        :return: str
        """
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
