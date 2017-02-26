from django.shortcuts import render, render_to_response

def main(request):
    my_dict1 = {'name': 'Павлов Дмитрий', 'project': 'AboutMe'}
    return render_to_response('index.html', my_dict1)
