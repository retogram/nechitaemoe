print('''
                        Тест: сколько в тебе творчества?

В этом тесте несколько заданий. Вы должны ответить, как бы вы их выполнили.
И будет ещё лучше, если по ходу прохождения теста, вы их действительно будете выполнять.
P.S У этого теста ограниченное количество прохождений.
Доступные пути:
 если нажать все 1, 2, 3.
''')

otvet = input('\t\t\t\tНачнём?!\nВведите "да" чтобы начать: ')
vopros1 = '''       Напиши письмо кумиру:
                    1) Меня никто особо не вдохновляет
                    2) Сeгодня же это сделаю и отправлю любимому автору
                    3) А если его нет в живых?!'''

vopros2 = '''       Сходите в кинотеатр и рисуйте в темноте:
                    1) О, это интересно! Сейчас выберу блокнот и ручки и отправлюсь на ближайший сеанс
                    2) А какой фильм выбрать? Половину я уже смотрел, а остальные мне не интересны
                    3) Не люблю рисовать. Тем более в темноте!'''

vopros3 = '''       Включите радио. Переключайте станции каждые 10 секунд и записывайте всё, что услышите:
                    1) Классная идея! Я не только записал, но и составил из получившегося смешной рассказ
                    2) У меня нет радиоприемника
                    3) Мне кажется это скучным'''

vopros4 = '''       Подстригитесь. Вспомните разговор со своим парикмахером:
                    1) Не общаюсь с малознакомыми людьми
                    2) Я не смог выбрать новую прическу
                    3) Мы отлично пообщались. Думаю в следующий раз я приду в эту же парикмахерскую'''

vopros5 = '''       Придумайте рекламу несуществующего продукта:
                    1) Я не силён в придумывании
                    2) Ксли продукта не существует, то для него не нужно придумывать рекламу
                    3) Можно смешать несколько известных мне брендов и историю их создания'''

vopros6 = '''       Нарисуйте своё рабочее место:
                    1) Я работаю в скучном офисе, поэтому мне нечего изобразить
                    2) Можно пользоваться любыми карандашами???
                    3) Я не умею рисовать'''

vopros7 = '''       Украдите название книги, которую никогда не читали и придумайте свою историю на эту тему:
                    1) Я редко читаю книги, да и не уверен, что смогу написать интересную историю
                    2) Легко выберу книгу из списка для чтения и напишу подробный рассказ, ведь я тот ещё писака
                    3) Не могу выбрать из книг: "Уход за хомячками" или "Что мы делаем на этой планете"'''

# если нажать все 1, (3, 2, 1, 3, 2, 1, 3), (2, 1, 3, 2, 1, 3, 2)
otvet1 = '''                                        ТВОРЕЦ
                    Ты умеешь красть как настоящий художник. 
                    Ты не не просто заимствуешь чужие задумки, а перерабатываешь их и создаёшь оригинальные идеи. Продолжай в том же духе!'''

# если нажать все 2 или 3, (1, 3, 2, 1, 3, 2, 1)
otvet2 = '''                                        ВЫДУМЩИК
                    Ты мастер придумывать отговорки. Но почему бы не направить твои креативные способности в нужное русло?'''

# (1, 2, 3, 1, 2, 3, 1), (1, 2, 3, 2, 1, 2, 3)
otvet3 = '''                                        НАЧИНАЮЩИЙ
                    Пока у тебя не очень хорошо получается смотреть на мир глазами художника. Но всему можно научиться! '''

let_int = (' Введите цифру: ')
err_otvet = 'Нет такого варианта ответа пока что!!!'

if otvet.lower() == 'да':
    print(vopros1)
    x = input(f'{let_int} ')
    if x == '1':
        print(vopros2)
        x = input(f'{let_int} ')
        if x == '1':
            print(vopros3)
            x = input(f'{let_int} ')
            if x == '1':
                print(vopros4)
                x = input(f'{let_int} ')
                if x == '1':
                    print(vopros5)
                    x = input(f'{let_int} ')
                    if x == '1':
                        print(vopros6)
                        x = input(f'{let_int} ')
                        if x == '1':
                            print(vopros7)
                            x = input(f'{let_int} ')
                            if x == '1':
                                print(otvet1)

        if x == '2':
            print(vopros3)
            x = input(f'{let_int} ')
            if x == '3':
                print(vopros4)
                x = input(f'{let_int} ')
                if x == '1':
                    print(vopros5)
                    x = input(f'{let_int} ')
                if x == '2':
                    print(vopros5)
                    if x == '1':
                        print(vopros6)
                        x = input(f'{let_int} ')
                    if x == '2':
                        print(vopros6)
                        x = input(f'{let_int} ')
                        if x == '1':
                            pass
                        if x == '2':
                            print(vopros7)
                            x = input(f'{let_int} ')
                            if x == '3':
                                print(otvet3)
                        if x == '3':
                            print(vopros7)
                            x = input(f'{let_int} ')
                            if x == '1':
                                print(otvet3)

    if x == '2':
        print(vopros2)
        x = input(f'{let_int} ')
        if x == '1':
            pass
        if x == '2':
            print(vopros3)
            x = input(f'{let_int} ')
            if x == '1':
                pass
            if x == '2':
                print(vopros4)
                x = input(f'{let_int} ')
                if x == '1':
                    pass
                if x == '2':
                    print(vopros5)
                    x = input(f'{let_int} ')
                    if x == '1':
                        pass
                    if x == '2':
                        print(vopros6)
                        x = input(f'{let_int} ')
                        if x == '1':
                            pass
                        if x == '2':
                            print(vopros7)
                            x = input(f'{let_int} ')
                            if x == '1':
                                pass
                            if x == '2':
                                print(otvet2)

    if x == '3':
        print(vopros2)
        x = input(f'{let_int} ')
        if x == '1':
            pass
        if x == '2':
            pass
        if x == '3':
            print(vopros3)
            x = input(f'{let_int} ')
            if x == '1':
                pass
            if x == '2':
                pass
            if x == '3':
                print(vopros4)
                x = input(f'{let_int} ')
                if x == '1':
                    pass
                if x == '2':
                    pass
                if x == '3':
                    print(vopros5)
                    x = input(f'{let_int} ')
                    if x == '1':
                        pass
                    if x == '2':
                        pass
                    if x == '3':
                        print(vopros6)
                        x = input(f'{let_int} ')
                        if x == '1':
                            pass
                        if x == '2':
                            pass
                        if x == '3':
                            print(vopros7)
                            x = input(f'{let_int} ')
                            if x == '1':
                                pass
                            if x == '2':
                                pass
                            if x == '3':
                                print(otvet2)

else:
    print('Тогда пока!')
