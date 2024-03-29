from django.shortcuts import render, redirect
from django.core.mail import send_mail
from nomanapp.forms import appointmentform
from nomanapp.models import Appointment
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "home.html/", {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST["message_name"]
        message_email = request.POST["message_email"]
        message_subject = request.POST["message_subject"]   
        umessage = request.POST["umessage"]

        # Define the email content
        subject = 'Subject: {}'.format(message_subject)
        message_content = 'From: {}\n\n{}'.format(message_name, umessage)
        from_email = 'example@example.com'  # Use a valid sender email address
        to_email = ['recipient@example.com']  # Use a list of recipient email addresses

        # Send email
        send_mail(subject, message_content, from_email, to_email)

        # Redirect or render a success page
        return render(request, 'home.html')

    return render(request, 'contact.html')

def about(request):
    return render(request, "about.html/", {})

def services(request):
    return render(request, "services.html/", {})

def appointment(request):
    form=appointmentform()
    if request.method == "POST":
        form = appointmentform(request.POST)
        if form.is_valid():
            disease_category = form.cleaned_data['disease_category']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            phone = form.cleaned_data['phone']
    
            reg=Appointment(disease_category=disease_category, name=name, email=email, date=date, time=time, phone=phone)
            reg.save()
            return redirect('thank_you')

        
    return render(request, "appointment.html", {'form': form})
            

def thank_you(request):
    return render(request, "thank_you.html/")