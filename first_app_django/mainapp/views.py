from django.shortcuts import render, render_to_response


def main(request):

    page_title = 'AboutMe project'
    menu_list = ['Резюме', 'Мои проекты', 'Увлечения', 'Контакты']

    my_dict = {'page_title': page_title,
               'menu_list': menu_list}

    return render_to_response('index.html', my_dict)


def cv(request):
    return render_to_response('cv.html')


def hobbies(request):
    return render_to_response('hobbies.html')


def projects(request):
    return render_to_response('projects.html')