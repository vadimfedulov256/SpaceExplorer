import numpy as np
import random
import string

# Bh = black hole
# St = star
# Pl = planet
# As = asteroid

sn = [0.15, 0.4, 0.15, 0.1, 0.1, 0.05, 0.05]
pn = [0.65, 0.25, 0.1]
z = '*' * 80


def name_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for char in range(size))


class System(object):
    def __init__(self, s_p=sn, p_p=pn, z=z, size=4):
        self.n = name_generator(size)
        self.n1 = self.n+'_1'
        self.n2 = self.n+'_2'
        self.n3 = self.n+'_3'
        self.s_var = ['St', 'St2', 'Bh', 'Bh2', 'St+Bh', 'St2+Bh', 'Bh2+St']
        self.s_ch = np.random.choice(self.s_var, p=s_p)
        self.p_var = ['Pl+As', 'Pl', 'As']
        self.p_ch = np.random.choice(self.p_var, p=p_p)

    @classmethod
    def hard(cls):
        return cls(s_p=[0.05, 0.2, 0.25, 0.15, 0.1, 0.05, 0.05], size=5)

    def examine_sys(self):
        if self.s_ch == 'St':
            self.e1 = 'Вы видите звезду'
        elif self.s_ch == 'St2':
            self.e1 = 'Вы видите две звезды'
        elif self.s_ch == 'Bh':
            self.e1 = 'Вы видите черную дыру'
        elif self.s_ch == 'Bh2':
            self.e1 = 'Вы видите две черных дыры'
        elif self.s_ch == 'St+Bh':
            self.e1 = 'Вы видите звезду и черную дыру'
        elif self.s_ch == 'St2+Bh':
            self.e1 = 'Вы видите две звезды и черную дыру'
        elif self.s_ch == 'Bh2+St':
            self.e1 = 'Вы видите две черных дыры и звезду'

        if self.p_ch == 'Pl+As':
            self.e2 = 'вместе с планетами и астероидами'
        elif self.p_ch == 'Pl':
            self.e2 = 'вместе с планетами'
        elif self.p_ch == 'As':
            self.e2 = 'вместе с астероидами'

        if self.s_ch == 'St' or self.s_ch == 'Bh':
            self.d1 = f'Вы прибыли в систему {self.n}:'
            self.d2 = f'{self.e1} {self.n1} {self.e2}'
        elif self.s_ch == 'St2' or self.s_ch == 'Bh2' or self.s_ch == 'St+Bh':
            self.d1 = f'Вы прибыли в систему {self.n}:'
            self.d2 = f'{self.e1} {self.n1}, {self.n2} {self.e2}'
        elif self.s_ch == 'St2+Bh' or self.s_ch == 'Bh2+St':
            self.d1 = f'Вы прибыли в систему {self.n}:'
            self.d2 = f'{self.e1} {self.n1}, {self.n2}, {self.n3} {self.e2}'
        print(f'{z}\n{self.d1}\n{self.d2}\n{z}')

    def get_ns(self, n):
        if n == 'sys':
            return self.n
        elif n == 1:
            return self.n1
        elif n == 2:
            return self.n2
        elif n == 3:
            return self.n3

    def get_obj(self, obj):
        if obj == 'St':
            if self.s_ch == 'Bh' or self.s_ch == 'Bh2':
                return None
            elif self.s_ch == 'St' or self.s_ch == 'St+Bh':
                return [1]
            elif self.s_ch == 'St2' or self.s_ch == 'St2+Bh':
                return [1, 2]
            elif self.s_ch == 'Bh2+St':
                return [3]
        elif obj == 'Bh':
            if self.s_ch == 'St' or self.s_ch == 'St2':
                return None
            elif self.s_ch == 'Bh':
                return [1]
            elif self.s_ch == 'St+Bh':
                return [2]
            elif self.s_ch == 'Bh2' or self.s_ch == 'Bh2+St':
                return [1, 2]
            elif self.s_ch == 'St2+Bh':
                return [3]
