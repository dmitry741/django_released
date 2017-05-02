class MyHobbyStructure:
    def __init__(self, caption):
        self.name = caption
        self.short_desc = ''
        self.desc = []

        self.button_name = self.name + ' на Википедии'
        self.button_link = ''

        self.main_image_src = ''
        self.small_images = []

    def __str__(self):
        return self.name


class StringTemplate:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def __str__(self):
        return self.item1


def get_model_captions():
    return ['Су-24', 'Су-37']


def get_nav_hobby():
    list_names = get_model_captions()
    st_list = []

    for x in range(2):
        st = StringTemplate(list_names[x], '/hobbies/?model=' + str(x))
        st_list.append(st)

    return st_list


def get_path_to_static(index):

    if index == 0:
        path = '/static/images/hobbies/su24/'
    else:
        path = '/static/images/hobbies/su37/'

    return path

def get_model(index):

    names = get_model_captions()
    model = MyHobbyStructure(names[index])

    if index == 0:
        model.short_desc = 'фронтовой бомбардировщик'
        model.desc = ['''Су-24 советский и российский тактический фронтовой бомбардировщик с крылом изменяемой
                       стреловидности, предназначенный для нанесения ракетно-бомбовых ударов в простых и сложных
                       метеоусловиях, днём и ночью, в том числе на малых высотах с прицельным поражением наземных и
                       надводных целей.''',
                       '''Су-24 это самолет, сконструированный еще в 1975 году. Несмотря на свой возраст, данная
                       летающая боевая машина находится на вооружении и по сей день. Более того, ее активно
                       модернизируют и совершенствуют, ведь ее качества актуальны и на сегодняшний день.''',
                       '''Во время боевой операции в Сирии, в ноябре 2015 Су-24M при возвращении на авиабазу Хмеймим был
                        сбит турецким истребителем F-16 в районе сирийско-турецкой границы. Лётчик погиб во время
                        катапультирования (расстрелян с земли). Штурман выжил (спасён российским и сирийским
                        спецназами). Модель была собрана в память об этом трагическом инциденте.''']

        model.button_link = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-24'
    elif index == 1:
        model.short_desc = 'экспериментальный сверхманевренный истребитель'
        model.desc = ['''Су-37 (по кодификации НАТО: Flanker-F) — российский экспериментальный сверхманевренный истребитель
                      четвёртого поколения с передним горизонтальным оперением (ПГО) и двигателями с УВТ. Создан на
                      базе истребителя Су-27М.''',
                      '''Самолет предназначен для достижения превосходства в воздухе и точечной
                      бомбардировки наземных целей. Су-37 был скомпонован по аэродинамической схеме -
                      интегральный неустойчивый триплан. Переднее горизонтальное оперение самолета позволяло повысить
                      его маневренность на сверхнизких скоростях и закритических углах атаки.''',
                      '''В настоящий момент проект закрыт. Отработанные на нём решения легли в основу создания самолётов
                      пятого поколения.''']

        model.button_link = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-37'

    path = get_path_to_static(index)
    model.main_image_src = path + '1.jpg'

    small_images = []

    for x in range(5):
        str_x = str(x + 1)
        si = StringTemplate(path + str_x + '.jpg', '/hobbies/?page=' + str_x)
        small_images.append(si)

    model.small_images = small_images

    return model

