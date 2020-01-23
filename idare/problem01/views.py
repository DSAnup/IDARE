from django.shortcuts import render
from django.http import HttpResponse
import math
# Create your views here.

def home(request):
    return render(request, 'home.html')

def calculate(request):
    pod = float(request.POST['pod'])
    pwt = float(request.POST['pwt'])
    pdensity = float(request.POST['pdensity'])
    coallow = float(request.POST['coallow'])
    fbethick = float(request.POST['fbethick'])
    fbedensity = float(request.POST['fbedensity'])
    ieair = float(request.POST['ieair'])
    fwater = float(request.POST['fwater'])
    hswater = float(request.POST['hswater'])
    pipInsideRadius = (pod -(2*pwt))/2
    pipOutsideRadius = pod/2
    outerRadiusCoat = pipOutsideRadius + (fbethick/2)
    totalPipeline = outerRadiusCoat * 2
    pipeWeightUnit = math.pi*(pipOutsideRadius**2-pipInsideRadius**2)/144*pdensity
    coatUnit = math.pi *(outerRadiusCoat**2 - pipOutsideRadius**2)/144*fbedensity
    contentsLength = math.pi*(pipInsideRadius**2/144*ieair)
    totalWeight = pipeWeightUnit + coatUnit + contentsLength
    buoyantForce = math.pi * (outerRadiusCoat**2/144*hswater)
    submergedWeight = totalWeight - buoyantForce
    subGravity = totalWeight/buoyantForce
    result = {'pipInsideRadius': pipInsideRadius,
              'pipOutsideRadius': pipOutsideRadius,
              'outerRadiusCoat': outerRadiusCoat,
              'totalPipeline': totalPipeline,
              'pipeWeightUnit': pipeWeightUnit,
              'coatUnit': coatUnit,
              'contentsLength': contentsLength,
              'totalWeight': totalWeight,
              'buoyantForce': buoyantForce,
              'submergedWeight': submergedWeight,
              'subGravity': subGravity
              }
    return render(request, 'result.html', {'result': result})