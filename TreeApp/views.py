from django.shortcuts import render
from .models import Menu

# Доступ к БД для получения списка всех меню
# Предполагается, что он не является частью условия №8 (одного запроса к БД), т.к. меню и их пункты - разные БД
# Для отрисовки каждого меню всё ещё реализуется только 1 запрос к БД
def db_access():

    menu_table = Menu.objects.all()

    result = []

    for obj in menu_table:
        result.append(obj.menu_name)

    return result


# Странциа отображения всех меню
def view_all_menus(request):

    menu_names = db_access()

    html = "menu_list.html"
    data = {"menu_list": menu_names}

    response = render(request, html, context=data)

    return response


# Страница отображения конкретного меню
def view_single_line(request, menu, line):

    strip_menu = menu[1:]

    html = "single_menu.html"
    data = {"menu": strip_menu, "line": line}

    response = render(request, html, context=data)

    return response
