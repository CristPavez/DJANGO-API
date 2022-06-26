from cgi import test
import json
from tkinter import Y
from django.shortcuts import render
from django.views import View
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from .models import Test, DataFrame_Model
from django.http import HttpRequest, JsonResponse
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Models.dataframe import test

from sklearn.ensemble import RandomForestClassifier
import seaborn as sb
import matplotlib.pyplot as plt
# Create your views here.
class ListaView(View):
  def get(self, request):
    if('numero1' in request.GET):
      Tlist = Test.objects.filter(numero1__contains=request.GET['numero1'])
    else:
      Tlist = Test.objects.all()
    return JsonResponse(list(Tlist.values()), safe=False)


class Lista_PView(View):
  def get(self, request,pk):
    Numero = Test.objects.get(pk=pk)
    return JsonResponse(model_to_dict(Numero))



class DataFrame_ModelV(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request: HttpRequest, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def get(self, request):
    if('x' in request.GET):  
      x2 = DataFrame_Model.objects.filter(x__contains=request.GET['x'])
 
    else:
      x2 = DataFrame_Model.objects.all()
    return JsonResponse(list(x2.values()), safe=False)

  def post(self, request):
    js = json.loads(request.body)
    Dato = js['Dato'] 
    Drop_Table = js['Drop_Table'] 
    n_estimators = js['n_estimators']
    bootstrap = js['bootstrap']
    verbose = js['verbose']
    max_features = js['max_features']
    Dataframe = js['Dataframe']
    #DATAFRAMME//////////////////////////////////////////////
    LABELS = ["Normal","Fraud"]
    y = test[Dato]
    print(y)
    X = test.drop(Drop_Table, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)
    
    model = RandomForestClassifier(n_estimators=n_estimators, 
                                  bootstrap = bootstrap,verbose=verbose,
                                  max_features = max_features)
    
    model.fit(X_train, y_train)
    def mostrar_resultados(y_test, pred_y):
      conf_matrix = confusion_matrix(y_test, pred_y)
      plt.figure(figsize=(8, 8))
      sb.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
      plt.title("Confusion matrix")
      plt.ylabel('True class')
      plt.xlabel('Predicted class')
       
      plt.show()
 
       
    pred_y = model.predict(X_test)
    mostrar_resultados(y_test, pred_y)
    report = classification_report(y_test, pred_y)
    print (classification_report(y_test, pred_y))
    #DATAFRAMME ///////////////////////////////////////////////
    DataFrame_Model.objects.create(Dato = Dato,Drop_Table=Drop_Table,n_estimators=n_estimators,verbose=verbose,max_features=max_features,Dataframe=Dataframe,bootstrap=bootstrap,report=report)
    datos = {'message':'Success'}
    return JsonResponse(datos, safe=False)
  

  # def post(self, request):
  #   jd = json.loads(request.body)
  #   MX = jd['X']
  #   suma = MX + 10
  #   MY = jd['Y']
  #   Test2.objects.create(x =suma,y = MY)
  #   datos = {'message':'Success'}
  #   return JsonResponse(datos, safe=False)

  # def post(self, request):
  # def put(self, request):
  # def delete(self, request):