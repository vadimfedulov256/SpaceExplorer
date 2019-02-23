import numpy as np
import random
import secrets
import string

# Bh = black hole
# St = star
# Pl = planet
# As = asteroid

sn = [0.15, 0.4, 0.15, 0.1, 0.1, 0.05, 0.05]
pn = [0.65, 0.25, 0.1]


def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(secrets.choice(chars) for _ in range(size))


class StarSystem(object):
    def __init__(self, s_p=sn, p_p=pn):
        self.n = name_generator(size=6)
        self.n_1 = self.n+'_1'
        self.n_2 = self.n+'_2'
        self.n_3 = self.n+'_3'
        self.z = '*' * 80
        self.s_var = ['St', 'St2', 'Bh', 'Bh2', 'St+Bh', 'St2+Bh', 'Bh2+St']
        self.s_ch = np.random.choice(self.s_var, p=s_p)
        self.p_var = ['Pl+As', 'Pl', 'As']
        self.p_ch = np.random.choice(self.p_var, p=p_p)

    def examine_sys(self):
        if self.s_ch == 'St':
            self.d1 = 'Вы видите звезду '
        elif self.s_ch == 'St2':
            self.d1 = 'Вы видите две звезды '
        elif self.s_ch == 'Bh':
            self.d1 = 'Вы видите черную дыру '
        elif self.s_ch == 'Bh2':
            self.d1 = 'Вы видите две черных дыры '
        elif self.s_ch == 'St+Bh':
            self.d1 = 'Вы видите звезду и черную дыру '
        elif self.s_ch == 'St2+Bh':
            self.d1 = 'Вы видите две звезды с черную дыру '
        elif self.s_ch == 'Bh2+St':
            self.d1 = 'Вы видите две черных дыры и звезду '

        if self.p_ch == 'Pl+As':
            self.d2 = ' вместе с планетами и астероидами'
        elif self.p_ch == 'Pl':
            self.d2 = ' вместе с планетами'
        elif self.p_ch == 'As':
            self.d2 = ' вместе с астероидами'

        if self.s_ch == 'St' or self.s_ch == 'Bh':
            des_1 = 'Вы прибыли в систему '+self.n+':'
            des_2 = self.d1+self.n_1+self.d2
            print(self.z)
            print(des_1)
            print(des_2)
            print(self.z)
        elif self.s_ch == 'St2' or self.s_ch == 'Bh2' or self.s_ch == 'St+Bh':
            des_1 = 'Вы прибыли в систему '+self.n+':'
            des_2 = self.d1+self.n_1+', '+self.n_2+self.d2
            print(self.z)
            print(des_1)
            print(des_2)
            print(self.z)
        elif self.s_ch == 'St2+Bh' or self.s_ch == 'Bh2+St':
            des_1 = 'Вы прибыли в систему '+self.n+':'
            des_2 = self.d1+self.n_1+', '+self.n_2+', '+self.n_3+self.d2
            print(self.z)
            print(des_1)
            print(des_2)
            print(self.z)

    def get_ns(self, n):
        if n == 'sys':
            return self.n
        elif n == 1:
            return self.n_1
        elif n == 2:
            return self.n_2
        elif n == 3:
            return self.n_3

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
