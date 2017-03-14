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


def main(request):

    page_title = 'AboutMe project'

    menu_manager = MyMainMenuManager()
    menu_list = menu_manager.menuItemList

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('index.html', my_dict)


def cv(request):
    return render_to_response('cv.html')


def hobbies(request):
    return render_to_response('hobbies.html')


def projects(request):
    return render_to_response('projects.html')


def contacts(request):
    return render_to_response('contacts.html')