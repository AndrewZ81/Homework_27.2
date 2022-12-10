import json
from typing import List, Dict

from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Advertisement


def show_main_page(request) -> HttpResponse:
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    """
    Отображает таблицу Category, делает выборку записи из Category по id
    или создаёт новую запись Category
    """
    def get(self, request) -> JsonResponse:
        categories = Category.objects.all()
        response_as_list: List[Dict[str, int | str]] = []
        for category in categories:
            response_as_list.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )
        return JsonResponse(response_as_list, safe=False,
                            json_dumps_params={"ensure_ascii": False, "indent": 4})

    def post(self, request) -> JsonResponse:
        category_data = json.loads(request.body)
        category: Category = Category(**category_data)
        category.save()
        response_as_dict: Dict[str, int | str] = {
            "id": category.id,
            "name": category.name
        }
        return JsonResponse(response_as_dict, json_dumps_params={"ensure_ascii": False, "indent": 4})


class CategoryDetailView(DetailView):
    """
    Делает выборку записи из таблицы Category по id
    """
    model = Category

    def get(self, request, *args, **kwargs) -> JsonResponse:
        category = self.get_object()

        response = {
            "id": category.id,
            "name": category.name
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4})


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
