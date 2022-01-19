from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        read_data = self.driver.read()
        for value in read_data:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    print("Считать данные из файла input.txt")
    driver = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver
    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    default_driver = SimpleFileFactoryMethod.get_driver()
    ll.driver = default_driver
    ll.write()
