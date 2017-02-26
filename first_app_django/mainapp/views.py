from django.shortcuts import render, render_to_response

def main(request):
    my_name = 'Pavlov Dmitry'
    return render_to_response('index.html', {'name': my_name})
