from django.http import HttpResponse
from django.shortcuts import render, redirect
from app1.models import Classes, Teachers


# classes表的增删改查
def get_classes(request):
    cls_list = Classes.objects.all()
    return render(request, 'get_classes.html', {'cls_list': cls_list})


def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        Classes.objects.create(title=title)
        return redirect('/classes.html')


def del_classes(request):
    nid = request.GET.get('nid', '')
    Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')


def edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get('nid', '')
        obj = Classes.objects.get(id=nid)
        return render(request, 'edit_classes.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('nid', '')
        title = request.POST.get('xxoo', '')
        Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')


def testdb(request):
    test1 = Classes(title='anyi')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def set_teachers(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        cls_obj = Classes.objects.get(id=nid)
        cls_teacher_list = cls_obj.a.all()
        all_teacher_list = Teachers.objects.all()
        return render(request, 'set_teachers.html', {
            'cls_teacher_list': cls_teacher_list,
            'all_teacher_list': all_teacher_list,
            'nid': nid,
        })
    elif request.method == 'POST':
        nid = request.POST.get('nid', '')
        ids_str = request.POST.getlist('teacher_id', '')
        ids_int = []
        for i in ids_str:
            i = int(i)
            ids_int.append(i)
        obj = Classes.objects.get(id=nid)
        obj.a.set(ids_int)
        return redirect('/classes.html')

