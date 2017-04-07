from django.shortcuts import render, render_to_response
import datetime


def get_mainsmenu_captions():
    return ['Главная', 'Резюме', 'Проекты', 'Увлечения', 'Контакты']


def get_mainmenu_links():
    return ['index', 'cv', 'projects', 'hobbies', 'contacts']


def skill_list():
    return ('C#', 'C++', 'Python', 'VB.NET', 'Perl', 'Windows API', 'COM', 'ActiveX', 'GDI+',
            'OpenGL', 'ASP.NET', 'Django', 'HTML', 'CSS', 'Bootstrap', 'Multi-threading', 'MFC', 'ATL', 'STL', 'Boost',
            'NAnt', 'NUnit', 'TFS', 'Git', 'Scrum', 'MS SQL', 'MySql')


# def get_cv_items():
#     return ('Синопсис', 'Образование', 'Опыт', 'Языки программирования', 'IDE', 'Технологии', 'Иностранные языки',
#             'Электронные сертификаты')


def get_age(_year, _month, _day):
    cur_time = datetime.date.today()
    my_hbd = datetime.date(_year, _month, _day)

    age = cur_time.year - my_hbd.year
    dt = datetime.date(year=cur_time.year, month=_month, day=_day)

    if dt > cur_time:
        age -= 1

    return age


def get_string_age(_year, _month, _day):
    age = get_age(_year, _month, _day)

    if age in range(11, 20):
        string = 'лет'
    elif age % 10 in (0, 5, 6, 7, 8, 9):
        string = 'лет'
    elif age % 10 == 1:
        string = 'год'
    else:
        string = 'года'

    return ' '.join([str(age), string])


def get_string_cur_date():
    months = {1: 'Января', 2: 'Февраля', 3: 'Марта',
              4: 'Апреля', 5: 'Мая', 6: 'Июня',
              7: 'Июля', 8: 'Августа', 9: 'сентября',
              10: 'октября ', 11: 'Ноября', 12: 'Декабря'}
    cur_date = datetime.datetime.now()
    day_of_weak = cur_date.isoweekday()

    weaks = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}

    return ' '.join([weaks[day_of_weak] + ',', str(cur_date.day), months[cur_date.month], str(cur_date.year)])


class MyMainMenuItem:
    def __init__(self, menuItem, link, active):
        self.caption = menuItem
        self.link = link
        self.active = active

    def __str__(self):
        return self.caption


class MyMainMenuManager:
    def __init__(self, index):
        self.menuItemList = []

        list_caption = get_mainsmenu_captions()
        list_links = get_mainmenu_links()
        count = len(list_caption)

        for i in range(count):
            self.menuItemList.append(MyMainMenuItem(list_caption[i], '/' + list_links[i], index == len(self.menuItemList)))


class StringTemplate:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def __str__(self):
        return self.item1


def get_common_dict(index):
    page_title = 'AboutMe project'
    menu_manager = MyMainMenuManager(index)
    menu_list = menu_manager.menuItemList
    small_caption = get_mainsmenu_captions()
    small_caption[0] = None

    d = {'page_title': page_title,
         'menu_list': menu_list,
         'small_caption': small_caption[index],
         'cur_year': datetime.datetime.strftime(datetime.datetime.now(), "%Y")}

    return d


def main(request):
    index = 0
    pages = get_mainmenu_links()

    d = get_common_dict(index)
    d['cur_time'] = get_string_cur_date()  # datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y")

    return render_to_response(pages[index] + '.html', d)


def cv(request):
    index = 1
    pages = get_mainmenu_links()

    d = get_common_dict(index)
    d['cv_panel'] = 'panel panel-default'
    d['cv_skills'] = skill_list()
    d['cv_age'] = get_string_age(1974, 2, 6)

    return render_to_response(pages[index] + '.html', d)


def projects(request):
    index = 2
    pages = get_mainmenu_links()

    d = get_common_dict(index)

    return render_to_response(pages[index] + '.html', d)


def hobbies(request):
    index = 3
    pages = get_mainmenu_links()

    d = get_common_dict(index)

    path = '/static/images/hobbies/su24/'

    d['hobby_caption'] = 'Модель Су-24, фронтовой бомбардировщик'
    d['hobby_link_to_wiki'] = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83-24'
    d['hobby_button_to_wiki'] = 'Су-24 на Википедии'
    d['hobby_cur_image'] = path + '1.jpg'
    d['hobby_list_models'] = [StringTemplate('Су-24', 'primary'), StringTemplate('Су-37', 'default')]

    request.session['fav_color'] = 'value from the current session'

    if request.method == 'GET':
        p = request.GET.get('page')

        if p is not None:
            if p in [str(x + 1) for x in range(5)]:
                request.session['fav_color'] = p
                d['hobby_cur_image'] = path + p + '.jpg'

    d['debug_value'] = request.session['fav_color']

    image_list = []

    for x in range(5):
        str_n = str(x + 1)
        s = StringTemplate(path + str_n + '.jpg', 'photo' + str_n)
        s.link = '/hobbies/?page=' + str_n
        image_list.append(s)

    d['image_list'] = image_list

    return render_to_response(pages[index] + '.html', d)


def contacts(request):
    index = 4
    pages = get_mainmenu_links()

    d = get_common_dict(index)

    return render_to_response(pages[index] + '.html', d)
