from django.shortcuts import render
from django.db.models import Q
from notes.models import Note

def search(request):
    query = request.GET.get('query', '')
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(course__description__icontains=query) |
            Q(created_by__username__icontains=query) |
            Q(created_by__first_name__icontains=query) |
            Q(created_by__last_name__icontains=query)
        ).distinct()
    else:
        notes = Note.objects.all()

    return render(request, 'core/index.html', {
        'notes': notes,
        'query': query,
    })