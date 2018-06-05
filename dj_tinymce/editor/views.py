from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EditorData
from .BasicHtmlParser import convertHTML
# Create your views here.

def index(request):
    all_editors = EditorData.objects.all()
    context = { "all_editors" : all_editors }
    return render(request, 'editor/index.html', context)

def nth_editor(request, editor_id):
    editor = EditorData.objects.get(id=editor_id)
    context = {'editor' : editor}
    return render(request, 'editor/edit-nth.html', context)

@csrf_exempt
def save_nth_editor(request, editor_id):
    if request.method == 'POST':
        htmlContent = request.POST.get('htmlContent', None)
        editor = EditorData.objects.get(id=editor_id)
        editor.htmlContent = htmlContent
        editor.showHTML = htmlContent
        editor.save()
        ret = {
            'saved': 'True'
        }
        return JsonResponse(ret)
    else:
        return render(request, 'editor/edit-nth.html', context)
