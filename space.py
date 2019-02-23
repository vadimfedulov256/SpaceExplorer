import string
import random
import time
from tqdm import tqdm

from StarSystem import StarSystem
from BlackHole import BlackHole
from Star import Star
import achivements as ach

z = '*' * 80
q = '\n'
jump = 0
e_sys = 0
e_st = 0
e_sts = 0
e_bh = 0
e_bhs = 0
enrg = 5000
change_rj = True
res = False
p_res = [False, False, False]

StSys = StarSystem()
St = Star(StSys)
Bh = BlackHole(StSys)


def titles():
    tit1 = f'{z}\nБыла пройдена очередная веха в исследовании космоса\n{z}'
    tit2 = 'Разработчик: Vadim Fedulov'
    tit3 = 'Год 2019, v0.9, Python3.7.2'
    tit4 = f'{z}\nОсобые благодарности: GLaDIS, Даше, Насте и Лесе\n{z}'
    print(tit1)
    time.sleep(1)
    print(tit2)
    time.sleep(0.75)
    print(tit3)
    time.sleep(0.75)
    print(tit4)
    time.sleep(1)


while True:
    if change_rj is True:
        rj = random.randint(30, 100) * 100
    change_rj = False
    act = input('Напишите ваше действие: ')
    if act.lower() == 'прыжок':
        j1 = f'Для прыжка потребуется {rj} единиц энергии'
        j2 = f'У вас {enrg} единиц энергии'
        j3 = 'Вы действительно хотите совершить прыжок? Д/Н'
        app = input(f'{z}\n{j1}\n{j2}\n{j3}\n{z}\n')
        if app.lower() == 'д' or app.lower() == 'да':
            if enrg < rj:
                a = 'У вас недостаточно энергии для совершения прыжка'
                b = 'Попробуйте получить энергию от ближайшей звезды'
                print(f'{z}\n{a}\n{b}\n{z}')
            else:
                print(f'{z}\nПрыжок в процессе...')
                for i in tqdm(range(rj)):
                    time.sleep(0.01)
                print(f'{z}\nВы совершили прыжок в другую систему\n{z}')
                change_rj = True
                res = False
                p_res = [False, False, False]
                enrg -= rj
                jump += 1
                StSys = StarSystem()
                St = Star(StSys)
                Bh = BlackHole(StSys)
                j1 = 'На прыжок было потрачено '
                j2 = ' единиц энергии'
                j3 = 'Теперь у вас '
                j4 = ' единиц энергии'
                print(f'{j1}{rj}{j2}\n{j3}{enrg}{j4}\n{z}')
                ach.jump(jump)
        else:
            print(f'Отмена прыжка...\n{z}')

    elif act.lower() == 'исследовать':
        react = input('Что именно вы хотите исследовать: ')

        if react.lower() == 'систему':
            s1 = 'Для исследования системы потребуется 1000 единиц энергии'
            s2 = f'У вас {enrg} единиц энергии'
            s3 = 'Вы действительно хотите исследовать систему? Д/Н'
            app = input(f'{z}\n{s1}\n{s2}\n{s3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 1000:
                    a = 'У вас недостаточно энергии для исследования системы'
                    b = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{a}\n{b}\n{z}')
                else:
                    print(f'{z}\nИсследуем систему...')
                    for i in tqdm(range(1000)):
                        time.sleep(0.01)
                    StSys.examine_sys()
                    res = True
                    e_sys += 1
                    ach.e_sys(e_sys)
                    enrg -= 1000
                    sys = StSys.get_ns('sys')
                    zs1 = f'На исследование системы {sys} '
                    zs2 = 'было потрачено 1000 единиц энергии'
                    zs3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zs1}{zs2}\n{zs3}\n{z}')
            else:
                print(f'Отмена исследования системы...\n{z}')

        elif react.lower() == 'звезду':
            st = input('Напишите номер звезды для исследования: ')
            if st.lower() == 'помощь':
                St.help_st(h_en=False)
            else:
                st1 = f'Для исследования звезды {st} '
                st2 = 'потребуется 250 единиц энергии'
                st3 = f'У вас {enrg} единиц энергии'
                st4 = f'Вы действительно хотите исследовать звезду {st}'
                st5 = '? Д/Н'
                app = input(f'{z}\n{st1}{st2}\n{st3}\n{st4}{st5}\n{z}\n')
                if app.lower() == 'д' or app.lower() == 'да':
                    try:
                        if enrg < 250:
                            a = 'У вас недостаточно энергии '
                            b = 'для исследования звезды'
                            c = 'Попробуйте получить энергию от '
                            d = 'ближайшей звезды'
                            print(f'{z}\n{a}{b}\n{c}{d}\n{z}')
                        else:
                            att_st = f'Пытаемся исследовать звезду {st}'
                            print(f'{z}\n{att_st}...')
                            for i in tqdm(range(250)):
                                time.sleep(0.01)
                            st = int(st)
                            St.examine_st(st)
                            enrg -= 250
                            zst1 = f'На исследование звезды {st} '
                            zst2 = 'было потрачено 250 единиц энергии'
                            zst3 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{zst1}{zst2}\n{zst3}\n{z}')
                            if St._multi_single_error(st)[0] is not True:
                                p_res[st-1] = True # we do it only for stars
                                e_st += 1
                                ach.e_st(e_st)
                    except:
                        if len(list(st)) == 1:
                            print(f'{z}\nВы ввели знак вместо номера\n{z}')
                        elif len(list(st)) > 1:
                            print(f'{z}\nВы ввели знаки вместо номера\n{z}')
                        enrg -= 250
                        er_st1 = f'На исследование звезды {st} '
                        er_st2 = 'было потрачено 250 единиц энергии'
                        er_st3 = f'Теперь у вас {enrg} единиц энергии'
                        print(f'{er_st1}{er_st2}\n{er_st3}\n{z}')
                else:
                    print(f'Отмена исследования звезды...\n{z}')

        elif react.lower() == 'звезды':
            sts1 = 'Для исследования звезд потребуется 500 единиц энергии'
            sts2 = f'У вас {enrg} единиц энергии'
            sts3 = 'Вы действительно хотите исследовать звезды? Д/Н'
            app = input(f'{z}\n{sts1}\n{sts2}\n{sts3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 500:
                    a = 'У вас недостаточно энергии '
                    b = 'для исследования звезд'
                    c = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{a}{b}\n{c}\n{z}')
                else:
                    print(f'{z}\nПытаемся исследовать звезды...')
                    for i in tqdm(range(500)):
                        time.sleep(0.01)
                    St.examine_st('all')
                    enrg -= 500
                    zsts1 = 'На исследование звезд '
                    zsts2 = 'было потрачено 500 единиц энергии'
                    zsts3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zsts1}{zsts2}\n{zsts3}\n{z}')
                    if St._multi_single_error('all')[1] is not True:
                        p_res[0] = True
                        p_res[1] = True
                        e_sts += 1
                        ach.e_sts(e_sts)
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
                bh5 = '? Д/Н'
                app = input(f'{z}\n{bh1}{bh2}\n{bh3}\n{bh4}{bh5}\n{z}\n')
                if app.lower() == 'д' or app.lower() == 'да':
                    try:
                        if enrg < 250:
                            a = 'У вас недостаточно энергии '
                            b = 'для иследования черной дыры'
                            c = 'Попробуйте получить энергию '
                            d = 'от ближайшей звезды'
                            print(f'{z}\n{a}{b}\n{c}{d}\n{z}')
                        else:
                            att_bh = f'Пытаемся исследовать черную дыру {bh}'
                            print(f'{z}\n{att_bh}...')
                            for i in tqdm(range(250)):
                                time.sleep(0.01)
                            bh = int(bh)
                            Bh.examine_bh(bh)
                            enrg -= 250
                            zbh1 = f'На исследование черной дыры {bh} '
                            zbh2 = 'было потрачено 250 единиц энергии'
                            zbh3 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{zbh1}{zbh2}\n{zbh3}\n{z}')
                            if Bh._multi_single_error(bh)[0] is not True:
                                e_bh += 1
                                ach.e_bh(e_bh)
                    except:
                        if len(list(bh)) == 1:
                            print(f'{z}\nВы ввели знак вместо номера\n{z}')
                        elif len(list(bh)) > 1:
                            print(f'{z}\nВы ввели знаки вместо номера\n{z}')
                        enrg -= 250
                        er_bh1 = f'На исследование черной дыры {bh} '
                        er_bh2 = 'было потрачено 250 единиц энергии'
                        er_bh3 = f'Теперь у вас {enrg} единиц энергии'
                        print(f'{er_bh1}{er_bh2}\n{er_bh3}\n{z}')
                else:
                    print(f'Отмена исследования черной дыры...\n{z}')

        elif react.lower() == 'черные дыры':
            bhs1 = 'Для исследования черных дыр потребуется 500 единиц энергии'
            bhs2 = f'У вас {enrg} единиц энергии'
            bhs3 = 'Вы действительно хотите исследовать черные дыры? Д/Н'
            app = input(f'{z}\n{bhs1}\n{bhs3}\n{z}\n')
            if app.lower() == 'д' or app.lower() == 'да':
                if enrg < 500:
                    a = 'У вас недостаточно энергии '
                    b = 'для исследования черных дыр'
                    c = 'Попробуйте получить энергию от ближайшей звезды'
                    print(f'{z}\n{a}{b}\n{c}\n{z}')
                else:
                    print(f'{z}\nПытаемся исследовать черные дыры...')
                    for i in tqdm(range(500)):
                        time.sleep(0.01)
                    Bh.examine_bh('all')
                    enrg -= 500
                    zbhs1 = 'На исследование черных дыр '
                    zbhs2 = 'было потрачено 500 единиц энергии'
                    zbhs3 = f'Теперь у вас {enrg} единиц энергии'
                    print(f'{zbhs1}{zbhs2}\n{zbhs3}\n{z}')
                    if Bh._multi_single_error('all')[1] is not True:
                        e_bhs += 1
                        ach.e_bhs(e_bhs)
            else:
                print(f'Отмена исследования черных дыр...\n{z}')

        elif react.lower() == 'помощь':
            h1 = 'Список возможных комманд для исследования объектов:'
            h2 = '"Систему", "Звезду", "Звезды", "Черную дыру", "Черные дыры"'
            print(f'{z}\n+{h1}\n{h2}\n{z}')
        elif react.lower() == 'выход' or react.lower() == 'конец':
            titles()
            break
        else:
            print('Непонятен объект исследования, попробуйте еще раз')

    elif act.lower() == 'зарядиться':
        en = input('Выберите звезду для подзарядки: ')
        if en.lower() == 'помощь':
            St.help_st(h_en=True)
        else:
            try:
                en = int(en)
                if St._multi_single_error(en)[0] is not True:
                    if res is True or p_res[en-1] is True:
                        nst = StSys.get_ns(en)
                    elif res is False and p_res[en-1] is False:
                        nst = en
                    en1 = f'Зарядка солнечных батарей от звезды {nst} займет '
                    if p_res[en-1] is True:
                        clt = f'{St._get_class_time(en)} секунд'
                    elif p_res[en-1] is False:
                        clt = '[Неизвестно] секунд'
                    en2 = 'Вы действительно хотите зарядиться? Д/Н'
                    repeat = input(f'{z}\n{en1}{clt}\n{en2}\n{z}\n')
                    if repeat.lower() == 'д' or repeat.lower() == 'да':
                        print(f'{z}\nЗаряжаемся от звезды {nst}...')
                        St.get_enrg(en)
                        p_res[en-1] = True
                        if enrg + 1000 < 15000:
                            enrg += 1000
                            zen1 = 'Вы получили 1000 единиц энергии от звезды '
                            zen2 = f'Теперь у вас {enrg} единиц энергии'
                            print(f'{z}\n{zen1}{nst}\n{zen2}\n{z}')
                        else:
                            genrg = 15000 - enrg
                            enrg += genrg
                            zen1 = f'Вы получили получили {genrg} '
                            zen2 = f'единиц энергии от звезды {nst}'
                            zen3 = f'Так как ваш аккумулятор достиг лимита: '
                            zen4 = '15000 единиц энергии'
                            print(f'{z}\n{zen1}{zen2}\n{zen3}{zen4}\n{z}')
                    else:
                        print(f'Отмена зарядки...\n{z}')
                else:
                    St.help_st(h_en=True)
            except:
                if len(list(str(en))) == 1:
                    print(f'{z}\nВы ввели знак вместо номера\n{z}')
                elif len(list(str(en))) > 1:
                    print(f'{z}\nВы ввели знаки вместо номера\n{z}')

    elif act.lower() == 'энергия':
        print(f'{z}\nВаша энергия равна: {enrg} / 15000\n{z}')

    elif act.lower() == 'помощь':
        eh1 = 'Список возможных комманд:'
        eh2 = '"Прыжок", "Исследовать", "Зарядиться", "Энергия"'
        print(f'{z}\neh1\n{eh2}\n{z}')

    elif act.lower() == 'выход' or act.lower() == 'конец':
        titles()
        break

    else:
        print('Непонятно действие, попробуйте еще раз')
