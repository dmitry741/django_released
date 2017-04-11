class MyHobbyStructure:
    def __init__(self, caption):
        self.name = caption
        self.shortdesc = ''
        self.desc = []

        self.buttonname = self.name + ' на Википедии'
        self.buttonlink = ''

        self.mainimagesrc = ''
        self.smallimages = []

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
        model.shortdesc = 'фронтовой бомбардировщик'
        model.desc = ['''Су-24 советский и российский тактический фронтовой бомбардировщик с крылом изменяемой
                       стреловидности, предназначенный для нанесения ракетно-бомбовых ударов в простых и сложных
                       метеоусловиях, днём и ночью, в том числе на малых высотах с прицельным поражением наземных и
                       надводных целей.''',
                       '''Су-24 это самолет, сконструированный еще в 1975 году. Несмотря на свой возраст, данная
                       летающая боевая машина находится на вооружении и по сей день. Более того, ее активно
                       модернизируют и совершенствуют, ведь ее качества актуальны и на сегодняшний день.''',
                       'Самолет хорошо себя зарекомендовала во время боевой опреации в Сирии.']
        model.buttonlink = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-24'
    elif index == 1:
        model.shortdesc = 'экспериментальный сверхманевренный истребитель'
        model.desc = ['''Су-37 (по кодификации НАТО: Flanker-F) — российский экспериментальный сверхманевренный истребитель
                      четвёртого поколения с передним горизонтальным оперением (ПГО) и двигателями с УВТ. Создан на
                      базе истребителя Су-27М.''',
                      '''Самолет имеет технологию управляемого вектора тяги, которую предполагалось использовать
                      на новых машинах семейства Сухого. Отработанные на нём решения легли в основу создания самолётов
                      пятого поколения.''']
        model.buttonlink = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-37'

    path = get_path_to_static(index)
    model.mainimagesrc = path + '1.jpg'

    small_images = []

    for x in range(5):
        str_x = str(x + 1)
        si = StringTemplate(path + str_x + '.jpg', '/hobbies/?page=' + str_x)
        small_images.append(si)

    model.smallimages = small_images

    return model


