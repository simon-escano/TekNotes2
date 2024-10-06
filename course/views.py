from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm

@login_required
def add_a_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('/')
    else:
        form = CourseForm()

    return render(request, 'course/add_a_course.html', {'form': form})
