from lib.FluentDB.core.FluentDB import FluentDB
from models.UserModel import UserModel
import hashlib

if __name__ == '__main__':
    # Create Users table
    # DB = FluentDB()
    # table = DB.newTable('users')
    # table.increments('id')
    # table.timestamps()
    # table.string('email').unique()
    # table.string('password')
    # DB.create(table)

    # Insert new User
    # # 1. From UserModel
    # User = UserModel()
    # User.email = 'john@example.com'
    # User.password = 'password123'
    # User.save()

    # # 2. From FluentDB
    # DB = FluentDB()
    # data = {
    #     'email': '',
    #     'password': hashlib.sha256('john@example.com'.encode('utf-8')).hexdigest()
    # }
    # DB.table('users').insert(data)

    # Fetch data from database
    # # 1. From UserModel
    User = UserModel()
    User.first()
    User.name = 'John'
    User.save()
    print(User.__dict__)
    # # 2. From FluentDB
    # DB = FluentDB()
    # Users = DB.table('users').get()
