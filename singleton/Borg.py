class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


if __name__ == "__main__":
    b = Borg()
    b1 = Borg()

    print(b.__dict__)
    print(b1.__dict__)

    b.novo_atributo = 5

    print(b.__dict__)
    print(b1.__dict__)
