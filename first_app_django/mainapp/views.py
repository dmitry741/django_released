from django.shortcuts import render, render_to_response

def main(request):
    edu_list = ['Нижегородский универстет им. Лобачевского. Механико-математический факультет.',
                'Online Geekbrains. Специальность Python разработчик.']
    work_list = ['ЗАО НКТ. Разработчик С++.', 'АО Ридан. Разработчик C#.']
    caption = 'Павлов Дмитрий. AboutMe project.'

    my_dict = {'edu_list': edu_list,
               'work_list': work_list,
               'caption': caption}

    return render_to_response('index.html', my_dict)
