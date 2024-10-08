from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery
from notes.models import Note
from course.models import Course
from tags.models import Tag
from comments.models import Like

def index(request):
    notes = Note.objects.filter(is_archived=False, is_private=False).order_by('-modified_at')
    courses = Course.objects.filter(note__in=notes).distinct()
    tags = Tag.objects.filter(notes__in=notes).distinct()

    return render(request, 'core/index.html', {
        'notes': notes,
        'courses': courses,
        'tags': tags
    })

@login_required
def your_notes(request):
    your_notes = Note.objects.filter(created_by=request.user, is_archived=False).order_by('-modified_at')
    courses = Course.objects.filter(note__in=your_notes).distinct()
    tags = Tag.objects.filter(notes__in=your_notes).distinct()

    return render(request, 'core/your_notes.html', {
        'notes': your_notes,
        'courses': courses,
        'tags': tags
    })

@login_required
def archive(request):
    archived_notes = Note.objects.filter(created_by=request.user, is_archived=True).order_by('-modified_at')
    courses = Course.objects.filter(note__in=archived_notes).distinct()
    tags = Tag.objects.filter(notes__in=archived_notes).distinct()

    return render(request, 'core/archive.html', {
        'notes': archived_notes,
        'courses': courses,
        'tags': tags
    })

@login_required
def likes(request):
    latest_likes = Like.objects.filter(note=OuterRef('pk'), user=request.user).order_by('-created_at')
    liked_notes = Note.objects.filter(likes__user=request.user, is_private=False).annotate(
        like_created_at=Subquery(latest_likes.values('created_at')[:1])
    ).distinct().order_by('-like_created_at')

    courses = Course.objects.filter(note__in=liked_notes).distinct()
    tags = Tag.objects.filter(notes__in=liked_notes).distinct()

    return render(request, 'core/likes.html', {
        'notes': liked_notes,
        'courses': courses,
        'tags': tags
    })