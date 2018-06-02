from django.shortcuts import render
from django.http import HttpResponse
from .models import EditorData
# Create your views here.

def index(request):
    all_editors = EditorData.objects.all()
    context = { "all_editors" : all_editors }
    return render(request, 'editor/index.html', context)

def nth_editor(request, editor_id):
    return HttpResponse("<h2>This is editor " + str(editor_id) + " : </h2>")
