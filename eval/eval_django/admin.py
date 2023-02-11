from django.contrib import admin
from .models import eval_class, evaluator_name, evaluated_subject

admin.site.register(eval_class)
admin.site.register(evaluator_name)
admin.site.register(evaluated_subject)
