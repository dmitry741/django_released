from django.shortcuts import render, render_to_response


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
        self.menuItemList.append(MyMainMenuItem('Главная', '/', index == len(self.menuItemList)))
        self.menuItemList.append(MyMainMenuItem('Резюме', '/cv', index == len(self.menuItemList)))
        self.menuItemList.append(MyMainMenuItem('Мои проекты', '/projects', index == len(self.menuItemList)))
        self.menuItemList.append(MyMainMenuItem('Увлечения', '/hobbies', index == len(self.menuItemList)))
        self.menuItemList.append(MyMainMenuItem('Контакты', '/contacts', index == len(self.menuItemList)))


def get_common_menu_list(index):
    menu_manager = MyMainMenuManager(index)
    return menu_manager.menuItemList


def main(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(0)

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('index.html', my_dict)


def cv(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(1)

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('cv.html', my_dict)


def projects(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(2)

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('projects.html', my_dict)


def hobbies(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(3)

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('hobbies.html', my_dict)


def contacts(request):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(4)

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('contacts.html', my_dict)