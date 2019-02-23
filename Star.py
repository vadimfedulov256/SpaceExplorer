import numpy as np
import random
import time
from tqdm import tqdm

cl_sn = [0.05, 0.1, 0.15, 0.2, 0.2, 0.25, 0.05]
m1_sn = [0.05, 0.25, 0.7]
m2_sn = [0.15, 0.2, 0.25, 0.3, 0.1]
m3_sn = [0.05, 0.05, 0.1, 0.1, 0.7]
z = '*' * 80


class Star(object):
    def __init__(self, Sys, clp=cl_sn, m1p=m1_sn, m2p=m2_sn, m3p=m3_sn, z=z):
        self.cl_var = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
        self.cl_ch1 = np.random.choice(self.cl_var, p=clp)
        self.cl_ch2 = np.random.choice(self.cl_var, p=clp)
        self.mOBAF_var = ['150-265', '100-149', '50-99']
        self.mFGK_var = ['50-99', '10-49', '5-9', '1-4', '0.1-0.99']
        self.mM_var = ['150-265', '100-149', '50-99', '1-4', '0.1-0.99']

        def mOBAF_checker(n):
            if n == 1:
                if self.m_ch_1 == '150-265':
                    self.m1 = np.round(random.uniform(150, 265), decimals=2)
                elif self.m_ch_1 == '100-149':
                    self.m1 = np.round(random.uniform(100, 149), decimals=2)
                elif self.m_ch_1 == '50-99':
                    self.m1 = np.round(random.uniform(50, 99), decimals=2)
            elif n == 2:
                if self.m_ch_2 == '150-265':
                    self.m2 = np.round(random.uniform(150, 265), decimals=2)
                elif self.m_ch_2 == '100-149':
                    self.m2 = np.round(random.uniform(100, 149), decimals=2)
                elif self.m_ch_2 == '50-99':
                    self.m2 = np.round(random.uniform(50, 99), decimals=2)

        def mFGK_checker(n):
            if n == 1:
                if self.m_ch_1 == '50-99':
                    self.m1 = np.round(random.uniform(50, 99), decimals=2)
                elif self.m_ch_1 == '10-49':
                    self.m1 = np.round(random.uniform(10, 49), decimals=2)
                elif self.m_ch_1 == '5-9':
                    self.m1 = np.round(random.uniform(5, 9), decimals=2)
                elif self.m_ch_1 == '1-4':
                    self.m1 = np.round(random.uniform(1, 4), decimals=2)
                elif self.m_ch_1 == '0.1-0.99':
                    self.m1 = np.round(random.uniform(0.1, 0.99), decimals=2)
            elif n == 2:
                if self.m_ch_2 == '50-99':
                    self.m2 = np.round(random.uniform(50, 99), decimals=2)
                elif self.m_ch_2 == '10-49':
                    self.m2 = np.round(random.uniform(10, 49), decimals=2)
                elif self.m_ch_2 == '5-9':
                    self.m2 = np.round(random.uniform(5, 9), decimals=2)
                elif self.m_ch_2 == '1-4':
                    self.m2 = np.round(random.uniform(1, 4), decimals=2)
                elif self.m_ch_2 == '0.1-0.99':
                    self.m2 = np.round(random.uniform(0.1, 0.99), decimals=2)

        def mM_checker(n):
            if n == 1:
                if self.m_ch_1 == '150-265':
                    self.m1 = np.round(random.uniform(150, 265), decimals=2)
                elif self.m_ch_1 == '100-149':
                    self.m1 = np.round(random.uniform(100, 149), decimals=2)
                elif self.m_ch_1 == '50-99':
                    self.m1 = np.round(random.uniform(50, 99), decimals=2)
                elif self.m_ch_1 == '1-4':
                    self.m1 = np.round(random.uniform(1, 4), decimals=2)
                elif self.m_ch_1 == '0.1-0.99':
                    self.m1 = np.round(random.uniform(0.1, 0.99), decimals=2)
            elif n == 2:
                if self.m_ch_2 == '150-265':
                    self.m2 = np.round(random.uniform(150, 265), decimals=2)
                elif self.m_ch_2 == '100-149':
                    self.m2 = np.round(random.uniform(100, 149), decimals=2)
                elif self.m_ch_2 == '50-99':
                    self.m2 = np.round(random.uniform(50, 99), decimals=2)
                elif self.m_ch_2 == '1-4':
                    self.m2 = np.round(random.uniform(1, 4), decimals=2)
                elif self.m_ch_2 == '0.1-0.99':
                    self.m2 = np.round(random.uniform(0.1, 0.99), decimals=2)

        def mOBAF_mFGK_checker(n):
            if n == 1:
                if self.ch_1 == 'mOBAF':
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.ch_1 == 'mFGK':
                    self.m_ch_1 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(1)
            elif n == 2:
                if self.ch_2 == 'mOBAF':
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.ch_2 == 'mFGK':
                    self.m_ch_2 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(2)

        def get_temp_m(obj, n, s_n):
            if n == 1:
                if self.cl_ch1 == 'O':
                    self.t1 = random.randint(30000, 60000)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch1 == 'B':
                    self.t1 = random.randint(10000, 29999)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch1 == 'A':
                    self.t1 = random.randint(7500, 9999)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch1 == 'F':
                    self.t1 = random.randint(6000, 7499)
                    self.ch_1 = np.random.choice(['mOBAF', 'mFGK'])
                    mOBAF_mFGK_checker(1)
                elif self.cl_ch1 == 'G':
                    self.t1 = random.randint(5000, 5999)
                    self.m_ch_1 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(1)
                elif self.cl_ch1 == 'K':
                    self.t1 = random.randint(3500, 4999)
                    self.m_ch_1 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(1)
                elif self.cl_ch1 == 'M':
                    self.t1 = random.randint(2000, 3499)
                    self.m_ch_1 = np.random.choice(self.mM_var, p=m3p)
                    mM_checker(1)
                self.nst1 = Sys.get_ns(obj)
                self.s = s_n

            elif n == 2:
                if self.cl_ch2 == 'O':
                    self.t2 = random.randint(30000, 60000)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch2 == 'B':
                    self.t2 = random.randint(10000, 29999)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch2 == 'A':
                    self.t2 = random.randint(7500, 9999)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch2 == 'F':
                    self.t2 = random.randint(6000, 7499)
                    self.ch_2 = np.random.choice(['mOBAF', 'mFGK'])
                    mOBAF_mFGK_checker(2)
                elif self.cl_ch2 == 'G':
                    self.t2 = random.randint(5000, 5999)
                    self.m_ch_2 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(2)
                elif self.cl_ch2 == 'K':
                    self.t2 = random.randint(3500, 4999)
                    self.m_ch_2 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(2)
                elif self.cl_ch2 == 'M':
                    self.t2 = random.randint(2000, 3499)
                    self.m_ch_2 = np.random.choice(self.mM_var, p=m3p)
                    mM_checker(2)
                self.nst2 = Sys.get_ns(obj)
                self.s = s_n

        def k_t(temp):
            return temp-271

        if Sys.get_obj('St') is None:
            self.s = None
        elif Sys.get_obj('St') == [1]:
            get_temp_m(obj=1, n=1, s_n=1)
            self.t1 = k_t(self.t1)
        elif Sys.get_obj('St') == [3]:
            get_temp_m(obj=3, n=1, s_n=1)
            self.t1 = k_t(self.t1)
        elif Sys.get_obj('St') == [1, 2]:
            get_temp_m(obj=1, n=1, s_n=2)
            get_temp_m(obj=2, n=2, s_n=2)
            self.t1 = k_t(self.t1)
            self.t2 = k_t(self.t2)

    def __num_error(self, number):
            self.err1 = 'Вы ввели некорректный номер звезды'
            self.err2 = 'Помните, что нужно писать '
            self.err3 = 'порядковый номер объекта данного типа'
            if number == 1:
                self.err4 = 'В данном случае вы можете написать только "1"'
            elif number == 2:
                self.err4 = 'В данном случае вы можете написать только "1"/"2"'
            self.err = f'{self.err1}\n{self.err2}{self.err3}\n{self.err4}'
            print(f'{z}\n{self.err}\n{z}')

    def __multiple_form(self, n, form):
        if form == 't':
            if int(str(n)[-1]) == 0:
                return 'градусов Цельсия'
            elif int(str(n)[-1]) == 1:
                return 'градус Цельсия'
            elif int(str(n)[-1]) == 2:
                return 'градуса Цельсия'
            elif int(str(n)[-1]) == 3:
                return 'градуса Цельсия'
            elif int(str(n)[-1]) == 4:
                return 'градуса Цельсия'
            elif int(str(n)[-1]) == 5:
                return 'градусов Цельсия'
            elif int(str(n)[-1]) == 6:
                return 'градусов Цельсия'
            elif int(str(n)[-1]) == 7:
                return 'градусов Цельсия'
            elif int(str(n)[-1]) == 8:
                return 'градусов Цельсия'
            elif int(str(n)[-1]) == 9:
                return 'градусов Цельсия'
        elif form == 'm':
            if int(str(n)[-1]) == 1:
                return 'солнечной единицы'
            else:
                return 'солнечных единиц'

    def _multi_single_error(self, n):
        if self.s is None:
            return [True, True]
        elif self.s == 2 and n is 'all':
            return [True, False]
        elif self.s == 1 and n != 1:
            return [True, True]
        elif self.s == 2 and n != 1 and n != 2:
            return [True, True]
        elif self.s == 1 or self.s == 2 and n == 1:
            return [False, True]
        elif self.s == 2 and n == 2:
            return [False, True]

    def _get_class_time(self, n):
        if n == 1 and self.s is not None:
            if self.cl_ch1 == 'O':
                return 2.5
            elif self.cl_ch1 == 'B':
                return 5
            elif self.cl_ch1 == 'A':
                return 7.5
            elif self.cl_ch1 == 'F':
                return 10
            elif self.cl_ch1 == 'G':
                return 25
            elif self.cl_ch1 == 'K':
                return 50
            elif self.cl_ch1 == 'M':
                return 75
        elif n == 2 and self.s == 2:
            if self.cl_ch2 == 'O':
                return 2.5
            elif self.cl_ch2 == 'B':
                return 5
            elif self.cl_ch2 == 'A':
                return 7.5
            elif self.cl_ch2 == 'F':
                return 10
            elif self.cl_ch2 == 'G':
                return 25
            elif self.cl_ch2 == 'K':
                return 50
            elif self.cl_ch2 == 'M':
                return 75

    def help_st(self, h_en):
        if h_en is False:
            if self.s is None:
                self.h1 = 'В данной системе нет звезд для исследования'
                self.h2 = 'Попробуйте исследовать систему, черные дыры'
                self.h3 = ' или совершить прыжок'
                print(f'{z}\n{self.h1}\n{self.h2}{self.h3}\n{z}')
            elif self.s == 1:
                self.h1 = 'В данной системе есть одна звезда для исследования'
                self.h2 = 'Вы можете написать "1" для её исследования'
                print(f'{z}\n{self.h1}\n{self.h2}\n{z}')
            elif self.s == 2:
                self.h1 = 'В данной системе есть две звезды для исследования'
                self.h2 = 'Вы можете написать "1" или "2" для исследования '
                self.h3 = 'одной из них'
                print(f'{z}\n{self.h1}\n{self.h2}{self.h3}\n{z}')
        elif h_en is True:
            if self.s is None:
                self.e1 = 'В данной системе нет звезд для подзарядки'
                self.e2 = 'Если у вас не хватает энергии на следующий прыжок'
                self.e3 = 'То к сожалению это конец вашего путешествия'
                self.e4 = 'Напишите "Конец" или "Выход", чтобы увидеть титры'
                print(f'{z}\n{self.e1}\n{self.e2}\n{self.e3}\n{self.e4}\n{z}')
            elif self.s == 1:
                self.e1 = 'В данной системе есть одна звезда для подзарядки'
                self.e2 = 'Вы можете написать "1" для зарядки от неё'
                print(f'{z}\n{self.e1}\n{self.e2}\n{z}')
            elif self.s == 2:
                self.e1 = 'В данной системе есть две звезды для подзарядки'
                self.e2 = 'Вы можете написать "1" или "2" для зарядки от '
                self.e3 = 'одной из них'
                print(f'{z}\n{self.e1}\n{self.e2}{self.e3}\n{z}')

    def get_enrg(self, n):
        if n == 1 and self.s is not None:
            if self.cl_ch1 == 'O':
                for i in tqdm(range(250)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'B':
                for i in tqdm(range(500)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'A':
                for i in tqdm(range(750)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'F':
                for i in tqdm(range(1000)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'G':
                for i in tqdm(range(2500)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'K':
                for i in tqdm(range(5000)):
                    time.sleep(0.01)
            elif self.cl_ch1 == 'M':
                for i in tqdm(range(7500)):
                    time.sleep(0.01)
        elif n == 2 and self.s == 2:
            if self.cl_ch2 == 'O':
                for i in tqdm(range(250)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'B':
                for i in tqdm(range(500)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'A':
                for i in tqdm(range(750)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'F':
                for i in tqdm(range(1000)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'G':
                for i in tqdm(range(2500)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'K':
                for i in tqdm(range(5000)):
                    time.sleep(0.01)
            elif self.cl_ch2 == 'M':
                for i in tqdm(range(7500)):
                    time.sleep(0.01)

    def examine_st(self, n):
        if self.s is None:
            self.ex_err = 'В данной системе нет звезд для исследования'
            print(f'{z}\n{self.ex_err}\n{z}')
        elif self.s == 2 and n == 'all':
            self.gr1 = self.__multiple_form(self.t1, form='t')
            self.gr2 = self.__multiple_form(self.t2, form='t')
            self.form1 = self.__multiple_form(self.m1, form='m')
            self.form2 = self.__multiple_form(self.m2, form='m')
            self.desc1 = f'{self.nst1} - это звезда класса {self.cl_ch1}.'
            self.desc2 = f'Имеет температуру {self.t1} {self.gr1}'
            self.desc3 = f'И массу {self.m1} {self.form1}'
            print(f'{z}\n{self.desc1}\n{self.desc2}\n{self.desc3}\n{z}')
            self.desc4 = f'{self.nst2} - это звезда класса {self.cl_ch2}.'
            self.desc5 = f'Имеет температуру {self.t2} {self.gr2}'
            self.desc6 = f'И массу {self.m2} {self.form2}'
            print(f'{self.desc1}\n{self.desc2}\n{self.desc3}\n{z}')
        elif self.s == 1 and n == 'all':
            self.ex_err = 'В данной системе находится только одна звезда'
            print(f'{z}\n{self.ex_err}\n{z}')
        elif self.s == 1 and n != 1:
            self.__num_error(1)
        elif self.s == 2 and n != 1 and n != 2:
            self.__num_error(2)
        elif self.s == 1 or self.s == 2 and n == 1:
            self.gr1 = self.__multiple_form(self.t1, form='t')
            self.form1 = self.__multiple_form(self.m1, form='m')
            self.desc1 = f'{self.nst1} - это звезда класса {self.cl_ch1}.'
            self.desc2 = f'Имеет температуру {self.t1} {self.gr1}'
            self.desc3 = f'И массу {self.m1} {self.form1}'
            print(f'{z}\n{self.desc1}\n{self.desc2}\n{self.desc3}\n{z}')
        elif self.s == 2 and n == 2:
            self.gr2 = self.__multiple_form(self.t2 , form='t')
            self.form2 = self.__multiple_form(self.m2, form='m')
            self.desc4 = f'{self.nst2} - это звезда класса {self.cl_ch2}.'
            self.desc5 = f'Имеет температуру {self.t2} {self.gr2}'
            self.desc6 = f'И массу {self.m2} {self.form2}'
