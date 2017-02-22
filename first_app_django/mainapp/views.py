from django.shortcuts import render, render_to_response

def main(request):
    my_name = 'Pavlovs Dmitry and Nataly'
    return render_to_response('index.html', {'name': my_name})

def about(request):
    return  render_to_response('about.html')
