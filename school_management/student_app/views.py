from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from models import Teachers 

# Create your views here.
def show_teacher_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        joining_date = request.POST.get('joining_date')

    if all(name,age,email,salary,joining_date):
        try:
            Teachers.objects.create(
                name = name,
                age = age,
                email = email,
                salary = salary,
                joining_date = joining_date
            )
            return JsonResponse({"status": "Success","message": "Congratualtions!"})
        except Exception as e:
            return JsonResponse({"status": "Failed","message": str(e)})
