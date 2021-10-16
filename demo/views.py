from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication


class Another(View):
    books = Book.objects.all()
    booksFilter = Book.objects.filter(onSale=True)
    output = ''
    for eachbook in booksFilter:
        output += f"ID# :  {eachbook.id} --- Name : {eachbook.title} --- Description : {eachbook.description} <br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('This is first function')


def second(request):
    return render(request, 'index.html')


def third(request):
    return render(request, 'index.html', {'data': 'This is sample data'})


def fourth(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'booksList': books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
