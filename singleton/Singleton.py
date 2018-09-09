class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class LazySingleton:
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == "__main__":
    s = Singleton()
    print("Object", s)

    s1 = Singleton()
    print("Object", s1)

    ls1 = LazySingleton()
    print("Object created", LazySingleton.getInstance())
    ls2 = Singleton()