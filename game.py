import string
import random
import time

from tqdm import tqdm

from System import System
from BlackHole import BlackHole
from Star import Star
import achivements as ach
import titles as t
from z import change_z

cj = 0
csys = 0
cst = 0
csts = 0
cbh = 0
cbhs = 0
hj = None

#enrg = random.randint(500, 700) * 10
enrg = 1000
change_nj = True
z = change_z(enrg)

res = False
p_res = [False, False, False]
sp_res = [False, False, False]

hard = False

err_single_str = 'Вы ввели знак вместо номера'
err_multiple_str = 'Вы ввели знаки вместо номера'

if __name__ == "__main__":
    l = '''|     _   __                      __   _____                      |
|    / | / /__  __  ___________ _/ /  / ___/____  ____ _________  |
|   /  |/ / _ \/ / / / ___/ __ `/ /   \__ \/ __ \/ __ `/ ___/ _ \ |
|  / /|  /  __/ /_/ / /  / /_/ / /   ___/ / /_/ / /_/ / /__/  __/ |
| /_/ |_/\___/\__,_/_/   \__,_/_/   /____/ .___/\__,_/\___/\___/  |
|                                       /_/                       |
                                                     v1.2(beta) ''')
    print(f'{z}\nДобро пожаловать в\n{l}\n{z}')

def riskjumping(time):
    print(f'{z}\nОпределяем траекторию полета...')
    for i in tqdm(range(time[0])):
        time.sleep(0.01)
    print(f'{z}\nОпределяем время и место сброса балласта...')
    for i in tqdm(range(time[1])):
        time.sleep(0.01)
    print(f'{z}\nНачинаем полет...')
    for i in tqdm(range(time[2]):
        time.sleep(0.01)
    print(z)

def end(hard, start, cj, csys, cst, csts, cbh, cbhs, hj):
    if hard and hj is not None:
        t.titles(hard, start, cj, csys, cst, csts, cbh, cbhs, hj)
    else:
        hard = h
        start = s
        t.titles(hard, start, cj, csys, cst, csts, cbh, cbhs)


start = time.time()

Sys = System(s_p=[0, 0, 0, 1, 0, 0, 0])
St = Star(Sys)
Bh = BlackHole(Sys)

while True:
    if change_nj:
        nj = random.randint(30, 80) * 100
    change_nj = False
    act = input('Напишите ваше действие: ')
    if act.lower() == 'прыжок':
        j1 = f'Для прыжка потребуется {nj} единиц энергии'
        j2 = f'У вас {enrg} единиц энергии'
        j3 = 'Вы действительно хотите совершить прыжок? Д(а)/Н'
        app = input(f'{z}\n{j1}\n{j2}\n{j3}\n{z}\n')
        if app.lower() == 'д' or app.lower() == 'да':
            if enrg < nj:
                if Sys.get_obj('St') is not None:
                    zj1 = 'У вас недостаточно энергии для совершения прыжка'
                    zj2 = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{zj1}\n{zj2}\n{z}')
                elif Sys.get_obj('St') is None and Bh.b == 1:
                    diff = nj - enrg
                    prob1 = Bh.get_prob(1, diff)
                    zj1 = 'У вас недостаточно энергии для совершения прыжка'
                    zj2 = 'А в данной системе совсем нет звезд для зарядки'
                    if Sys.get_obj('Bh') == [1]:
                        if p_res[0]:
                            b1 = Sys.get_ns(1)
                        else:
                            b1 = 1
                    elif Sys.get_obj('Bh') == [2]:
                        if p_res[1]:
                            b1 = Sys.get_ns(2)
                        else:
                            b1 = 2
                    elif Sys.get_obj('Bh') == [3]:
                        if p_res[2]:
                            b1 = Sys.get_ns(3)
                        else:
                            b1 = 3
                    zj3 = f'Тем не менее присутствует черная дыра {b1}'
                    zj4 = 'Вероятность совершить удачный прыжок, пройдя вблизи'
                    zj5 = f' черной дыры {b1} равна {prob1}%'
                    print(f'{z}\n{zj1}\n{zj2}\n{zj3}\n{zj4}{zj5}')
                    ask = 'Вы действительно хотите рискнуть своими данными? '
                    app = input(f'{ask}Д(а)/Н\n{z}\n')
                    if app.lower() == 'д' or app.lower() == 'да':
                        riskjumping(Bh.get_t(bh))
                        enrg -= diff
                        if Bh.riskjump(1, diff, prob1):
                            pass
                        else:
                            print('NoeargreiagnIREOGREUGVJOEIRUHY/...' * 1000)
                            break
                    else:
                        end(hard, start, cj, csys, cst, csts, cbh, cbhs, hj)
                        break
                elif Sys.get_obj('St') is None and Bh.b == 2:
                    diff = nj - enrg
                    prob1 = Bh.get_prob(1, diff)
                    prob2 = Bh.get_prob(2, diff)
                    zj1 = 'У вас недостаточно энергии для совершения прыжка'
                    zj2 = 'А в данной системе совсем нет звезд для зарядки'
                    if p_res[0]:
                        b1 = Sys.get_ns(1)
                    else:
                        b1 = 1
                    if p_res[1]:
                        b2 = Sys.get_ns(2)
                    else:
                        b2 = 2
                    zj3 = f'Тем не менее присутствуют черные дыры {b1}, {b2}'
                    zj4 = 'Вероятности совершить удачный прыжок пройдя вблизи'
                    zj5 = f' черной дыры {b1} и {b2}'
                    zj6 = f'Cоответственно равны {prob1}% и {prob2}%'
                    print(f'{z}\n{zj1}\n{zj2}\n{zj3}\n{zj4}{zj5}\n{zj6}')
                    ask = 'Вы действительно хотите рискнуть своими данными? '
                    app = input(f'{ask}Д(а)/Н\n{z}\n')
                    if app.lower() == 'д' or app.lower() == 'да':
                        bh = input('Напишите номер черной дыры для прыжка: ')
                        if bh.lower() == 'помощь':
                            Bh.help_bh(h_j=True)
                        else:
                            try:
                                bh = int(bh)  # exception occures here
                                prob = Bh.get_prob(bh, diff)
                                riskjumping(Bh.get_t(bh))
                                enrg -= diff
                                if Bh.riskjump(bh, diff, prob):
                                    pass
                                else:
                                    print('NoeargreiagnIREOGREUGVJO...' * 1000)
                                    break
                            except:
                                if len(list(bh)) == 1:
                                    print(f'{z}\n{err_single_str}\n{z}')
                                elif len(list(bh)) > 1:
                                    print(f'{z}\n{err_multiple_str}\n{z}')

            else:
                print(f'{z}\nПрыжок в процессе...')
                for i in tqdm(range(nj)):
                    time.sleep(0.01)
                enrg -= nj
                z = change_z(enrg)
                print(f'{z}\nВы совершили прыжок в другую систему\n{z}')
                change_nj = True
                res = False
                p_res = [False, False, False]
                sp_res = [False, False, False]
                cj += 1
                if hard:  # here definetely will be markov chain in future
                    Sys = System.hard()  # releases
                    St = Star(Sys)
                    Bh = BlackHole(Sys)
                else:
                    Sys = System()
                    St = Star(Sys)
                    Bh = BlackHole(Sys)
                zj1 = f'На прыжок было потрачено {nj} единиц энергии'
                zj2 = f'Теперь у вас {enrg} единиц энергии'
                print(f'{zj1}\n{zj2}\n{z}')
                ach.j(cj)
        else:
            print(f'Отмена прыжка...\n{z}')

    elif act.lower() == 'исследовать':
        react = input('Что именно вы хотите исследовать: ')

        if react.lower() == 'систему':
            sys1 = 'Для исследования системы потребуется 1000 единиц энергии'
            sys2 = f'У вас {enrg} единиц энергии'
            sys3 = 'Вы действительно хотите исследовать систему? Д(а)/Н'
            app = input(f'{z}\n{sys1}\n{sys2}\n{sys3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 1000:
                    zs1 = 'У вас недостаточно энергии для исследования системы'
                    zs2 = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{zs1}\n{zs2}\n{z}')
                else:
                    print(f'{z}\nИсследуем систему...')
                    for i in tqdm(range(1000)):
                        time.sleep(0.01)
                    enrg -= 1000
                    z = change_z(enrg)
                    Sys.examine_sys(z)
                    res = True
                    csys += 1
                    ach.sys(csys)
                    sys = Sys.get_ns('sys')
                    zs1 = f'На исследование системы {sys} '
                    zs2 = 'было потрачено 1000 единиц энергии'
                    zs3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zs1}{zs2}\n{zs3}\n{z}')
            else:
                print(f'Отмена исследования системы...\n{z}')

        elif react.lower() == 'звезду':
            st = input('Напишите номер звезды для исследования: ')
            if st.lower() == 'помощь':
                St.help_st()
            else:
                st1 = f'Для исследования звезды {st} '
                st2 = 'потребуется 250 единиц энергии'
                st3 = f'У вас {enrg} единиц энергии'
                st4 = f'Вы действительно хотите исследовать звезду {st}'
                st5 = '? Д(а)/Н'
                app = input(f'{z}\n{st1}{st2}\n{st3}\n{st4}{st5}\n{z}\n')
                if app.lower() == 'д' or app.lower() == 'да':
                    try:
                        if enrg < 250:
                            zst1 = 'У вас недостаточно энергии '
                            zst2 = 'для исследования звезды'
                            zst3 = 'Попробуйте получить энергию от '
                            zst4 = 'ближайшей звезды'
                            print(f'{z}\n{zst1}{zst2}\n{zst3}{zst4}\n{z}')
                        else:
                            att_st = f'Пытаемся исследовать звезду {st}'
                            print(f'{z}\n{att_st}...')
                            for i in tqdm(range(250)):
                                time.sleep(0.01)
                            enrg -= 250
                            z = change_z(enrg)
                            st = int(st)  # exception occures here
                            St.examine_st(z, st)
                            zst1 = f'На исследование звезды {st} '
                            zst2 = 'было потрачено 250 единиц энергии'
                            zst3 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{zst1}{zst2}\n{zst3}\n{z}')
                            if not St._multi_single_error(st)[0]:
                                p_res[st-1] = True  # learn name
                                sp_res[st-1] = True  # learn speed of charge
                                cst += 1             # (only for St)
                                ach.st(cst)
                    except:
                        if len(list(st)) == 1:
                            print(f'{z}\n{err_single_str}\n{z}')
                        elif len(list(st)) > 1:
                            print(f'{z}\n{err_multiple_str}\n{z}')
                        er_st1 = f'На исследование звезды {st} '
                        er_st2 = 'было потрачено 250 единиц энергии'
                        er_st3 = f'Теперь у вас {enrg} единиц энергии'
                        print(f'{er_st1}{er_st2}\n{er_st3}\n{z}')
                else:
                    print(f'Отмена исследования звезды...\n{z}')

        elif react.lower() == 'звезды':
            sts1 = 'Для исследования звезд потребуется 500 единиц энергии'
            sts2 = f'У вас {enrg} единиц энергии'
            sts3 = 'Вы действительно хотите исследовать звезды? Д(а)/Н'
            app = input(f'{z}\n{sts1}\n{sts2}\n{sts3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 500:
                    zsts1 = 'У вас недостаточно энергии '
                    zsts2 = 'для исследования звезд'
                    zsts3 = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{zsts1}{zsts2}\n{zsts3}\n{z}')
                else:
                    print(f'{z}\nПытаемся исследовать звезды...')
                    for i in tqdm(range(500)):
                        time.sleep(0.01)
                    enrg -= 500
                    z = change_z(enrg)
                    St.examine_st(z, z, 'all')
                    zsts1 = 'На исследование звезд '
                    zsts2 = 'было потрачено 500 единиц энергии'
                    zsts3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zsts1}{zsts2}\n{zsts3}\n{z}')
                    if not St._multi_single_error('all')[1]:
                        p_res[0] = True  # learn names
                        p_res[1] = True
                        sp_res[0] = True  # learn speeds of charge
                        sp_res[1] = True  # (only for Stars)
                        csts += 1
                        ach.sts(csts)
            else:
                print(f'Отмена исследования звезд...\n{z}')

        elif react.lower() == 'черную дыру':
            bh = input('Напишите номер черной дыры для исследования: ')
            if bh.lower() == 'помощь':
                Bh.help_bh()
            else:
                bh1 = f'Для исследования черной дыры {bh} '
                bh2 = 'потребуется 250 единиц энергии'
                bh3 = f'У вас {enrg} единиц энергии'
                bh4 = f'Вы действительно хотите исследовать черную дыру {bh}'
                bh5 = '? Д(а)/Н'
                app = input(f'{z}\n{bh1}{bh2}\n{bh3}\n{bh4}{bh5}\n{z}\n')
                if app.lower() == 'д' or app.lower() == 'да':
                    try:
                        if enrg < 250:
                            zbh1 = 'У вас недостаточно энергии '
                            zbh2 = 'для иследования черной дыры'
                            zbh3 = 'Попробуйте получить энергию '
                            zbh4 = 'от ближайшей звезды'
                            print(f'{z}\n{zbh1}{zbh2}\n{zbh3}{zbh4}\n{z}')
                        else:
                            att_bh = f'Пытаемся исследовать черную дыру {bh}'
                            print(f'{z}\n{att_bh}...')
                            for i in tqdm(range(250)):
                                time.sleep(0.01)
                            enrg -= 250
                            z = change_z(enrg)
                            bh = int(bh)  # exception occures here
                            Bh.examine_bh(z, bh)
                            zbh1 = f'На исследование черной дыры {bh} '
                            zbh2 = 'было потрачено 250 единиц энергии'
                            zbh3 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{zbh1}{zbh2}\n{zbh3}\n{z}')
                            if not Bh._multi_single_error(bh)[0]:
                                p_res[st-1] = True
                                cbh += 1
                                ach.bh(cbh)
                    except:
                        if len(list(bh)) == 1:
                            print(f'{z}\n{err_single_str}\n{z}')
                        elif len(list(bh)) > 1:
                            print(f'{z}\n{err_multiple_str}\n{z}')
                        er_bh1 = f'На исследование черной дыры {bh} '
                        er_bh2 = 'было потрачено 250 единиц энергии'
                        er_bh3 = f'Теперь у вас {enrg} единиц энергии'
                        print(f'{er_bh1}{er_bh2}\n{er_bh3}\n{z}')
                else:
                    print(f'Отмена исследования черной дыры...\n{z}')

        elif react.lower() == 'черные дыры':
            bhs1 = 'Для исследования черных дыр потребуется 500 единиц энергии'
            bhs2 = f'У вас {enrg} единиц энергии'
            bhs3 = 'Вы действительно хотите исследовать черные дыры? Д(а)/Н'
            app = input(f'{z}\n{bhs1}\n{bhs3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 500:
                    zbhs1 = 'У вас недостаточно энергии '
                    zbhs2 = 'для исследования черных дыр'
                    zbhs3 = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{zbhs1}{zbhs2}\n{zbhs3}\n{z}')
                else:
                    print(f'{z}\nПытаемся исследовать черные дыры...')
                    for i in tqdm(range(500)):
                        time.sleep(0.01)
                    enrg -= 500
                    z = change_z(enrg)
                    Bh.examine_bh(z, z, 'all')
                    zbhs1 = 'На исследование черных дыр '
                    zbhs2 = 'было потрачено 500 единиц энергии'
                    zbhs3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zbhs1}{zbhs2}\n{zbhs3}\n{z}')
                    if not Bh._multi_single_error('all')[1]:
                        p_res[0] = True  # learn names
                        p_res[1] = True
                        cbhs += 1
                        ach.bhs(cbhs)
            else:
                print(f'Отмена исследования черных дыр...\n{z}')

        elif react.lower() == 'помощь':
            h1 = 'Список возможных комманд для исследования объектов:'
            h2 = '"Систему", "Звезду", "Звезды", "Черную дыру", "Черные дыры"'
            print(f'{z}\n{h1}\n{h2}\n{z}')

        else:
            print('Непонятен объект исследования, попробуйте еще раз')

    elif act.lower() == 'зарядиться':
        en = input('Выберите звезду для подзарядки: ')
        if en.lower() == 'помощь':
            St.help_st(h_en=True, z=z)
        else:
            try:
                en = int(en)  # exception occures here
                if not St._multi_single_error(en)[0]:
                    if res or p_res[en-1]:
                        nst = Sys.get_ns(en)
                    else:  # we use _multi_single_error earlier to make game
                        nst = en  # easier when charging
                    en1 = f'Зарядка солнечных батарей от звезды {nst} займет '
                    if sp_res[en-1] is True:
                        clt = f'{St._get_class_time(en)} секунд'
                    elif sp_res[en-1] is False:
                        clt = '[Неизвестно] секунд'
                    en2 = 'Вы действительно хотите зарядиться? Д(а)/Н'
                    app = input(f'{z}\n{en1}{clt}\n{en2}\n{z}\n')
                    if app.lower() == 'д' or app.lower() == 'да':
                        print(f'{z}\nЗаряжаемся от звезды {nst}...')
                        St.get_enrg(en)
                        sp_res[en-1] = True  # we will get speed, but not name
                        if enrg + 1000 < 15000:
                            enrg += 1000
                            z = change_z(enrg)
                            zen1 = 'Вы получили 1000 единиц энергии от звезды '
                            zen2 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{z}\n{zen1}{nst}\n{zen2}\n{z}')
                        else:
                            genrg = 15000 - enrg
                            enrg += genrg
                            z = change_z(enrg)
                            zen1 = f'Вы получили получили {genrg} '
                            zen2 = f'единиц энергии от звезды {nst}'
                            zen3 = f'Так как ваш аккумулятор достиг лимита: '
                            zen4 = '15000 единиц энергии'
                            print(f'{z}\n{zen1}{zen2}\n{zen3}{zen4}\n{z}')
                    else:
                        print(f'Отмена зарядки...\n{z}')
                else:
                    St.help_st(h_en=True, z=z)
            except:
                if len(list(str(en))) == 1:
                    print(f'{z}\n{err_single_str}\n{z}')
                elif len(list(str(en))) > 1:
                    print(f'{z}\n{err_multiple_str}\n{z}')

    elif act.lower() == 'энергия':
        print(f'{z}\nВаша энергия равна: {enrg} / 15000\n{z}')

    elif act.lower() == 'помощь':
        eh1 = 'Список возможных комманд:'
        eh2 = '"Прыжок", "Исследовать", "Зарядиться", "Энергия"'
        print(f'{z}\n{eh1}\n{eh2}\n{z}')

    elif act == 'CRAZYMEGAHELL':
        hard = True
        hj = cj
        print(f'{z}\nОООООО МОЯЯЯ ОБОРОООНААААА!!! HARD ВКЛЮЧЕН ;_)\n{z}')

    elif act.lower() == 'выход' or act.lower() == 'конец':
        end(hard, start, cj, csys, cst, csts, cbh, cbhs, hj)
        break

    else:
        print('Непонятно действие, попробуйте еще раз')
