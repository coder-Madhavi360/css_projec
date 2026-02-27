from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def colleges(request):
    colleges_list = ['SVECW', 'VIT', 'BVRIT']
    return render(request, 'colleges.html', {'colleges': colleges_list})

def students(request):
    students_list = [
        {'sno': 1, 'name': 'Madhavi', 'branch': 'CSE', 'age': 17},
        {'sno': 2, 'name': 'Harshitha', 'branch': 'IT', 'age': 19},
        {'sno': 3, 'name': 'Vennela', 'branch': 'ECE', 'age': 18},
    ]
    return render(request, 'students.html', {'students': students_list})

def address(request):
    return render(request, 'address.html')