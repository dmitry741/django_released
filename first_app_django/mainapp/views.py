from django.shortcuts import render, render_to_response

def main(request):
    edu_list = ['Нижегородский универстет им. Лобачевского. Механико-математический факультет.',
                'Online Geekbrains. Специальность Python разработчик.']
    work_list = ['ЗАО НКТ. Разработчик С++.', 'АО Ридан. Разработчик C#.']
    first_name = 'павлов'
    second_name = 'дмитрий'
    project_name = 'AboutMe'

    my_dict = {'edu_list': edu_list,
               'work_list': work_list,
               'first_name': first_name,
               'second_name': second_name,
               'project_name': project_name}

    return render_to_response('index.html', my_dict)
