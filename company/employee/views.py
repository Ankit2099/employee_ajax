from django.shortcuts import render
from django.views.generic import ListView,View
from employee.models import *
from django.http import JsonResponse, HttpResponse

# Create your views here.
# def home(request):
#     return render(request, 'base.html',{'context':'anshu'})


class HomeView(ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employee'

class CreateEmployee(View):
    def get(self,request):
        name1 = request.GET.get('name')
        roll1 = request.GET.get('roll_no')
        class1 = request.GET.get('class_name')
        obj = Employee.objects.create(
           name = name1,
           roll_no = roll1,
           class_name = class1,
        )

        user = {'id':obj.id, 'name':obj.name, 'roll_no':obj.roll_no,'class_name':obj.class_name}

        data = {'user':user}

        return JsonResponse(data)

class DeleteEmployee(View):
    def get(self, request):
        empty = False
        id1 = request.GET.get('id')
        Employee.objects.get(id=id1).delete()
        queryset = Employee.objects.all()
        if not queryset.exists():
            empty=True
        print(empty)
        data = {
            'deleted': True,
            'empty'  : empty
        }
        return JsonResponse(data)

class UpdateEmployee(View):
    def get(self,request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        roll1 = request.GET.get('roll_no', None)
        class1 = request.GET.get('class_name', None)

        print(roll1)

        obj = Employee.objects.get(id=id1)
        obj.name = name1
        obj.roll_no = roll1
        obj.class_name = class1
        obj.save()
        print(obj)

        user = {
            'id':obj.id, 
            'name':obj.name, 
            'roll_no':obj.roll_no,
            'class_name':obj.class_name
        }

        data = {'user':user}

        return JsonResponse(data)