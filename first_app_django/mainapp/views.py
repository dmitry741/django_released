from django.shortcuts import render, render_to_response
import datetime


def get_mainsmenu_captions():
    return ['Главная', 'Резюме', 'Проекты', 'Увлечения', 'Контакты']


def get_mainmenu_links():
    return ['index', 'cv', 'projects', 'hobbies', 'contacts']


def skill_list():
    return ['C#', 'C++', 'Python', 'VB.NET', 'Perl', 'Windows API', 'COM', 'ActiveX', 'GDI+',
            'OpenGL', 'ASP.NET', 'Django', 'HTML', 'CSS', 'Bootstrap', 'Multi-threading', 'MFC', 'ATL', 'STL', 'Boost',
            'NAnt', 'NUnit', 'TFS', 'Git', 'Scrum', 'MS SQL', 'MySql']


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
    string = ''

    if age in range(11, 20):
        string = 'лет'
    elif age % 10 in (0, 5, 6, 7, 8, 9):
        string = 'лет'
    elif age % 10 == 1:
        string = 'год'
    else:
        string = 'года'

    return ' '.join([str(age), string])


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


def get_response(index):
    page_title = 'AboutMe project'
    menu_manager = MyMainMenuManager(index)
    menu_list = menu_manager.menuItemList
    pages = get_mainmenu_links()
    small_caption = get_mainsmenu_captions()
    small_caption[0] = None

    my_dict = {'page_title': page_title,
               'menu_list': menu_list,
               'small_caption': small_caption[index],
               'cur_year': datetime.datetime.strftime(datetime.datetime.now(), "%Y")}

    if index == 0:  # index
        my_dict['cur_time'] = datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y")
    elif index == 1:  # cv
        my_dict['cv_panel'] = 'panel panel-default'
        my_dict['cv_skills'] = skill_list()
        my_dict['age'] = get_string_age(1974, 2, 6)

    return render_to_response(pages[index] + '.html', my_dict)


def main(request):
    return get_response(0)


def cv(request):
    return get_response(1)


def projects(request):
    return get_response(2)


def hobbies(request):
    return get_response(3)


def contacts(request):
    return get_response(4)