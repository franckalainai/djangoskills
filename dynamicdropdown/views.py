from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from .models import Subject, Topic

# Create your views here.

def dropdown(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'dropdown.html', context)


def get_topics_ajax(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        try:
            subject = Subject.objects.filter(id = subject_id).first()
            topics = Topic.objects.filter(subject = subject)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(topics.values('id', 'title')), safe = False) 