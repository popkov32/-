from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def func_view(request):
    """
    Функция, возвращающая представление с помощью функционального подхода.
    :param request: объект запроса.
    :return: представление на основе шаблона - func_template.html.
    """
    return render(request, 'func_template.html')

def class_view(request):
    """
    Функция, возвращающая представление с помощью классового подхода.
    :param request: объект запроса.
    :return: представление на основе шаблона - class_template.html.
    """
    return render( request, 'class_template.html' )

# def main_view(request):
#     return render(request, 'main_template.html')

