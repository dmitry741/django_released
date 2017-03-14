from django.shortcuts import render, render_to_response


class MyMainMenuItem:
    def __init__(self, menuItem, link):
        self.caption = menuItem
        self.link = link

    def __str__(self):
        return self.caption


class MyMainMenuManager:
    def __init__(self):
        self.menuItemList = []
        self.menuItemList.append(MyMainMenuItem('Резюме', '/cv'))
        self.menuItemList.append(MyMainMenuItem('Мои проекты', '/projects'))
        self.menuItemList.append(MyMainMenuItem('Увлечения', '/hobbies'))
        self.menuItemList.append(MyMainMenuItem('Контакты', '/contacts'))


def get_common_menu_list():
    menu_manager = MyMainMenuManager()
    return menu_manager.menuItemList


def main(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list()

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('index.html', my_dict)


def cv(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list()

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('cv.html', my_dict)


def hobbies(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list()

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('hobbies.html', my_dict)


def projects(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list()

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('projects.html', my_dict)


def contacts(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list()

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('contacts.html', my_dict)