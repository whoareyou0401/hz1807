print("6666666")
print("jsjsj")
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, QueryDict
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Book
from .my_signals import my_signal
from .STATUS import *
# Create your views here.
def create_book(req):
    book = Book()
    book.name = "呵呵"
    book.price = 20
    book.save()
    my_signal.send("达达", cid=1, nid=2)
    return HttpResponse("OK")

def book_api(req):

    if req.method == "GET":
        # 获取数据
        id = req.GET.get("id")
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            book = None
        except Book.MultipleObjectsReturned:
            book = None

        res = {}
        if book:
            # 将模型转字典
            res = model_to_dict(book)
        return JsonResponse(res)
    elif req.method == "POST":
        # 创建数据
        name = req.POST.get("name")
        price = req.POST.get("price")
        Book.objects.create(
            name=name,
            price=float(price)
        )
        res = {
            "code": 0,
            "msg": "创建完成",
            "data": ""
        }
        return JsonResponse(res, status=CREATED_STATUS_201)
    elif req.method == "PUT":
        # 修改
        params = QueryDict(req.body)
        id = params.get("id")
        book = Book.objects.get(pk=int(id))

        book.name = params.get("name", book.name)
        book.price = float(params.get("price", book.price))
        book.save()
        res = {
            "code": 0,
            "msg": "updated",
            "data": model_to_dict(book)
        }
        return JsonResponse(res, status=UPDATED_STATUS_201)
    elif req.method == "DELETE":
        # 删除
        params = QueryDict(req.body)
        book = Book.objects.get(pk=params.get("id"))
        book.delete()
        res = {
            "code": 0,
            "msg": "删除成功",
            "data": ""
        }
        return JsonResponse(res, status=DELETED_STATUS_204)
    else:
        return HttpResponseNotAllowed("请求方式不正确")

class BookApi(View):

    def get(self, req):
        # 获取数据
        id = req.GET.get("id")
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            book = None
        except Book.MultipleObjectsReturned:
            book = None

        res = {}
        if book:
            # 将模型转字典
            res = model_to_dict(book)
        return JsonResponse(res)

    def post(self, req):
        # 创建数据
        name = req.POST.get("name")
        price = req.POST.get("price")
        Book.objects.create(
            name=name,
            price=float(price)
        )
        res = {
            "code": 0,
            "msg": "创建完成",
            "data": ""
        }
        return JsonResponse(res, status=CREATED_STATUS_201)

    def put(self, req):
        # 修改
        params = QueryDict(req.body)
        id = params.get("id")
        book = Book.objects.get(pk=int(id))

        book.name = params.get("name", book.name)
        book.price = float(params.get("price", book.price))
        book.save()
        res = {
            "code": 0,
            "msg": "updated",
            "data": model_to_dict(book)
        }
        return JsonResponse(res, status=UPDATED_STATUS_201)

    def delete(self, req):
        # 删除
        params = QueryDict(req.body)
        book = Book.objects.get(pk=params.get("id"))
        book.delete()
        res = {
            "code": 0,
            "msg": "删除成功",
            "data": ""
        }
        return JsonResponse(res, status=DELETED_STATUS_204)

class HelloTemplateView(TemplateView):
    template_name = "html_one.html"


class MyListView(ListView):
    # model = Book
    queryset = Book.objects.all()
    template_name = "books.html"
    # 指定每一页有多少数据
    # paginate_by = 3
    # allow_empty = False

class BookDetailView(DetailView):
    model = Book
    slug_field = slug_url_kwarg = "name"
