from django.shortcuts import render, redirect, HttpResponse
from app1 import models


def ajax1(request):
    return render(request, 'ajax1.html')


def ajax2(request):
    u = request.GET.get('username')
    p = request.GET.get('password')
    return HttpResponse('我愿意')


def ajax4(request):
    nid=request.GET.get('nid')
    msg='成功'
    try:
        models.Students.objects.get(id=nid).delete()
    except Exception as e:
        msg = str(e)
    return HttpResponse(msg)

