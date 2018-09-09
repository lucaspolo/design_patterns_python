import sqlite3


class MyInt(type):
    def __call__(self, *args, **kwargs):
        print("*** Here's My int ***", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(self, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.y = y
        self.x = x


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


if __name__ == "__main__":
    i = int(4,5)

    logger1 = Logger()
    logger2 = Logger()

    print(logger1, logger2)

    db1 = Database().connect()
    db2 = Database().connect()

    print("Database 1 ", db1)
    print("Database 2 ", db2)
