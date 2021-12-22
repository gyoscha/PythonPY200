from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def __str__(self):
        return f'Стакан объемом {self.capacity_volume} и заполнен на {self.occupied_volume}'

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError

        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError

        self.occupied_volume = occupied_volume

    def add_water(self, add: Union[int, float]):
        if not isinstance(add, (int, float)):
            raise TypeError
        if self.capacity_volume < self.occupied_volume + add:
            raise ValueError('Пытаетесь долить слишком много воды!')
        self.occupied_volume += add

    def remove_water(self, remove: Union[int, float]):
        if not isinstance(remove, (int, float)):
            raise TypeError
        if self.occupied_volume < remove:
            raise ValueError('В стакане нет столько воды!')
        self.occupied_volume -= remove


if __name__ == '__main__':
    glass_1 = Glass(500, 100)
    glass_2 = Glass(200, 10)

    glass_1.remove_water(99)
    print(glass_1)

    glass_2.add_water(191)
    print(glass_2)
