import numpy as np
import time
import os

z = '*' * 80


def titles(hard, start, end, j, csys, cst, csts, cbh, cbhs, h=False):
    end = time.time()
    tit1 = f'{z}\nБыла пройдена очередная веха в исследовании космоса\n{z}'
    tit2 = 'Разработчик: Vadim Fedulov'
    tit3 = 'Год 2019, v1.0 (fix), Python3.7.2'
    tit4 = f'{z}\nОсобые благодарности: GLaDIS, Даше, Насте и Лесе\n{z}'
    if hard is True:
        res1 = f'Уровень сложности: Hard (с прыжка {h})'
    elif hard is False:
        res1 = 'Уровень сложности: Normal'
    res2 = f'Всего {np.round((end-start)/60, decimals=2)} минут в игре'
    res3 = f'Всего прыжков совершено: {j}'
    res4 = f'Всего систем исследовано: {csys}'
    res5 = f'Всего звезд исследовано: {cst}'
    res6 = f'Всего звезд исследовано совместно: {csts}'
    res7 = f'Всего черных дыр исследовано: {cbh}'
    res8 = f'Всего черных дыр исследовано совместно: {cbhs}'
    print(tit1)
    time.sleep(0.75)
    print(tit2)
    time.sleep(0.75)
    print(tit3)
    time.sleep(0.75)
    print(tit4)
    time.sleep(0.75)
    print(res1)
    time.sleep(0.3)
    print(res2)
    time.sleep(0.3)
    print(res3)
    time.sleep(0.3)
    print(res4)
    time.sleep(0.3)
    print(res5)
    time.sleep(0.3)
    print(res6)
    time.sleep(0.3)
    print(res7)
    time.sleep(0.3)
    print(res8)
    time.sleep(0.3)
    ask = input(f'{z}\nЗаписать ваши результаты в results.txt? Д(а)/Н:\n{z}\n')
    if ask.lower() == 'д' or ask.lower() == 'да':
        if not os.path.isfile('./results.txt'):
            pass
        else:
            in1 = 'Файл results.txt уже существует'
            in2 = 'Переместите или переименуйте его или он будет перезаписан'
            in3 = 'Нажмите Ввод, чтобы продолжить...'
            input(f'{z}\n{in1}\n{in2}\n{in3}\n{z}\n')

        try:
            if not os.path.isfile('./results.txt'):
                rewrite = False
            else:
                rewrite = True
            file = open('results.txt', 'w')
            file.write(f'{res1}\n')
            file.write(f'{res2}\n')
            file.write(f'{res3}\n')
            file.write(f'{res4}\n')
            file.write(f'{res5}\n')
            file.write(f'{res6}\n')
            file.write(f'{res7}\n')
            file.write(f'{res7}')
        except:
            print(f'{z}\nЧто-то пошло не так во время записи файла...\n{z}')
        else:
            r = 'results.txt'
            if rewrite is False:
                print(f'{z}\nРезультаты были успешно записаны в {r}\n{z}')
            elif rewrite is True:
                print(f'{z}\nРезультаты в {r} были успешно перезаписаны\n{z}')
        finally:
            file.close()
