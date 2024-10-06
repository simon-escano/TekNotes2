from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Note, Like, Dislike
from .models import Comment

@login_required
def comment(request, note_id):
    note = Note.objects.get(id=note_id)
    content = request.POST.get('comment', '')
    if content:
        Comment.objects.create(user=request.user, note=note, content=content)
    return redirect('notes:note_detail', note_id=note_id)

@login_required
def like(request, note_id):
    note = Note.objects.get(id=note_id)
    like, created = Like.objects.get_or_create(user=request.user, note=note)
    if not created:
        like.delete()
    Dislike.objects.filter(user=request.user, note=note).delete()
    return redirect('notes:note_detail', note_id=note_id)

@login_required
def dislike(request, note_id):
    note = Note.objects.get(id=note_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, note=note)
    if not created:
        dislike.delete()
    Like.objects.filter(user=request.user, note=note).delete()
    return redirect('notes:note_detail', note_id=note_id)
