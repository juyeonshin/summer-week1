from django.shortcuts import render

def main(request):
    return render (request, 'main.html')

def book(request):
    return render (request, 'book.html')