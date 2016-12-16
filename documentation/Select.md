### FluentDB
# Fetching Data

Lets say we have a `users` table with some entries, as follows:

| id  | created_at  | updated_at  | email  | password  |
|-----|-------------|-------------|--------|-----------|
| 1   | 06-May-2009 16:40:04  | 04-Nov-2010 18:24:40  | john@example.com  |  7fae8c79b45a1690a5adf37c7dc108de8698fe38 |
| 2   | 11-Oct-2010 22:30:43  | 07-Oct-2016 14:12:21  | jane@example.com  |  67c03a024140ae827db19dc6ab0a32b6228d5462 |
| 3   | 07-Jan-2018 10:34:59  | 29-May-2035 15:07:04  | jeff@example.com  |  97e3f719a38bd05a8ff4e7ddd1a211d6731fc2a1 |

#### Initializing module
First we need to instantiate FluentDB: 
```python
from lib.FluentDB.core import FluentDB


if __name__ == "__main__":
    # Instantiates FluentDB class and initiates the database driver 
    DB = FluentDB()
```

Now that we have instantiated and initialized the database driver, we can start interacting with the database.

#### .table(name)
To begin a fluent query against a database, we can select a table by using.

```python
""" DB.table({TABLE NAME}) """
    DB.table("users")
```

#### .select(*args)
To run a select statement against the database you can use the `select()` methods with the arguments being the selected column names. It defaults to `"*"`.

```python
""" DB.select({COLUMN NAME}, ... : defaults to "*") """
    DB.select() # SELECT *
    DB.select("email", "password") # SELECT email, password
    DB.select("email AS E-mail", "password") # SELECT email AS E-mail, password
```

#### .where(*args)


```python
""" DB.where({COLUMN NAME}, {OPERATOR}, {VALUE}) """
    DB.where(1) # WHERE id=1
    DB.where("email", "john@example.com") # WHERE email="john@example.com"
    DB.where("id", ">", 2) # WHERE id>2
    DB.where("id", ">", 2).where("email", "jeff@example.com") # WHERE id>2 AND email="jeff@example.com"
```

#### .orderBy(column, order)


```python
""" DB.orderBy({COLUMN NAME}, {ORDER SORT} : defaults to "ASC") """
    DB.orderBy("email") # ORDER BY email ASC
    DB.orderBy("email", "DESC") # ORDER BY email DESC
```

#### .limitBy(count, offset)


```python
""" DB.limitBy({NUMBER OF RECORDS}, {OFFSET} : defaults to None) """
    DB.limitBy(1) # LIMIT 1 
    DB.limitBy(1, 2) # LIMIT 1, 2 
```

#### .get()
Queries against database with the constructed string. 

```python
""" DB.get """
    DB.table("users").get() # SELECT * FROM users
    DB.table("users").select("email").get() # SELECT email FROM users 
    DB.table("users").select("email").orderBy("updated_at").get() # SELECT email FROM users ORDER BY updated_at 
    DB.table("users").select("email").orderBy("updated_at").limitBy(1).get() # SELECT email FROM users ORDER BY updated_at LIMIT 1 
```

#### .raw(query)


```python
""" DB.raw({RAW MYSQL QUERY}) """
    DB.raw("SELECT email FROM users ORDER BY updated_at LIMIT 1").get() # SELECT email FROM users ORDER BY updated_at LIMIT 1 
```