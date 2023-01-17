from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = form.cleaned_data['recipients']
            recipient_list = recipients.split(',')
            send_mail(subject, message, 'from@example.com', recipient_list)
            return redirect('/success')
    else:
        form = EmailForm()
    return render(request, 'contact/email_form.html', {'form': form})

def success(request):
    return render(request, 'contact/success.html')
