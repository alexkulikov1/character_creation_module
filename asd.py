class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    # Переопределите метод describe().

    def describe(self, full=False):
        if full:
            return f'Размер птицы {self.name} — {self.size}.'
        else:
            return (f'Попугай {self.name} — заметная птица,'
                    f'окрас её перьев — {self.color}, а размер — {self.size}.'
                    f'Интересный факт: попугаи чувствуют ритм,'
                    f'а вовсе не бездумно двигаются под музыку.'
                    f'Если сменить композицию, то и темп движений'
                    f' птицы изменится.')


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    # Переопределите метод describe().

    def describe(self, full=False):
        if full:
            return f'Размер птицы {self.name} — {self.size}.'
        else:
            return (f'Размер пингвина {self.name} из'
                    f'рода {self.genus} — {self.size}.'
                    f'Интересный факт: однажды группа'
                    f'геологов-разведчиков похитила пингвинье яйцо,'
                    f'и их принялась преследовать вся стая, не пытаясь,'
                    f'впрочем, при этом нападать. Посовещавшись,'
                    f'похитители вернули птицам яйцо, и те отстали.')


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)
