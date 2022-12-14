import collections
import json
from typing import List, Dict

from django.http import JsonResponse

# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Advertisement


def show_main_page(request) -> JsonResponse:
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    """
    Отображает таблицу Category или создаёт новую запись Category
    """
    def get(self, request) -> JsonResponse:
        categories: collections.Iterable = Category.objects.all()
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
        category_data: Dict[str, int | str] = json.loads(request.body)
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
        category: Category = self.get_object()
        response: Dict[str, int | str] = {
            "id": category.id,
            "name": category.name
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementView(View):
    """
    Отображает таблицу Advertisement или создаёт новую запись Advertisement
    """
    def get(self, request) -> JsonResponse:
        advertisements: collections.Iterable = Advertisement.objects.all()
        response_as_list: List[Dict[str, int | str]] = []
        for advertisement in advertisements:
            response_as_list.append(
                {
                    "id": advertisement.id,
                    "name": advertisement.name,
                    "author": advertisement.author,
                    "price": advertisement.price,
                }
            )
        return JsonResponse(response_as_list, safe=False,
                            json_dumps_params={"ensure_ascii": False, "indent": 4})

    def post(self, request) -> JsonResponse:
        advertisement_data: Dict[str, int | str] = json.loads(request.body)
        advertisement: Advertisement = Advertisement(**advertisement_data)
        advertisement.save()
        response_as_dict: Dict[str, int | str] = {
            "id": advertisement.id,
            "name": advertisement.name,
            "author": advertisement.author,
            "price": advertisement.price,
            "description": advertisement.description,
            "address": advertisement.address,
            "is_published": advertisement.is_published
        }
        return JsonResponse(response_as_dict, json_dumps_params={"ensure_ascii": False, "indent": 4})


class AdvertisementDetailView(DetailView):
    """
    Делает выборку записи из таблицы Advertisement по id
    """
    model = Advertisement

    def get(self, request, *args, **kwargs) -> JsonResponse:
        advertisement: Advertisement = self.get_object()
        response: Dict[str, int | str] = {
            "id": advertisement.id,
            "name": advertisement.name,
            "author": advertisement.author,
            "price": advertisement.price,
            "description": advertisement.description,
            "address": advertisement.address,
            "is_published": advertisement.is_published
        }
        return JsonResponse(response, safe=False,
                            json_dumps_params={"ensure_ascii": False, "indent": 4})
