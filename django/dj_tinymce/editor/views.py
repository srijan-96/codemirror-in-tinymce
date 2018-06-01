from django.shortcuts import render
from django.http import HttpResponse
from .models import EditorData
# Create your views here.

def index(request):
    all_editors = EditorData.objects.all()
    ret = '<h1>This is the list of all the editors in database</h1><br><h3><ul>'
    for editor in all_editors:
        url = '/editor/' + str(editor.id) + '/'
        ret += '<li><a href="' + url + '">' + editor.name + '</a></li>'
    ret += '</ul></h3>'
    return HttpResponse(ret)

def nth_editor(request, editor_id):
    return HttpResponse("<h2>This is editor " + str(editor_id) + " : </h2>")
