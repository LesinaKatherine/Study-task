class Homework:
    def __init__(self, x: str) -> (str, int):
        if x.isdigit():
            self.x = int(x)
        else:
            self.x = x

    def __len__(self):
        return len(str((self.x)))

    def start(self):
        """Метод класса, принимающий введенное значение х;
        Если х - число, то возвращает сумму четных цифр, умноженных на длину числа;
        Если х - строка, то, если частное от деления гласных на согласные больше
        или равно длины слова, то возвращает все гласные из строки. В противном случае - согласные."""
        if isinstance(self.x, int):
            even = []
            for i in str(self.x):
                if int(i) % 2 == 0:
                    even.append(int(i))
            print(sum(even) * len(str(self.x)))

        elif isinstance(self.x, str):
            wowels: str = ''
            consonants: str = ''
            for i in self.x:
                if isinstance(i, str):
                    for _ in i:
                        if _ in 'уеыаоэяиюeyuioa':
                            wowels += _
                        else:
                            consonants += _

            if len(wowels) / len(consonants) >= len(self.x):
                print(wowels)
            else:
                print(consonants)


a = Homework(input("Введите число или строку: "))
a.start()
print(f'Длина переменной составляет {a.__len__()} символов')