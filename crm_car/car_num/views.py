from django.shortcuts import render
from car_num.models import PlateNum
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


#JSON
def platenum_json(request):
    platenums = PlateNum.objects.all()
    data = [platenum.get_data() for platenum in platenums]
    response = {'data': data}
    return JsonResponse(response)



