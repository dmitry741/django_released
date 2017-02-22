from django.shortcuts import render, render_to_response

def main(request):
    return render_to_response('index.html')

# Create your views here.
