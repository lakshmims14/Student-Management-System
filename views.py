from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import StudentForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def index(request):
    course=Course.objects.all()
    return render(request,'index.html',{'course':course})

def courses(request):
    return render(request,'courses.html')

def contact(request):
    return render(request,'contact.html')

def detail(request,pk):
    course=Course.objects.get(pk=pk)
    return render(request,'detail.html',{'course':course})



@login_required
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'student.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    return render(request, 'student_detail.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})
    

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'form.html', {'form': form})
    


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete.html', {'student': student})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
