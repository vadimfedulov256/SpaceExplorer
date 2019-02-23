import numpy as np
import random

cl_bn = [0.5, 0.25, 0.2, 0.05]


class BlackHole(object):
    def __init__(self, StarSystem, clp=cl_bn):
        self.cl_var = ['малая', 'средне-малая', 'средне-большая', 'большая']
        self.z = '*' * 80
        self.cl_1_ch = np.random.choice(self.cl_var, p=clp)
        self.cl_2_ch = np.random.choice(self.cl_var, p=clp)

        def check_cl_ch(number):
            if number == 1:
                if self.cl_1_ch == 'малая':
                    self.m1 = np.round(random.uniform(10, 99), decimals=2)
                elif self.cl_1_ch == 'средне-малая':
                    self.m1 = np.round(random.uniform(100, 264), decimals=2)
                elif self.cl_1_ch == 'средне-большая':
                    self.m1 = np.round(random.uniform(265, 499), decimals=2)
                elif self.cl_1_ch == 'большая':
                    self.m1 = np.round(random.uniform(500, 999), decimals=2)
            elif number == 2:
                if self.cl_2_ch == 'малая':
                    self.m2 = np.round(random.uniform(10, 99), decimals=2)
                elif self.cl_2_ch == 'средне-малая':
                    self.m2 = np.round(random.uniform(100, 264), decimals=2)
                elif self.cl_2_ch == 'средне-большая':
                    self.m2 = np.round(random.uniform(265, 499), decimals=2)
                elif self.cl_2_ch == 'большая':
                    self.m2 = np.round(random.uniform(500, 999), decimals=2)

        if StarSystem.get_obj('Bh') is None:
            self.b = None
        elif StarSystem.get_obj('Bh') == [1]:
            check_cl_ch(1)
            self.n_b_1 = StarSystem.get_ns(1)
            self.b = 1
        elif StarSystem.get_obj('Bh') == [2]:
            check_cl_ch(1)
            self.n_b_1 = StarSystem.get_ns(2)
            self.b = 1
        elif StarSystem.get_obj('Bh') == [1, 2]:
            check_cl_ch(1)
            check_cl_ch(2)
            self.n_b_1 = StarSystem.get_ns(1)
            self.n_b_2 = StarSystem.get_ns(2)
            self.b = 2
        elif StarSystem.get_obj('Bh') == [3]:
            check_cl_ch(1)
            self.n_b_1 = StarSystem.get_ns(3)
            self.b = 1

    def __num_error(self, number):
        if number == 1:
            self.a1 = 'Вы ввели некорректный номер черной дыры'
            self.b1 = 'Помните, что нужно писать '
            self.c1 = 'порядковый номер объекта данного типа'
            self.d1 = 'В данном случае вы можете написать только "1"'
            print(self.z)
            print(self.a1+'\n'+self.b1+self.c1+'\n'+self.d1)
            print(self.z)
        elif number == 2:
            self.a2 = 'Вы ввели некорректный номер черной дыры'
            self.b2 = 'Помните, что нужно писать '
            self.c2 = 'порядковый номер объекта данного типа'
            self.d2 = 'В данном случае вы можете написать только "1"/"2"'
            print(self.z)
            print(self.a2+'\n'+self.b2+self.c2+'\n'+self.d2)
            print(self.z)

    def _multi_single_error(self, n):
        if self.b is None:
            return [True, True]
        elif self.b == 2 and n is 'all':
            return [True, False]
        elif self.b == 1 and n != 1:
            return [True, True]
        elif self.b == 2 and n != 1 and n != 2:
            return [True, True]
        elif self.b == 1 or self.b == 2 and n == 1:
            return [False, True]
        elif self.b == 2 and n == 2:
            return [False, True]

    def help_bh(self):
        if self.b is None:
            self.h1 = 'В данной системе нет черных дыр для исследования'
            self.h2 = 'Попробуйте исследовать систему, звезды'
            self.h3 = ' или совершить прыжок'
            print(self.z+'\n'+self.h1+'\n'+self.h2+self.h3+'\n'+self.z)
        elif self.b == 1:
            self.h1 = 'В данной системе есть одна черная дыра для исследования'
            self.h2 = 'Вы можете написать "1" для её исследования'
            print(self.z+'\n'+self.h1+'\n'+self.h2+'\n'+self.z)
        elif self.b == 2:
            self.h1 = 'В данной системе есть две черные дыры для исследования'
            self.h2 = 'Вы можете написать "1" или "2" для исследования '
            self.h3 = 'одной из них'
            print(self.z+'\n'+self.h1+'\n'+self.h2+self.h3+'\n'+self.z)

    def examine_bh(self, n):
        if self.b is None:
            print(self.z)
            print('В данной системе нет черных дыр для исследования')
            print(self.z)
        elif self.b == 2 and n is 'all':
            self.m1 = str(self.m1)
            self.m2 = str(self.m2)
            print(self.z)
            self.desc_1 = self.n_b_1+' - это '+self.cl_1_ch+' черная дыра'
            print(self.desc_1)
            self.desc_2 = 'Имеет массу '+self.m1+' солнечных единиц'
            print(self.desc_2)
            print(self.z)
            self.desc_3 = self.n_b_2+' - это '+self.cl_2_ch+' черная дыра'
            print(self.desc_3)
            self.desc_4 = 'Имеет массу '+self.m2+' солнечных единиц'
            print(self.desc_4)
            print(self.z)
        elif self.b == 1 and n is 'all':
            self.a = 'В данной системе находится только одна черная дыра'
            print(self.z+'\n'+self.a+'\n'+self.z)
        elif self.b == 1 and n != 1:
            self.__num_error(1)
        elif self.b == 2 and n != 1 and n != 2:
            self.__num_error(2)
        elif self.b == 1 or self.b == 2 and n == 1:
            self.m1 = str(self.m1)
            print(self.z)
            self.desc_1 = self.n_b_1+' - это '+self.cl_1_ch+' черная дыра'
            print(self.desc_1)
            self.desc_2 = 'Имеет массу '+self.m1+' солнечных единиц'
            print(self.desc_2)
            print(self.z)
        elif self.b == 2 and n == 2:
            self.m2 = str(self.m2)
            print(self.z)
            self.desc_3 = self.n_b_2+' - это '+self.cl_2_ch+' черная дыра'
            print(self.desc_3)
            self.desc_4 = 'Имеет массу '+self.m2+' солнечных единиц'
            print(self.desc_4)
            print(self.z)
