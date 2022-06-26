from msilib.schema import Class
from unicodedata import name
from django.db import models

# Create your models here.
class Test(models.Model):
  numero1 = models.CharField(max_length=50)
  numero2 = models.CharField(max_length=50)
  resultado = models.CharField(max_length=50)

class Test2(models.Model):
  y = models.CharField(max_length=50)
  x = models.CharField(max_length=50)


class DataFrame_Model(models.Model):
  Dato = models.CharField(max_length=50)
  Drop_Table = models.CharField(max_length=50)
  n_estimators = models.IntegerField()
  bootstrap = models.BooleanField()
  verbose = models.IntegerField()
  max_features = models.CharField(max_length=50)
  Dataframe = models.FileField();
  Agregar = 'True'
  NoAgregar = 'False'
  op = [
        (Agregar, 'True'),
        (NoAgregar, 'False'),
 
    ]
  bootstrap = models.CharField(
      max_length=5,
      choices=op,
      default=Agregar,
  )
  report = models.CharField(max_length=500)