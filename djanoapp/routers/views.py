from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

async def get_all_employees(request):
    employees = {
            "id" : 1,
            "name" : "Sudharsan",
            "stack" : "python",
        }    
    return JsonResponse(employees)
