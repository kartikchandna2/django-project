from django.db import models

class eval_class(models.Model):

    id = models.IntegerField(primary_key=True)
    eval_name = models.CharField(max_length = 100, null = False)
    eval_subject = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return str(self.id)

class evaluator_name(models.Model):
    eval_id = models.IntegerField(primary_key=True)
    eval_name = models.ForeignKey(
        eval_class, related_name = "%(class)s_evaluatedby",
        on_delete = models.CASCADE, null = False)
    eval_age = models.IntegerField(null = True)
    
    def __str__(self):
        return self.eval_name

class evaluated_subject(models.Model):
    eval_id = models.IntegerField(primary_key=True)
    eval_subject = models.ForeignKey(
        eval_class, related_name= "%(class)s_evaluatedsubject", 
        on_delete=models.CASCADE, null = False)
    
