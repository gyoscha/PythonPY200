class Parent:
    class_attr = 'Публичный атрибут класса'
    _class_attr1 = 'Приватный атрибут класса'
    __class_attr2 = 'Защищенный атрибут класса'

    def __init__(self):
        self.attr = 'Публичный атрибут экземпляра'
        self._attr1 = 'Приватный атрибут экземпляра'
        self.__attr2 = 'Защищенный атрибут экземпляра'

    def method_attr(self):
        ...

    def _method_attr1(self):
        ...

    def __method_attr2(self):
        ...

    @classmethod
    def method_class(cls):
        ...

    @classmethod
    def _method_class1(cls):
        ...

    @classmethod
    def __method_class2(cls):
        ...

    @staticmethod
    def static():
        ...

    @staticmethod
    def _static1():
        ...

    @staticmethod
    def __static2():
        ...


class Child(Parent):
    ...


if __name__ == "__main__":
    ...
