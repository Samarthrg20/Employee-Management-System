from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.contrib import messages
from datetime import datetime, timedelta


# 📋 Employee List + Search + Dashboard Data
def employee_list(request):
    query = request.GET.get('q')

    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()

    # Total employees
    total_count = employees.count()

    # New employees (last 7 days)
    last_week = datetime.now() - timedelta(days=7)
    new_count = Employee.objects.filter(created_at__gte=last_week).count()

    return render(request, 'employee_list.html', {
        'employees': employees,
        'query': query,
        'total_count': total_count,
        'new_count': new_count
    })


# 👁️ Employee Detail
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_detail.html', {'employee': employee})


# ➕ Create Employee
def employee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        # Validation
        if not name or not email or not age:
            messages.error(request, "All fields are required!")
            return redirect('employee_create')

        Employee.objects.create(name=name, email=email, age=age)
        messages.success(request, "Employee added successfully!")

        return redirect('employee_list')

    return render(request, 'employee_form.html')


# ✏️ Update Employee
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.age = request.POST.get('age')
        employee.save()

        messages.success(request, "Employee updated successfully!")
        return redirect('employee_list')

    return render(request, 'employee_form.html', {'employee': employee})


# ❌ Delete Employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employee_list')

    return render(request, 'employee_confirm_delete.html', {'employee': employee})