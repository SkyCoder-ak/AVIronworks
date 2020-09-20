from django.shortcuts import render
from django.http import HttpResponse
from AVShopProject import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect,HttpResponseRedirect
from .forms import ContactForm
from django.http.response import HttpResponseNotAllowed

# Create your views here.
def thankyou_view(request):
    thanks_head = "Thanks For Contacting Us!"
    thanks_para = "We care about your every inquiry. Be some patient we will shortly in touch with you."
    return render(request,'contact_app/thankyou.html',{'thanks_head':thanks_head,'thanks_para':thanks_para})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            all_data = f"Name: {name}\nCity/Village: {city}\nMobile: {mobile}\nMessage:{message}\n"
            subject = "Message Form Contact Page."
            sender = 'beyondhorrizon7@gmail.com'
            recipients = ['avironworks21@gmail.com']

            sent = send_mail(subject, all_data, sender, recipients,fail_silently=True,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD)
            if sent == 1:
                return redirect('/contact-success')
            else:
                messages.warning(request,'Failed, Your message not sent. Try again!')
                return redirect('/')
            # return redirect('/thankyou')

            
    else:
        form = ContactForm()
    return render(request,'contact_app/contact.html',{'form':form})


