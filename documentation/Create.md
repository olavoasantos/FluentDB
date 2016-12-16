### FluentDB
# Creating Table

#### Initializing module
First we need to instantiate FluentDB: 
```python
from lib.Fluenttable.core import FluentDB


if __name__ == "__main__":
    # Instantiates FluentDB class and initiates the database driver 
    DB = FluentDB()
```

Now that we have instantiated and initialized the database driver, we can start interacting with the database.

### Creating table structure
First we need to create the table structure. To do that, we should instantiate the table-maker:

#### .newTable(name)


```python
""" .newTable({TABLE NAME}) """
    table = DB.newTable('users')
```

With our table-maker instance in hand, we can create our columns.

## Creating columns

#### .increments(name)


```python
""" .increments({COLUMN NAME}) """
    table.increments("id") # id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
```

#### .bigIncrements(name)


```python
""" .bigIncrements({COLUMN NAME}) """
    table.bigIncrements("id") # id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
```

#### .tinyInteger(name, size=None)


```python
""" .tinyInteger({COLUMN NAME}, {SIZE} = None) """
    table.tinyInteger("numbers") # numbers TINYINT
```
#### .smallInteger(name, size=None)
 
 
```python
""" .smallInteger({COLUMN NAME}) """
    table.smallInteger("number") # number SMALLINT
```

#### .mediumInteger(name, size=None)


```python
""" .mediumInteger({COLUMN NAME}, {SIZE}) """
    table.mediumInteger("number") # number MEDIUMINT
```

#### .integer(name, size=None)


```python
""" .integer({COLUMN NAME}, {SIZE}) """
    table.integer("id") # id INT
```

#### .bigInteger(name, size=None)


```python
""" .bigInteger({COLUMN NAME}, {SIZE}) """
    table.bigInteger("bigNumber") # bigNumber BIGINT
```

#### .float(name, size=None, decimal=None)


```python
""" .float({COLUMN NAME}, {SIZE}) """
    table.float("number") # number FLOAT
```

#### .double(name, size=None, decimal=None)


```python
""" .double({COLUMN NAME}, {SIZE}, {DECIMALs}) """
    table.double("number") # number DOUBLE
```

#### .decimal(name, size=None, decimal=None)


```python
""" .decimal({COLUMN NAME}, {SIZE}, {DECIMALs}) """
    table.decimal("number") # number DECIMAL
```

#### .char(name, size=None)


```python
""" .char({COLUMN NAME}, {SIZE}) """
    table.char("character") # character CHAR
```

#### .string(name, size=255)


```python
""" .string({COLUMN NAME}, {SIZE}) """
    table.string("email") # email VARCHAR(255)
```

#### .text(name, size=65535)


```python
""" .text({COLUMN NAME}, {SIZE}) """
    table.text("text") # text TEXT
```

#### .tinyText(name, size=255)


```python
""" .tinyText({COLUMN NAME}, {SIZE}) """
    table.tinyText("twit") # twit TINYTEXT
```

#### .mediumText(name)


```python
""" .mediumText({COLUMN NAME}) """
    table.mediumText("post") # post MEDIUMTEXT
```

#### .longText(name)


```python
""" .longText({COLUMN NAME}) """
    table.longText("body") # body LONGTEXT
```

#### .timestamp(name)


```python
""" .timestamp({COLUMN NAME}) """
    table.timestamp("deleted_at") # deleted_at TIMESTAMP
```

#### .timestamps()


```python
""" .timestamps() """
    table.timestamps() # created_at TIMESTAMP, updated_at TIMESTAMP,
```

#### .rawColumn(query)


```python
""" .rawColumn({RAW MYSQL QUERY}) """
    table.rawColumn("CREATE TABLE users (...)") # CREATE TABLE users (...)
```

## Column constraints

#### .check(column, operator, value)

```python
""" .check({COLUMN NAME}, {OPERATOR}, {VALUE}) """
    table.check("age", ">", 18) # CHECK (age>18)
```

#### .unique()


```python
""" .unique() """
    table.string('email').unique() #  email VARCHAR(255) UNIQUE
```

#### .nullable()


```python
""" .nullable() """
    table.string('email').nullable() #  email VARCHAR(255) IS NULL
```

#### .notNull()


```python
""" .notNull() """
    table.string('email').notNull() #  email VARCHAR(255) NOT NULL
```

#### .default()


```python
""" .default() """
    table.integer('votes').default(0) # votes INT DEFAULT 0
```

#### .rawConstraint()


```python
""" .rawConstraint({RAW MYSQL QUERY}) """
    table.integer('id').rawConstraint("UNIQUE IS NULL AUTO_INCREMENT") # id INT UNIQUE IS NULL AUTO_INCREMENT
```

### Example
Say we want to create a `users` table like the one below:

| id  | created_at  | updated_at  | email  | password  |
|-----|-------------|-------------|--------|-----------|
| 1   | 06-May-2009 16:40:04  | 04-Nov-2010 18:24:40  | john@example.com  |  7fae8c79b45a1690a5adf37c7dc108de8698fe38 |
| 2   | 11-Oct-2010 22:30:43  | 07-Oct-2016 14:12:21  | jane@example.com  |  67c03a024140ae827db19dc6ab0a32b6228d5462 |
| 3   | 07-Jan-2018 10:34:59  | 29-May-2035 15:07:04  | jeff@example.com  |  97e3f719a38bd05a8ff4e7ddd1a211d6731fc2a1 |

```python
from lib.Fluenttable.core import FluentDB


if __name__ == "__main__":
    # Instantiates FluentDB class and initiates the database driver 
    DB = FluentDB()
    # Instantiate the table-maker
    table = DB.newTable('users')
    
    # Create columns
    table.increments('id')
    table.timestamps()
    table.string('email').unique()
    table.string('password')
    
    # Execute command
    DB.create(table)
    
```