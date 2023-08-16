from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'service.html')



from django.contrib import messages


def contact1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        phone_number = request.POST.get('phone_number')  # Add 'phone_number' field
        
        if not name or not email or not subject or not description or not phone_number:
            messages.error(request, "Please fill in all fields.")
        else:
            contact = Contact(
                name=name,
                email=email,
                subject=subject,
                description=description,
                phone_number=phone_number  # Add phone_number
            )
            contact.save()
            messages.success(request, "Success")
            return redirect('/contact')  # Redirect to a success page

    return render(request, 'contact.html')
