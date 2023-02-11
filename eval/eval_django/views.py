# from django.shortcuts import render
# from django.views.generic.detail import DetailView
# from .models import eval_class, evaluated_subject, evaluator_name

# class eval_detail_view(DetailView):
#     model = eval_class

# class eval_name_dview(DetailView):
#     model = evaluator_name

# class eval_sub_dview(DetailView):
#     model = evaluated_subject

# class Template(request):
#     return render(request, 'eval_class_detail.html')

from rest_framework.views import APIView
from django.shortcuts import render
#from rest_framework.decorators import api_view

def TemplateView(request):
    return render(request, 'eval_class_detail.html')
