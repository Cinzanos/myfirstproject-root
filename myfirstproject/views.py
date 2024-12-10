# Создадим функцию с параметром request
# Этот параметр означает что каждый раз когда кто то ищет какую то веб страницу
# на нашем веб сайте он отправляет этот request(запрос) запрос url который он хочет и также этот запрос содержит куки(cookies) какой браузер используется и тд все это приходит с этим запросом(request)
# И внутри этой функции мы должны возвратить http response объект нужно импортировать hhtp response из django

from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')


# def home(request):
#     return HttpResponse('<h1>This is home</h1>') # можно также передавать html элементы какие то
# Но если мы хотим передать какой то большой html код (файл) мы не должны это делать через HttpResponse
# для этого используют Templates(шаблоны)
# Templates - это HTML код в который мы можем помещать какой то джанго код или пайтон код

def home(request):
    return render(request, 'home.html', {'greeting':'Hello!'}) # Передаем теперь наш файл с html кодом внутри в папке templates
# Также тут можно передавать словарь greeting