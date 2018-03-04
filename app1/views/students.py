from django.shortcuts import render, redirect
from app1.models import Students, Classes


# 学生表的增删改查
def get_students(request):
    stu_list = Students.objects.all()
    return render(request, 'get_students.html', {'stu_list': stu_list})


def add_students(request):
    if request.method == 'GET':
        cs_list = Classes.objects.all()
        return render(request, 'add_students.html', {'cs_list': cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username', '')
        a = request.POST.get('age', '')
        g = request.POST.get('gender', '')
        c = request.POST.get('cs', '')
        Students.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')


def del_students(request):
    nid = request.GET.get('nid', '')
    Students.objects.filter(id=nid).delete()
    return redirect('/students.html')


def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        obj = Students.objects.get(id=nid)
        cs_list = Classes.objects.all()
        return render(request, 'edit_students.html', {'obj': obj, 'cs_list': cs_list})
    elif request.method == 'POST':
        nid = request.POST.get('nid', '')
        u = request.POST.get('username', '')
        a = request.POST.get('age', '')
        g = request.POST.get('gender', '')
        c = request.POST.get('cs', '')
        Students.objects.filter(id=nid).update(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')


