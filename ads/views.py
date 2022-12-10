from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
from ads.models import Category, Advertisement


def show_main_page(request) -> HttpResponse:
    return JsonResponse({"status": "ok"})


def show_categories(request) -> JsonResponse:
    """
    Отображает таблицу Category в формате списка словарей
    :param request:
    :return:
    """
    if request.method == "GET":
        categories = Category.objects.all()
        response: list = []
        for category in categories:
            response.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )
        return JsonResponse(response, safe=False,
                            json_dumps_params={"ensure_ascii": False, "indent": 4})


def show_advertisements(request) -> JsonResponse:
    """
    Отображает таблицу Advertisement в формате списка словарей
    :param request:
    :return:
    """
    if request.method == "GET":
        advertisements = Advertisement.objects.all()
        response: list = []
        for advertisement in advertisements:
            response.append(
                {
                    "id": advertisement.id,
                    "name": advertisement.name,
                    "author": advertisement.author,
                    "price": advertisement.price,
                }
            )
        return JsonResponse(response, safe=False,
                            json_dumps_params={"ensure_ascii": False, "indent": 4})
