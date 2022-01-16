class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if not isinstance(year, int):
            raise TypeError('Неправильно введен год!')

        if year % 4 == 0:
            print('Год високосный')
            return True
        else:
            print('Обычный год')
            return False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if not isinstance(month, int):
            raise TypeError('Неправильно введен месяц!')
        if not 1 <= month <= 12:
            raise ValueError('Такого месяца не существует!')

        if self.is_leap_year(year) is True:
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        if not isinstance(day, int):
            raise TypeError('Неправильно введен день!')
        if not 1 <= day <= self.get_max_day(month, year):
            raise ValueError('Такого дня в этом месяце нет!')

    def __str__(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError
        if not 1 <= day <= 31:
            raise ValueError

        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month: int) -> None:
        if not isinstance(month, int):
            raise TypeError
        if not 1 <= month <= 12:
            raise ValueError

        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year:int) -> None:
        if not isinstance(year, int):
            raise TypeError
        if not year > 0:
            raise ValueError

        self._year = year


if __name__ == "__main__":
    date_1 = Date(1, 12, 1990)
    print(date_1)
