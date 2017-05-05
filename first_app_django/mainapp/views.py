from django.shortcuts import render, render_to_response
import datetime
from mainapp.hobbystructure import get_model, get_path_to_static, get_nav_hobby
from mainapp.sessioncontrol import MySession
from mainapp.projectstructure import MyProjectStructure, Carusel


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
    d['cur_time'] = get_string_cur_date()

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

    # 1
    caption = 'Игра Жизнь'
    text = 'Игра Жизнь (англ. Conway\'s Game of Life) - клеточный автомат, придуманный английским математиком Джоном '\
        'Конвеем в 1970 году. Программная реализация игры в виде десктопного приложения написанного на C#.'
    button_text = 'Перейти на GitHub'
    button_link = 'https://github.com/dmitry741/gamelife_project.git'
    active = 'item active'
    class_name = 'first-slide'
    alt = 'First slide'

    carusel1 = Carusel(caption, text, button_text, button_link, active, class_name, alt)

    # 2
    caption = 'Расчетная программа АО Ридан'
    text = 'Программа для расчета и подбора теплообменников. Программа преимущественно ориентирована на специалистов в'\
        ' подборе теплообменников для сферы жилищно-коммунального хозяйства.'
    button_text = 'Перейти на сайт'
    button_link = 'http://www.ridan.ru/raschet-i-zakaz/raschetnaja_programma_ridan'
    active = 'item'
    class_name = 'second-slide'
    alt = 'Second slide'

    carusel2 = Carusel(caption, text, button_text, button_link, active, class_name, alt)

    # 3
    caption = 'SusaninLab: поиск кратчайших маршрутов'
    text = 'Программа для решения ряда классических задач на взвешенном графе: задача коммивояжера, кратчайший путь '\
        'между двумя вершинами, построение минимального остовного дерева.'
    button_text = 'Перейти на промо-сайт'
    button_link = 'http://www.orpal.ru'
    active = 'item'
    class_name = 'third-slide'
    alt = 'Third slide'

    carusel3 = Carusel(caption, text, button_text, button_link, active, class_name, alt)

    # 4
    caption = 'Сайт-визитка'
    text = 'Одним из проектов является данный сайт. Он написан с использованием одного из популярных веб-фреймверков'\
        ' Django, где встроенным языком программирования является Python.'
    button_text = 'Перейти к описанию'
    button_link = '#'
    active = 'item'
    class_name = 'fourth-slide'
    alt = 'Fourth slide'

    carusel4 = Carusel(caption, text, button_text, button_link, active, class_name, alt)

    my_project_structure = MyProjectStructure()
    my_project_structure.carusel.append(carusel1)
    my_project_structure.carusel.append(carusel2)
    my_project_structure.carusel.append(carusel3)
    my_project_structure.carusel.append(carusel4)

    my_project_structure.indicators.append((0, 'active'))
    my_project_structure.indicators.append((1, ''))
    my_project_structure.indicators.append((2, ''))
    my_project_structure.indicators.append((3, ''))

    my_project_structure.stack.append(('C#', 'GDI+', 'Git', 'MS Visual Studio'))
    my_project_structure.stack.append(('C#', 'GDI+', 'SQL', 'TFS', 'MS Visual Studio'))
    my_project_structure.stack.append(('C++', 'STL', 'MFC', 'ActiveX', 'COM', 'GDI+', 'MS Visual Studio'))
    my_project_structure.stack.append(('Django', 'Python', 'HTML', 'Bootstrap', 'Git', 'PyCharm'))

    d['projects_data'] = my_project_structure

    return render_to_response(pages[index] + '.html', d)


def hobbies(request):
    index = 3
    pages = get_mainmenu_links()

    d = get_common_dict(index)
    d['hobby_list_models'] = get_nav_hobby()

    p = '1'

    if request.method == 'GET':
        p = request.GET.get('page')

        if p is None:
            p = '1'
        elif p not in [str(x + 1) for x in range(5)]:
            p = '1'

        hp = request.GET.get('model')

        if hp is not None and hp in [str(x) for x in range(2)] :
            MySession.set_hobby_index(request, int(hp))

    model_index = MySession.get_hobby_index(request)
    model = get_model(model_index)
    model.main_image_src = get_path_to_static(model_index) + p + '.jpg'
    d['debug_value'] = model_index
    d['model'] = model

    return render_to_response(pages[index] + '.html', d)


def contacts(request):
    index = 4
    pages = get_mainmenu_links()
    d = get_common_dict(index)

    return render_to_response(pages[index] + '.html', d)