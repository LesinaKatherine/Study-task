import random


class Tomato:
    states = {0: 'цветок', 1: 'завязь', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = random.randint(0, 3)

    def grow(self):
        self._next_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _next_state(self):
        if self._state < 3:
            self._state += 1
        print(f'Томат {self._index} на стадии "{Tomato.states[self._state]}"')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name, bush):
        self.name = name
        self._bush = bush

    def work(self):
        print('Садовник работает')
        self._bush.grow_all()

    def harvest(self):
        print('Садовник собирает урожай')
        if self._bush.all_are_ripe():
            self._bush.give_away_all()
            print('Урожай собран!')
        else:
            print('Слишком рано для сбора урожая, помидоры ещё не созрели!')

    @staticmethod
    def knowledge_base():
        print('Необходимо постоянно ухаживать за томатами,\n'
              'от стадии цветка до полного созревания, чтобы получить\n'
              'действительно хороший куст спелых красных томатов.\n'
              'Только благодаря нашей селекции можно указать количество\n'
              'томатов, которые будут расти на вашем кусте.')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Пауло', great_tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()
