class Date:
    """
    Класс, который описывает дату в формате DD/MM/YYYY

    """
    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.init_day(day)

        self.month = None
        self.init_month(month)

        self.year = None
        self.init_year(year)

    def init_day(self, day: int):
        if not isinstance(day, int):
            raise TypeError
        if day > 31:
            raise ValueError
        self.day = day

    def init_month(self, month: int):
        if not isinstance(month, int):
            raise TypeError
        if month > 12 or month <= 0:
            raise ValueError
        self.month = month

    def init_year(self, year: int):
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __str__(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'

    def __repr__(self):
        return f'Date({self.day}, {self.month}, {self.year})'


if __name__ == '__main__':
    date_1 = Date(1, 12, 2007)
    print(date_1)

    date_2 = [Date(9, 8, 2005)]
    print(date_2)