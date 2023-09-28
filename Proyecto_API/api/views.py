from django.views import View
from .models import Company
from django.http.response import JsonResponse



# Create your views here.

class CompanyView(View):

    def get(self,request):
        companies = list(Company.objects.values())
        if len(companies)>0:
            datos={'message':"Sucess",'companies': companies}
        else:
            datos={'message': "Companies not found..."}

        return JsonResponse(datos)
    
        

    def post(self,request):
        datos={'message':"Sucess"}
        return JsonResponse(datos)

    def put(self,request):
        

     def delete(self,request):
        pass

