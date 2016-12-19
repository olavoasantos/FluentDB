# FluentDB
### Fluent database interface for python
This is an attempt to make database management with Python more fluid and intuitive. By wrapping the database modules within custom functions, we can standardize the different types of queries for a cleaner and easier workflow.

#### Limitations

- Python version:
    - Works with Python 3.x (tested with 3.5.2)
- Database drive:
    - The only driver available is [MySQL.connector](https://github.com/sanpingz/mysql-connector)
    - Implementation of abstract classes (still in the TODOs list) will make it easier to create new drivers for other database modules

#### Dependencies
These packages are required for FluentDB to work:

1. [Python 3.x](https://www.python.org/)
2. [MySQL.connector](https://github.com/sanpingz/mysql-connector)

#### Installation
1. Pull in the package
2. Create a `config.ini` file in the project's main folder
3. Add the following variables to the `config.ini` file:
```ini
[database]
driver=mysql
host={DB_HOST}
database={DB_DATABASE}
user={DB_USERNAME}
password={DB_PASSWORD}
```
Have fun! 

#### Vendor scripts
These packages are included out of the box. Check out the links for details on documentations:

1. [Python Inflector](https://github.com/ixmatus/inflector)

#### Examples of use

##### Create table

```python
from lib.FluentDB.core.FluentDB import FluentDB

if __name__ == '__main__':
    # Create Users table
    DB = FluentDB()
    table = DB.newTable('users')
    table.increments('id')
    table.timestamps()
    table.string('email').unique()
    table.string('password')
    DB.create(table)

```

For data manipulation, such as inserting or fetching data, we could use either FluentDB Models or raw FluentDB queries.

##### Inserting data


```python
from lib.FluentDB.core.FluentDB import FluentDB
from models.UserModel import UserModel
import hashlib

if __name__ == '__main__':
    # Insert new User
    # # 1. Using a FluidDB Model (UserModel)
    User = UserModel()
    User.email = 'john@example.com'
    User.password = 'password123'
    User.save()

    # # 2. Using raw FluentDB query
    DB = FluentDB()
    data = {
        'email': 'john@example.com',
        'password': hashlib.sha256('password123'.encode('utf-8')).hexdigest()
    }
    DB.table('users').insert(data)

```

##### Fetching data

```python
from lib.FluentDB.core.FluentDB import FluentDB
from models.UserModel import UserModel

if __name__ == '__main__':
    # Fetch data from database
    # # 1. Using a FluentDB Model (UserModel)
    # # # Fetching all users
    User = UserModel()
    Users = User.all()
    
    # # # Fetching user with ID of 1
    User = UserModel()
    User.find(1)
    
    # # 2. Using raw FluentDB query
    # # # Fetching all users
    DB = FluentDB()
    Users = DB.table('users').get()
    
    # # # Fetching user with ID of 1
    DB = FluentDB()
    User = DB.table('users').where('id', 1).first()

```

#### To do's
##### Coding fun
- [ ] Refactor MySQL Query Builder
- [ ] Create DB Drive interface

##### Docs
- [ ] Method doc blocks
- [ ] Models doc blocks
- [ ] Models docs
- [ ] Fetch data docs
- [ ] Insert data docs
- [ ] Update data docs
- [ ] Delete data docs
- [ ] Create table docs
