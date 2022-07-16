import string

# 1
class Human():
    default_name = 'Eve'
    default_age = 33

    def __init__(self, name=default_name, age=default_age):
        self.name, self.age = name, age
        self.__money = 100
        self.__house = 'house_type'

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_inf():
        print(Human.default_name, Human.default_age)

    def earn_money(self, value):
        self.__money += value
        print(f'Текущий баланс: {self.__money}$')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        print(f'Cтоимость дома с учетом скидки: {house.final_price(discount)}')
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f'Покупка дома совершена успешно!\n'
                  f'Остаток на счету равен {self.__money}$')
        else:
            print('Недостаточно средств!')


class House:
    def __init__(self, area=10, price=1000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price - ((self._price / 100) * discount)
        return final_price


class SmallHouse(House):
    small_house_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.small_house_area, price)

    def info(self):
        print(self._area, self._price)


small_house1 = SmallHouse(1200)
man = Human()
man.buy_house(small_house1, 5)
man.earn_money(1200)
man.buy_house(small_house1, 30)
print('\n')


# 2
class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def letters_num(self):
        return EngAlphabet.__letters_num

    def is_en_letter(self, let):
        self.let = let
        if self.let in self.letters:
            print('Такая буква есть в английском алфавите')
        else:
            print('Такой буквы в английском алфавите нет')

    @staticmethod
    def example():
        return 'The five boxing wizards jump quickly'


ex = EngAlphabet()
ex.print()
print(ex.letters_num())
ex.is_en_letter('F')
ex.is_en_letter('Щ')
print(ex.example())
