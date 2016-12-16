### FluentDB
# Models

## Introduction
As defined in the [MVC design pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), the model directly manages the data, logic, and rules of the application. As such, each database table should have a corresponding "Model" which is used to interact with that table. Models allow you to use and manipulate your database data in a more readable way.

In FluentDB, you have two options for using models: using the generic [BaseModel](https://github.com/olavoasantos/FluentDB/blob/master/lib/FluentDB/model/BaseModel.py) or creating your own. As default, the FluentDB's fetching queries returns either a collection or a single BaseModel. Ultimately, all models, either custom or generic, are all instances or extensions of the `FluentDB.model.BaseModel` class.

## Defining Models
### FluentDB Model Conventions
Before creating our own method, we should know that FluentDB's models follow certain conventions.

##### Directory Placement
Firstly, all custom models are stored on the projects main folder, in a `./models` directory.

##### Primary Key and Timestamps
By default, FluentDB will assume your primary key is `id` and expects `created_at` and `updated_at` columns to exist on your table. The timestamps will be set and updated automatically by FluentDB when inserting and saving your models.

##### Naming convention
Finally, the model's file and class name should always be `{Capitalized singular form of database name}Model`. If that sounded really really scary, don't sweat it! Let's look at an example.

### Creating Our Model
Say we have a table in our database called `'users'`. This table's model should be called `UserModel`. The directory structure would look something like:
 
 ```markdown
     .
     +-- lib
     +-- models
     |   +-- UserModel.py
     +-- __main__.py
 ```
and the class should be defined as:
 
```python
from lib.FluentDB.model.BaseModel import BaseModel


class UserModel(BaseModel):
    ...
```

### Table Name
Now that we created our class, we need to the FluentDB which table our User model will use. To do that, we can specify the table as a `table` property on our model:

##### table
```python
from lib.FluentDB.model.BaseModel import BaseModel


class UserModel(BaseModel):
    # *
    # The table associated with the model.
    # 
    # @var string   !Required
    # **  
    table = 'users'
```
 
Congrats! You are done. This is the simplest model you get create and, essentially, this is the equivalent of what you get when using the generic model.

Now that we got to this point, let's take a look on how we can personalize this class.

### Hiding Attributes
Sometimes you may wish to limit the attributes, such as passwords, that are included in your model. To do so, you can define  a `__hidden` property:

##### __hidden
```python
from lib.FluentDB.model.BaseModel import BaseModel


class UserModel(BaseModel):
    # *
    # The attributes that should be hidden from the model.
    # 
    # @var dict (default) {}
    # **
    __hidden = {'password'}
```

On the other hand, you may choose to define only the properties that should be visible. You can do that by defining a `__visible` property:

##### __visible
```python
from lib.FluentDB.model.BaseModel import BaseModel


class UserModel(BaseModel):
    # *
    # The attributes that should be visible in the model. If is empty,
    # the model will shows all which are not listed in __hidden.
    #
    # @var  dict    !optional  (default)    {}
    # **
    __visible = {'email', 'first_name', 'last_name'}
```

### Securing Attributes
When working with your database, the may come a time in which you need to secure an attribute preventing it from being modify when updated. You can achieve that by adding a `__secure` property:
 
##### __secure
```python
from lib.FluentDB.model.BaseModel import BaseModel


class UserModel(BaseModel):
    # *
    # The attributes that should not be modified in the model.
    # 
    # @var dict
    # **
    __secure = {'id', 'created_at'}
```

By default, both `id` and `created_at` are secure in the models.

## Inserting Data

##### .save()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.first_name = 'John'
    User.last_name = 'Doe'
    User.email = 'john@example.com'
    User.password = 'password123'
    User.save()
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at': datetime.datetime(2016, 12, 15, 22, 23, 14),
    #   'first_name': 'John',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
```

##### .create(data)
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'password': 'password123',
    }
    User.create(data)
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at': datetime.datetime(2016, 12, 15, 22, 23, 14),
    #   'first_name': 'John',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
```

## Retrieving Models
Once we have created our model and its associated database table, we are ready to start managing the data. For example, to get all the entries in `users`:

##### .all()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    Users = User.all()
    
    print(Users)
    # yields:
    # [
    #   <models.UserModel.UserModel object at 0x02A26EB0>,
    #   <models.UserModel.UserModel object at 0x02A26F70>,
    #   <models.UserModel.UserModel object at 0x02A26F50>
    # ]
```

On the other hand, if you wish to get the first entry:

##### .first()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.first()
    
    print(User)
    # yields:
    # <models.UserModel.UserModel object at 0x00B6F470>
```

Finally, if you wish to get an entry with a specified `id`:

##### .find(id)
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.find(1)
    
    print(User)
    # yields:
    # <models.UserModel.UserModel object at 0x00B6F470>
```

## Accessing Attributes
The model class allow us to access the data from these models through simple attributes. So, back to our `users` example:

##### .{column name}
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.find(1)
    
    print(User.id)
    print(User.email)
    print(User.first_name)
    print(User.last_name)
    # yields:
    # 1
    # 'john@example.com'
    # 'John'
    # 'Doe'
```

## Updating Data
##### .save()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.find(1)
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at': datetime.datetime(2016, 12, 15, 22, 23, 14),
    #   'first_name': 'John',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
    
    User.first_name = 'Johnathan'
    User.save()
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at':datetime.datetime(2016, 12, 16, 16, 19, 29, 565916),
    #   'first_name': 'Johnathan',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
```

## Rolling Back Update to Original Attributes

##### .rollback()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.find(1)
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at': datetime.datetime(2016, 12, 15, 22, 23, 14),
    #   'first_name': 'John',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
    
    User.first_name = 'Johnathan'
    User.save()
    
    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at':datetime.datetime(2016, 12, 16, 16, 19, 29, 565916),
    #   'first_name': 'Johnathan',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
    
    User.rollback()

    print(User.__dict__)
    # yields:
    # {
    #   'id': 1,
    #   'created_at': datetime.datetime(2016, 12, 14, 22, 10, 14)
    #   'updated_at': datetime.datetime(2016, 12, 15, 22, 23, 14),
    #   'first_name': 'John',
    #   'last_name': 'Doe',
    #   'email': 'john@example.com',
    #   'password': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    # }
```

## Deleting Model

##### .delete()
```python
from models.UserModel import UserModel

if __name__ == '__main__':
    User = UserModel()
    User.delete()
```

## Before/After Call
Sometimes we may wish to trigger events right before or right after a method is called. For example, we may want to hash the `password` attribute before saving to the database or validate the data. In these cases, you can activate the `beforeAfterCall` wrapper. When a function is called, this wrapper will call two functions based on the original function's name: `before{Capitalized function name}` and `after{Capitalized function name}`.
 
 I know... It's easier to see an example. Let's say. as I mentioned before, we may want to hash the `password` attribute before saving to the database. So the function should be called right before the `save()` function runs. That means we need to define a `beforeSave()` function:
 
 ```python
import hashlib # This is just to hash the password =)
from lib.FluentDB.model.BaseModel import BaseModel
from lib.FluentDB.helpers.decorator import decorate_all_functions, beforeAfterCall

@decorate_all_functions(beforeAfterCall)
class UserModel(BaseModel):
    # *
    #* beforeSave(*args)
    #* -----------------------------------------------------------------------------------------
    #* This is an example use of a beforeAfterCall function that is called before saving a
    #* model. Before persisting the data to the database, the password is hashed. This
    #* is an optional method.
    # **
    def beforeSave(*args):
        """
        Function called before executing self.save(). It hashes the 'password' attribute.
        *** args[0] represents 'self' object.

        :param args:    Mixed
        :return: pass
        """
        args[0].password = args[0].hash(args[0].password)

        pass

    # *
    #* hash(string)
    #* -----------------------------------------------------------------------------------------
    #* Hashes a given string using SHA256 algorithm. This is an optional method but good for
    #* password security.
    # **
    @staticmethod
    def hash(string):
        """
        It Hashes a given string using SHA256 algorithm.

        :param string:  str
        :return: str
        """
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
```