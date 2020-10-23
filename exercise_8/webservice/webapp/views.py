from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Employee_Details
from . import models
import json
from .serializers import EmployeeSerializers

class EmpView(APIView):

    def get(self, request, *args, **kwargs):
        params = request.GET.keys()
        if not params:
            data = models.get_all_object()
        else:
            filter_query = list(params)[0]
            query_val = request.GET.get(filter_query)
            if filter_query == 'e_id':
                data = models.filter_by_id(query_val)

            elif filter_query == 'e_name':
                data = models.filter_by_name(query_val)

            elif filter_query == 'e_loc':
                data = models.filter_by_e_loc(query_val)

            elif filter_query == 'designation':
                data = models.filter_by_designation(query_val)

            elif filter_query == 'top_emp':
                data = models.get_top_emp(query_val)
            else:
                data = "Error !"

        return JsonResponse({'data': data})

    def delete(self, request):
        data = request.data
        response=models.delete_emp(data['e_id'])
        return JsonResponse({"response":response})

    def post(self, request):
        data = request.data
        e_id = data['e_id']
        e_name = data['e_name']
        e_sal = data['e_sal']
        e_loc = data['e_loc']
        email = data['email']
        designation = data['designation']
        emp_obj = Employee_Details(e_id, e_name, e_sal, e_loc, email, designation)
        response=emp_obj.add_employee()
        return JsonResponse({'response': response})


