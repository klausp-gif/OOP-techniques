class Newspaper:
    def __init__(self, name, year, month, day_of_month, is_finnish):
        self.__name = name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def __str__(self):
        return f'Newspaper: {self.__name}, {self.day_of_month}.{self.month}.{self.year}, Finnish: {self.is_finnish}'

    def get_name(self):
        return self.__name

print(Newspaper('HS', 2025, 12, 23, True))
print(Newspaper('HS', 2025, 12, 23, True).get_name())