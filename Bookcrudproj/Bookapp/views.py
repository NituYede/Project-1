from django.shortcuts import render, redirect
from Bookapp.models import Book

def homepage(request):
    data = Book.objects.all()
    context = {'books': data}
    return render(request, 'home.html', context)

def addbook(request):
    if request.method == "GET":
        return render(request, 'addbook.html')
    else:
        t = request.POST['title']
        a = request.POST['author']
        p = request.POST['price']
        b = Book.objects.create(title=t, author=a, price=p)
        b.save()
        return redirect('/home')

def deletebook(request, bookid):
    # Corrected syntax in the comment
    # print('delete book id:', bookid)
    b = Book.objects.filter(id=bookid)
    b.delete()
    return redirect('/home')

def updatebook(request, bookid):
    if request.method == "GET":
        print('update book id:', bookid)
        book = Book.objects.get(id=bookid)
        context = {'book': book}
        return render(request, 'updatebook.html', context)
    else:
        t = request.POST['title']
        a = request.POST['author']
        p = request.POST['price']
        book = Book.objects.get(id=bookid)
        book.title = t
        book.author = a
        book.price = p
        book.save()
        return redirect('/home')
