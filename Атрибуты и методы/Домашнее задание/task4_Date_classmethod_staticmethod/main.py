class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if not isinstance(year, int):
            raise TypeError('Неправильно введен год!')

        if year % 4 == 0:
            print('Год високосный')
            return True
        else:
            print('Обычный год')
            return False

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if not isinstance(month, int):
            raise TypeError('Неправильно введен месяц!')
        if not 1 <= month <= 12:
            raise ValueError('Такого месяца не существует!')

        if cls.is_leap_year(year) is True:
            return cls.DAY_OF_MONTH[1][month - 1]
        else:
            return cls.DAY_OF_MONTH[0][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        if not isinstance(day, int):
            raise TypeError('Неправильно введен день!')
        if not 1 <= day <= cls.get_max_day(month, year):
            raise ValueError('Такого дня в этом месяце нет!')

    def __str__(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'


if __name__ == "__main__":
    date_1 = Date(11, 2, 1990)
    print(date_1)
