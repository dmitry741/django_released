from django.shortcuts import render, render_to_response


def get_mainmenu_captions():
    return ['Главная', 'Резюме', 'Мои проекты', 'Увлечения', 'Контакты']


def get_mainmenu_links():
    return ['/', '/cv', '/projects', '/hobbies', '/contacts']


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

        list_caption = get_mainmenu_captions()
        list_links = get_mainmenu_links()
        count = len(list_caption)

        for i in range(count):
            self.menuItemList.append(MyMainMenuItem(list_caption[i], list_links[i], index == len(self.menuItemList)))


def get_common_menu_list(index):
    menu_manager = MyMainMenuManager(index)
    return menu_manager.menuItemList


def get_dict(index):
    page_title = 'AboutMe project'
    menu_list = get_common_menu_list(index)
    small_caption = get_mainmenu_captions()
    small_caption[0] = None

    my_dict = {'page_title': page_title,
               'menu_list': menu_list,
               'small_caption': small_caption[index]}

    return my_dict


def main(request):
    return render_to_response('index.html', get_dict(0))


def cv(request):
    return render_to_response('cv.html', get_dict(1))


def projects(request):
    return render_to_response('projects.html', get_dict(2))


def hobbies(request):
    return render_to_response('hobbies.html', get_dict(3))


def contacts(request):
    return render_to_response('contacts.html', get_dict(4))