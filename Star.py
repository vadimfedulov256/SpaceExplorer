import numpy as np
import random
import time
from tqdm import tqdm

cl_sn = [0.05, 0.1, 0.15, 0.2, 0.2, 0.25, 0.05]
m1_sn = [0.05, 0.25, 0.7]
m2_sn = [0.15, 0.2, 0.25, 0.3, 0.1]
m3_sn = [0.05, 0.05, 0.1, 0.1, 0.7]


class Star(object):
    def __init__(self, StarSystem, clp=cl_sn, m1p=m1_sn, m2p=m2_sn, m3p=m3_sn):
        self.cl_var = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
        self.cl_ch_1 = np.random.choice(self.cl_var, p=clp)
        self.cl_ch_2 = np.random.choice(self.cl_var, p=clp)
        self.mOBAF_var = ['150-265', '100-149', '50-99']
        self.mFGK_var = ['50-99', '10-49', '5-9', '1-4', '0.1-0.99']
        self.mM_var = ['150-265', '100-149', '50-99', '1-4', '0.1-0.99']
        self.z = '*' * 80

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
                if self.cl_ch_1 == 'O':
                    self.t1 = random.randint(30000, 60000)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch_1 == 'B':
                    self.t1 = random.randint(10000, 29999)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch_1 == 'A':
                    self.t1 = random.randint(7500, 9999)
                    self.m_ch_1 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(1)
                elif self.cl_ch_1 == 'F':
                    self.t1 = random.randint(6000, 7499)
                    self.ch_1 = np.random.choice(['mOBAF', 'mFGK'])
                    mOBAF_mFGK_checker(1)
                elif self.cl_ch_1 == 'G':
                    self.t1 = random.randint(5000, 5999)
                    self.m_ch_1 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(1)
                elif self.cl_ch_1 == 'K':
                    self.t1 = random.randint(3500, 4999)
                    self.m_ch_1 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(1)
                elif self.cl_ch_1 == 'M':
                    self.t1 = random.randint(2000, 3499)
                    self.m_ch_1 = np.random.choice(self.mM_var, p=m3p)
                    mM_checker(1)
                self.n_s_1 = StarSystem.get_ns(obj)
                self.s = s_n

            elif n == 2:
                if self.cl_ch_2 == 'O':
                    self.t2 = random.randint(30000, 60000)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch_2 == 'B':
                    self.t2 = random.randint(10000, 29999)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch_2 == 'A':
                    self.t2 = random.randint(7500, 9999)
                    self.m_ch_2 = np.random.choice(self.mOBAF_var, p=m1p)
                    mOBAF_checker(2)
                elif self.cl_ch_2 == 'F':
                    self.t2 = random.randint(6000, 7499)
                    self.ch_2 = np.random.choice(['mOBAF', 'mFGK'])
                    mOBAF_mFGK_checker(2)
                elif self.cl_ch_2 == 'G':
                    self.t2 = random.randint(5000, 5999)
                    self.m_ch_2 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(2)
                elif self.cl_ch_2 == 'K':
                    self.t2 = random.randint(3500, 4999)
                    self.m_ch_2 = np.random.choice(self.mFGK_var, p=m2p)
                    mFGK_checker(2)
                elif self.cl_ch_2 == 'M':
                    self.t2 = random.randint(2000, 3499)
                    self.m_ch_2 = np.random.choice(self.mM_var, p=m3p)
                    mM_checker(2)
                self.n_s_2 = StarSystem.get_ns(obj)
                self.s = s_n

        def k_t(temp):
            return temp-271

        if StarSystem.get_obj('St') is None:
            self.s = None
        elif StarSystem.get_obj('St') == [1]:
            get_temp_m(obj=1, n=1, s_n=1)
            self.t1 = k_t(self.t1)
        elif StarSystem.get_obj('St') == [3]:
            get_temp_m(obj=3, n=1, s_n=1)
            self.t1 = k_t(self.t1)
        elif StarSystem.get_obj('St') == [1, 2]:
            get_temp_m(obj=1, n=1, s_n=2)
            get_temp_m(obj=2, n=2, s_n=2)
            self.t1 = k_t(self.t1)
            self.t2 = k_t(self.t2)

    def __num_error(self, number):
        if number == 1:
            self.a1 = 'Вы ввели некорректный номер звезды'
            self.b1 = 'Помните, что нужно писать '
            self.c1 = 'порядковый номер объекта данного типа'
            self.d1 = 'В данном случае вы можете написать только "1"'
            print(self.z)
            print(self.a1+'\n'+self.b1+self.c1+'\n'+self.d1)
            print(self.z)
        elif number == 2:
            self.a2 = 'Вы ввели некорректный номер звезды'
            self.b2 = 'Помните, что нужно писать '
            self.c2 = 'порядковый номер объекта данного типа'
            self.d2 = 'В данном случае вы можете написать только "1"/"2"'
            print(self.z)
            print(self.a2+'\n'+self.b2+self.c2+'\n'+self.d2)
            print(self.z)

    def __multiple_form(self, n):
        if int(str(n)[-1]) == 0:
            return ' градусов Цельсия'
        elif int(str(n)[-1]) == 1:
            return ' градус Цельсия'
        elif int(str(n)[-1]) == 2:
            return ' градуса Цельсия'
        elif int(str(n)[-1]) == 3:
            return ' градуса Цельсия'
        elif int(str(n)[-1]) == 4:
            return ' градуса Цельсия'
        elif int(str(n)[-1]) == 5:
            return ' градусов Цельсия'
        elif int(str(n)[-1]) == 6:
            return ' градусов Цельсия'
        elif int(str(n)[-1]) == 7:
            return ' градусов Цельсия'
        elif int(str(n)[-1]) == 8:
            return ' градусов Цельсия'
        elif int(str(n)[-1]) == 9:
            return ' градусов Цельсия'

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
            if self.cl_ch_1 == 'O':
                return 2.5
            elif self.cl_ch_1 == 'B':
                return 5
            elif self.cl_ch_1 == 'A':
                return 7.5
            elif self.cl_ch_1 == 'F':
                return 10
            elif self.cl_ch_1 == 'G':
                return 25
            elif self.cl_ch_1 == 'K':
                return 50
            elif self.cl_ch_1 == 'M':
                return 75
        elif n == 2 and self.s == 2:
            if self.cl_ch_2 == 'O':
                return 2.5
            elif self.cl_ch_2 == 'B':
                return 5
            elif self.cl_ch_2 == 'A':
                return 7.5
            elif self.cl_ch_2 == 'F':
                return 10
            elif self.cl_ch_2 == 'G':
                return 25
            elif self.cl_ch_2 == 'K':
                return 50
            elif self.cl_ch_2 == 'M':
                return 75
        elif self.s == 1 and n != 1:
            self.__num_error(1)
        elif self.s == 2 and n != 1 and n != 2:
            self.__num_error(2)

    def help_st(self, h_en):
        if h_en is False:
            if self.s is None:
                self.h1 = 'В данной системе нет звезд для исследования'
                self.h2 = 'Попробуйте исследовать систему, черные дыры'
                self.h3 = ' или совершить прыжок'
                print(self.z+'\n'+self.h1+'\n'+self.h2+self.h3+'\n'+self.z)
            elif self.s == 1:
                self.h1 = 'В данной системе есть одна звезда для исследования'
                self.h2 = 'Вы можете написать "1" для её исследования'
                print(self.z+'\n'+self.h1+'\n'+self.h2+'\n'+self.z)
            elif self.s == 2:
                self.h1 = 'В данной системе есть две звезды для исследования'
                self.h2 = 'Вы можете написать "1" или "2" для исследования '
                self.h3 = 'одной из них'
                print(self.z+'\n'+self.h1+'\n'+self.h2+self.h3+'\n'+self.z)
        elif h_en is True:
            if self.s is None:
                self.e1 = 'В данной системе нет звезд для подзарядки'
                self.e2 = 'Если у вас не хватает энергии на следующий прыжок'
                self.e3 = 'То к сожалению это конец вашего путешествия'
                self.e4 = 'Напишите "Конец" или "Выход", чтобы увидеть титры'
                print(self.z)
                print(self.e1+'\n'+self.e2+'\n'+self.e3+'\n'+self.e4)
                print(self.z)
            elif self.s == 1:
                self.e1 = 'В данной системе есть одна звезда для подзарядки'
                self.e2 = 'Вы можете написать "1" для зарядки от неё'
                print(self.z+'\n'+self.e1+'\n'+self.e2+'\n'+self.z)
            elif self.s == 2:
                self.e1 = 'В данной системе есть две звезды для подзарядки'
                self.e2 = 'Вы можете написать "1" или "2" для зарядки от '
                self.e3 = 'одной из них'
                print(self.z+'\n'+self.e1+'\n'+self.e2+self.e3+'\n'+self.z)

    def get_enrg(self, n):
        if n == 1 and self.s is not None:
            if self.cl_ch_1 == 'O':
                for i in tqdm(range(250)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'B':
                for i in tqdm(range(500)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'A':
                for i in tqdm(range(750)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'F':
                for i in tqdm(range(1000)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'G':
                for i in tqdm(range(2500)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'K':
                for i in tqdm(range(5000)):
                    time.sleep(0.01)
            elif self.cl_ch_1 == 'M':
                for i in tqdm(range(7500)):
                    time.sleep(0.01)
        elif n == 2 and self.s == 2:
            if self.cl_ch_2 == 'O':
                for i in tqdm(range(250)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'B':
                for i in tqdm(range(500)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'A':
                for i in tqdm(range(750)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'F':
                for i in tqdm(range(1000)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'G':
                for i in tqdm(range(2500)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'K':
                for i in tqdm(range(5000)):
                    time.sleep(0.01)
            elif self.cl_ch_2 == 'M':
                for i in tqdm(range(7500)):
                    time.sleep(0.01)

    def examine_st(self, n):
        if self.s is None:
            print(self.z)
            print('В данной системе нет звезд для исследования')
            print(self.z)
        elif self.s == 2 and n is 'all':
            self.gr1 = self.__multiple_form(self.t1)
            self.gr2 = self.__multiple_form(self.t2)
            self.t1 = str(self.t1)
            self.t2 = str(self.t2)
            self.m1 = str(self.m1)
            self.m2 = str(self.m2)
            print(self.z)
            self.desc_1 = self.n_s_1+' - это звезда класса '+self.cl_ch_1
            print(self.desc_1+'. ')
            self.desc_2 = 'Имеет температуру '+self.t1+self.gr1
            print(self.desc_2)
            self.desc_3 = 'И массу '+self.m1+' солнечных единиц'
            print(self.desc_3)
            print(self.z)
            self.desc_4 = self.n_s_2+' - это звезда класса '+self.cl_ch_2
            print(self.desc_4+'. ')
            self.desc_5 = 'Имеет температуру '+self.t2+self.gr2
            print(self.desc_5)
            self.desc_6 = 'И массу '+self.m2+' солнечных единиц'
            print(self.desc_6)
            print(self.z)
        elif self.s == 1 and n is 'all':
            self.a = 'В данной системе находится только одна звезда'
            print(self.z+'\n'+self.a+'\n'+self.z)
            return True, True
        elif self.s == 1 and n != 1:
            self.__num_error(1)
        elif self.s == 2 and n != 1 and n != 2:
            self.__num_error(2)
            return True, True
        elif self.s == 1 or self.s == 2 and n == 1:
            self.gr1 = self.__multiple_form(self.t1)
            self.t1 = str(self.t1)
            self.m1 = str(self.m1)
            print(self.z)
            self.desc_1 = self.n_s_1+' - это звезда класса '+self.cl_ch_1
            print(self.desc_1+'. ')
            self.desc_2 = 'Имеет температуру '+self.t1+self.gr1
            print(self.desc_2)
            self.desc_3 = 'И массу '+self.m1+' солнечных единиц'
            print(self.desc_3)
            print(self.z)
        elif self.s == 2 and n == 2:
            self.gr2 = self.__multiple_form(self.t2)
            self.t2 = str(self.t2)
            self.m2 = str(self.m2)
            print(self.z)
            self.desc_4 = self.n_s_2+' - это звезда класса '+self.cl_ch_2
            print(self.desc_4+'. ')
            self.desc_5 = 'Имеет температуру '+self.t2+self.gr2
            print(self.desc_5)
            self.desc_6 = 'И массу '+self.m2+' солнечных единиц'
            print(self.desc_6)
            print(self.z)
