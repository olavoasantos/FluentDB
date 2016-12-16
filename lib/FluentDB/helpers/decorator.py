from functools import wraps


def decorate_all_functions(function_decorator):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                setattr(cls, name, function_decorator(obj))
        return cls

    return decorator


def beforeAfterCall(func):
    @wraps(func)
    def wrapper(*args, **kw):
        name = func.__name__

        # before
        if getattr(args[0], "before{0}".format(name.capitalize()), None):
            getattr(args[0], "before{0}".format(name.capitalize()))(*args)
        try:
            res = func(*args, **kw)
        finally:
            # After
            if getattr(args[0], "after{0}".format(name.capitalize()), None):
                getattr(args[0], "after{0}".format(name.capitalize()))(*args)
        return res

    return wrapper