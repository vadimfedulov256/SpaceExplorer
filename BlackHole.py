import numpy as np
import random

cl_bn = [0.5, 0.25, 0.2, 0.05]
z = '*' * 80


class BlackHole(object):
    def __init__(self, Sys, clp=cl_bn, z=z):
        self.cl_var = ['малая', 'средне-малая', 'средне-большая', 'большая']
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

        if Sys.get_obj('Bh') is None:
            self.b = None
        elif Sys.get_obj('Bh') == [1]:
            check_cl_ch(1)
            self.n_b_1 = Sys.get_ns(1)
            self.b = 1
        elif Sys.get_obj('Bh') == [2]:
            check_cl_ch(1)
            self.n_b_1 = Sys.get_ns(2)
            self.b = 1
        elif Sys.get_obj('Bh') == [1, 2]:
            check_cl_ch(1)
            check_cl_ch(2)
            self.n_b_1 = Sys.get_ns(1)
            self.n_b_2 = Sys.get_ns(2)
            self.b = 2
        elif Sys.get_obj('Bh') == [3]:
            check_cl_ch(1)
            self.n_b_1 = Sys.get_ns(3)
            self.b = 1

    def __num_error(self, number):
        self.nerr1 = 'Вы ввели некорректный номер черной дыры\n'
        self.nerr2 = 'Помните, что нужно писать порядковый '
        self.nerr3 = 'номер объекта данного типа\n'
        if number == 1:
            self.nerr4 = 'В данном случае вы можете написать только "1"'
        elif number == 2:
            self.nerr4 = 'В данном случае вы можете написать только "1"/"2"'
        self.nerr = f'{self.nerr1}{self.nerr2}{self.nerr3}{self.nerr4}'
        print(f'{z}\n{self.nerr}\n{z}')

    def __multiple_form(self, n):
        if int(str(n)[-1]) == 1:
            return 'солнечной единицы'
        else:
            return 'солнечных единиц'

    def _multi_single_error(self, n):
        if self.b is None:
            return [True, True] # error for all forms
        elif self.b == 2 and n is 'all':
            return [True, False] # error for single form
        elif self.b == 1 and n != 1:
            return [True, True] # error for all forms
        elif self.b == 2 and n != 1 and n != 2:
            return [True, True] # error for all forms
        elif self.b == 1 or self.b == 2 and n == 1:
            return [False, True] # error for multiple form
        elif self.b == 2 and n == 2:
            return [False, True] # error for multiple form

    def help_bh(self):
        if self.b is None:
            self.h1 = 'В данной системе нет черных дыр для исследования'
            self.h2 = 'Попробуйте исследовать систему, звезды'
            self.h3 = ' или совершить прыжок'
            print(f'{z}\n{self.h1}\n{self.h2}{self.h3}\n{z}')
        elif self.b == 1:
            self.h1 = 'В данной системе есть одна черная дыра для исследования'
            self.h2 = 'Вы можете написать "1" для её исследования'
            print(f'{z}\n{self.h1}\n{self.h2}\n{z}')
        elif self.b == 2:
            self.h1 = 'В данной системе есть две черные дыры для исследования'
            self.h2 = 'Вы можете написать "1" или "2" для исследования '
            self.h3 = 'одной из них'
            print(f'{z}\n{self.h1}\n{self.h2}{self.h3}\n{z}')

    def examine_bh(self, n):
        if self.b is None:
            print(z)
            print('В данной системе нет черных дыр для исследования')
            print(z)
        elif self.b == 2 and n is 'all':
            self.form1 = self.__multiple_form(self.m1)
            self.desc1 = f'{self.n_b_1} - это {self.cl_1_ch} черная дыра'
            self.desc2 = f'Имеет массу {self.m1} {self.form1}'
            print(f'{z}\n{self.desc1}\n{self.desc2}\n{z}')
            self.form2 = self.__multiple_form(self.m2)
            self.desc3 = f'{self.n_b_2} - это {self.cl_2_ch} черная дыра'
            self.desc4 = f'Имеет массу {self.m2} {self.form2}'
            print(f'{self.desc3}\n{self.desc4}\n{z}')
        elif self.b == 1 and n is 'all':
            self.err = 'В данной системе находится только одна черная дыра'
            print(f'{z}\n{self.err}\n{z}')
        elif self.b == 1 and n != 1:
            self.__num_error(1)
        elif self.b == 2 and n != 1 and n != 2:
            self.__num_error(2)
        elif self.b == 1 or self.b == 2 and n == 1:
            self.form1 = self.__multiple_form(self.m1)
            self.desc1 = f'{self.n_b_1} - это {self.cl_1_ch} черная дыра'
            self.desc2 = f'Имеет массу {self.m1} {self.form1}'
            print(f'{z}\n{self.desc1}\n{self.desc2}\n{z}')
        elif self.b == 2 and n == 2:
            self.form2 = self.__multiple_form(self.m2)
            self.desc3 = f'{self.n_b_2} - это {self.cl_2_ch} черная дыра'
            self.desc4 = f'Имеет массу {self.m2} {self.form2}'
            print(f'{z}\n{self.desc3}\n{self.desc4}\n{z}')
