
from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import EmployeeForm,Employee_Edit_Form
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# def home_page(request): return render(request, 'home_page.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('employee_list')
        else:
            return HttpResponse("Invalid credentials or not an admin")
    return render(request, 'admin_login.html')


def employee_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            data =Member.objects.get(user = user)
            print(user,"hii")
            name=user.first_name
            return render(request, 'employee_details.html', {'mymember': data,"name":name})
        else:
            return HttpResponse("Invalid credentials")
    else:
      try:
        request.user.is_authenticated
        data =Member.objects.get(user = user)
        name=user.first_name
        return render(request, 'employee_details.html', {'mymember': data,"name":name})
      except:
          return render(request, 'login.html')



def employee_detail_edit(request,pk):
    employee = get_object_or_404(Member, pk=pk)
    return render(request, 'employee_details.html', {'mymember': employee})


def employee_update_edit(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = Employee_Edit_Form(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_login')
    else:
      form = Employee_Edit_Form(instance=employee)
      return render(request, 'employee_edit_form.html', {'form': form})


def employee_list(request):
    if request.user.is_authenticated:
      employees = Member.objects.all() 
      # print(employees)
      return render(request, 'employee_list.html', {'employees': employees})
    else:
        return redirect('admin_login')

def employee_detail(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    return render(request, 'details.html', {'mymember': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def logout_view(request):
    logout(request)
    return redirect('admin_login')
