class MyHobbyStructure:
    def __init__(self, caption):
        self.name = caption
        self.shortdesc = ''
        self.desc = []
        self.buttonname = self.name + ' на Википедии'
        self.buttonlink = ''

        self.mainimagesrc = ''

        self.smallimagesrc = []
        self.smallimagelink = []


    def __str__(self):
        return self.name


def get_model_captions():
    return ['Су-24', 'Су-37']


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

        path = '/static/images/hobbies/su24/'

    elif index == 1:
        model.shortdesc = 'фронтовой бомбардировщик'
        model.desc = ['''Су-37 (по кодификации НАТО: Flanker-F) — российский экспериментальный сверхманевренный истребитель
                      четвёртого поколения с передним горизонтальным оперением (ПГО) и двигателями с УВТ. Создан на
                      базе истребителя Су-27М.''',
                      '''Су 37 демонстрировал технологию управления вектором тяги, которую предполагалось использовать
                      на новых машинах семейства Сухого. Отработанные на нём решения легли в основу создания самолётов
                      пятого поколения.''']
        model.buttonlink = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-37'

        path = '/static/images/hobbies/su37/'

    model.mainimagesrc = path + '1.jpg'

    imagesrc = []
    imagelinks = []

    for x in range(5):
        str_x = str(x + 1)
        imagesrc.append(path + str_x + '.jpg')
        imagelinks.append('/hobbies/?page=' + str_x)

    model.smallimagesrc = imagesrc
    model.smallimagelink = imagelinks

    return model


